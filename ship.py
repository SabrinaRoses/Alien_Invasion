#modulo para usar a espaço nave do jogador

import pygame 
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings,screen):
        """Inicializa a espaço nave e define sua posição inicial"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('imagens/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #inicia a cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Armazena um valor decimmal para o centro da espaçonave
        self.center = float(self.rect.centerx) # O atributos de rentangulo como centerx, armazenm apenas valores inteiros, por isso a conversão

        #flag movimento
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Atualiza a posiçao da espaçonave de acordo com a flag de movimento"""
        #atualiza o valor central da espaçonave, e não o retangulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            #atualiza o objeto rect de acordo com o self center
        self.rect.centerx = self.center

    def blitme(self):
        """Desenha a espaçonave em sua posição atual"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Centraliza a espaçonave na tela"""
        self.center = self.screen_rect.centerx
    