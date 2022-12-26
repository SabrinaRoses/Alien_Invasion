import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """Uma classe para mostrar informações sobre pontuação"""

    def __init__(self, ai_settings, screen, stats):
        """Inicializa os atributos da pontuação"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #configurando uma fonte para as informações de pontuação
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        #Prepara a imagem da pontuação inicial
        self.prep_score()
        #Prepara imagem pontuação máxima
        self.prep_high_score()
        #prepara as imagens das pontuações iniciais
        self.prep_level()
        #Cria um grupo vazio para armazenar espaçonaves
        self.prep_ships()
        
    def prep_score(self):
        """Transforma a pontuação em uma imagem renderizada"""
        rounded_score = int(round(self.stats.score, -1)) #Arredonda a pontuação para o número mais proximo de 10
        score_str = "{:,}".format(rounded_score) #insere virgulas nos números ao converter para string
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #Exibe a pontuação na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        """Desenha a pontuação na tela"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        #Desenha a espaçonave
        self.ships.draw(self.screen)
    
    def prep_high_score(self):
        """Transforma a pontuação máxima numa imagem renderizada"""
        high_score = int(round(self.stats.high_score, -1)) #arrendonando e formatando com virgulas
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        #centralizamos seu rect horizontelmente 
        #self.high_score_rect.centerx = self.score_rect.centerx 
        #x e definimos seu atributo top para que seja igual a parte superior da pontuação
        #self.high_score_rect.top = self.score_rect.top

        #Centraliza a pontuação maxima na parte supeior da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Transforma o nivel em uma imagem renderizada"""
        self.level_image = self.font.render(str(self.stats.level), True, self.ai_settings.text_color)
        
        #Posiciona o nível abaixo da pontuação
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        #10 pixels abaixo
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        """Mostra quantas espaçonaves restam"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

        