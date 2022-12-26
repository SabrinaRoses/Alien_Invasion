#Isolando os eventos de alien_invasion.py
from mimetypes import init
from tabnanny import check
from game_stats import GameStats
import sys
import pygame
from alien import Alien
from time import sleep
from bullet import Bullet



def check_keydown_events(event, ai_settings, screen, ship, bullets,):
    """Responde os eventos de pressionamento da tecla"""
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        som = pygame.mixer.Sound('music/bullet04.wav')
        som.play()
        
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
        #cria um novo projetil e adiciona ao grupo de projeteis
    if len(bullets) < ai_settings.bullets_allowed: #se len bullets for menor que tres criaremos um novo projetil
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """"Responde a solturas de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats,sb,play_button, ship, aliens, bullets):
    """Responde o pressionamento de teclas e mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Inicia um novo jogo quando o jogador clicar em play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if  button_clicked and not stats.game_active:
        #Reinicia as configuraçõe do jogo
        ai_settings.initialize_dynamic_settings()
        #reinicia os dados estatisticos do jogo
        stats.reset_stats()
        stats.game_active = True

        #Reinicia as imamges do paivel de pontuação
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        #esvazia a lista de aliens e de projeteis
        aliens.empty
        bullets.empty()

        #cria uma nova frota e centraliza a espaçonave
        #create_fleet(ai_settings, screen, ship, aliens) #isolei pois estava duplicando na primeira fase
        ship.center_ship()
        pygame.mouse.set_visible(False) #Tirando o cursor da tela do jogo
        
   
#atualização de tela
def update_screen(ai_settings, screen, ship, aliens, bullets, stats, sb, play_button):
    """Atualiza as imagens na tela e alterna para a nova tela"""
    #Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    #Redesenha todos os projeteis da espaçonave e dos aliens
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #Desenha informação sobre a pontuação
    sb.show_score()

    #Desenha o botão play se o jogo estiver inativo
    if not stats.game_active:
        play_button.draw_button()
    
    #deixa a tela mais recente visivel
    pygame.display.flip()

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
        """Responde as colisões entre os projeteis e aliens"""
    #verifica se algum projetil atingiu os aliens
    #em caso de afirmativo livra-se do projetil e do alien
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        if collisions:
            stats.score += ai_settings.alien_points
            sb.prep_score()
            check_high_score(stats, sb)



def update_bullets(ai_settings,screen,ship,aliens, bullets, stats, sb):
    """Atualiza a posição dos projeteis e se dos antigos"""
    bullets.update()
    #livra dos projeteis que desaparecem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #verifica se algum projetil atingiu os aliens
    #em caso de afirmativo livra-se do projetil e do alien
    #collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)   
    if len(aliens) == 0:
        #Destroi os projeteis existentes e cria uma nova frota
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        stats.level += 1
        sb.prep_level()
    
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

        

def get_number_aliens_x(ai_settings, alien_width):
    """"Determina o número de aliens que cabe numa linha"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/( 2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina o número de linhas com aliens que cabem na tela"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y /(2*alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #cria um alien e o posiciona na linha
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height +2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Cria uma frota completa de aliens"""
    #Cria um alien e calcula o número de alins em uma linha
    alien = Alien(ai_settings, screen)
   # alien_width = alien.rect.width 
   # available_space_x = ai_settings.screen_width - 2* alien_width
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    #cria uma fronta de alien
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
             create_alien(ai_settings, screen, aliens ,alien_number, row_number)
    #cria a primeira linha de aliens
    
        #cria uma um alien e o posiciona na linha
      #  alien = Alien(ai_settings, screen)
       # alien.x = alien_width + 2 * alien_width * alien_number
        #alien.rect.x = alien.x
        #liens.add(alien)
def check_fleet_edges(ai_settings, aliens):
    """Responde apropiadamente se algum alien alcançou a borda"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Faz a frota toda descer e mudar sua direção"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde ao fato de a espaçonave ter sido atingida por um alien"""
    if stats.ships_left > 0:
        #decrementa ships_left
        stats.ships_left -= 1

        #Atualiza o painel de pontuação
        sb.prep_ships()

        #esvazia a lista de alien e de projeteis
        aliens.empty()
        bullets.empty()

        #cria uma nova foto e centraliza a espaçnave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #faz uma pausa
        sleep(0.5)
    
        
    else:
        #som gamer over
        gameover = pygame.mixer.Sound('music/game-over.wav')
        gameover.play()
        stats.game_active = False
        pygame.mouse.set_visible(True) #Deixando o cursos visivel assim que o jogo torna-se inativo



def check_aliens_bottom(ai_settings, screen, stats,sb, ship, aliens, bullets):
    """verifica se algum alien alcançou a parte inferior da tela"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #trata esse caso do mesmo modo que é feito quando a espaçonave é antingida
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
        break

def check_high_score(stats, sb):
    """verifica se há uma nova pontuação máxima"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets): 
    """Atualiza as posições de todos os aliens da frota"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #verifica se houve colisoes entre aliens e a espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):
        #ship_hit(ai_settings, screen, stats, sb,  ship, aliens, bullets)
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
        #verifica se há algum alien que atingiu a parte inferior da tela
        check_aliens_bottom(ai_settings,screen, stats, sb,  ship, aliens, bullets)

    
    