from calendar import c
from cmath import rect
from sys import float_repr_style
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota"""
    
    def __init__(self, ai_settings, screen):
        """"Inicializa o alien e define sua posição inicial"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

    #carrega a imagem do alien e define seu atributo rect
        self.image = pygame.image.load('imagens/ufo.bmp')
        self.rect = self.image.get_rect()
    
    #Inicia cada novo alien próximo a parte superior da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    #Armazena a posição exata do alien
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Desenha o alien em sua posição atual"""
        self.screen.blit(self.image, self.rect)
    
  
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        """Move o alien para a direita ou para esquerda"""
        #Sempre que atualizarmos a posição de um alien ele será movido para direita com o valor armazendo em alien_speed...
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x