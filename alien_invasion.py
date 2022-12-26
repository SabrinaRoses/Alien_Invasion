#Criando uma janela do Pygame e respondendo às entradas do usuário.
# Em primeiro lugar, criaremos uma janela vazia.

#criando um executavel
import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

#importando modulos (sys -> para sair do jogo) e (pygame -> funcionalidades necessárias para criar uma game)
import sys
import pygame
from pygame.sprite import Group

#importando as configurações
from settings import Settings #config
from ship import Ship #Imagem
import game_functions as gf #Importando função de eventos
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #incializa o jogo e criar um  objeto para a tela
    pygame.init() #inicializa as funções de segundo palano de que pygame precisa para funcionar de forma apropiada
    #criando uma janela de exibição chamada screen, na qual desenharemos todos os elementos gráficos do jogo. 
    #O argumento (1200, 800) é uma tupla que define as dimensões da janela do jogo
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    #cria um botao play
    play_button = Button(ai_settings, screen, "Play")
    #criar uma instancia para armazenar dados estatisticos
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #criar uma espaçonave
    ship = Ship(ai_settings, screen)
    #cria um personagem
    alien = Alien(ai_settings, screen)
    #cria um grupo no qual serão armazenados os projeteis
    bullets = Group()
    aliens = Group()
    #cria uma frota de aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
       #Inicia o laço principal doe jogo
    while True:
        """Observa os elementos do teclado e de mouse"""
       # for event in pygame.event.get(): #Qualquer eveno de teclado ou mouse fará o laço for executar.
         #    if event.type == pygame.QUIT:
        #        sys.exit
        #Refatoração chamando a função de fame functions
        gf.check_events(ai_settings, screen,stats, sb, play_button, ship, aliens, bullets)
        #stats.game_active:
        #posição será atualizada depois que verificarmos os enventos do teclados
        ship.update()       #Refatoração updates da telas
        #bullets.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)
        #print(len(bullets)) verificar se os projeteis estão sendo apagados
        gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen ,ship, aliens, bullets,stats, sb, play_button)
        #livra-se dos projeteis que desaparecem
        
        
    
    #Redesenha a tela a cada passagem pelo laço
        #screen.fill(ai_settings.bg_color)
        #ship.blitme()
        #Deixa a tela mais recente visível
        #pygame.display.flip()

#incializa o jogo e o laço principal
run_game()
