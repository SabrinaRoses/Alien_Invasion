from zoneinfo import available_timezones


class Settings():
    """"Uma classe para armazenar todas as configurações da invasão alienigena"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
         #configuração da espaçonave
         #Quando quisermos mover a espaçonva ajustaremos sua posição em 1,5 pixel.
        #self.ship_speed_factor = 1.5
        self.ship_limit = 3 #O numero de naves
        #configurando os projéteis
        #self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        #numeros de projeteis permitidos
        self.bullets_allowed = 10 #limita o jogador a três projeteis ao mesmo tempo
        #configurações do alien
        #self.alien_speed_factor = 3
        self.fleet_drop_speed = 1
        #fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        #self.fleet_direction = 1
        #A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.2
        #self.fleet_drop_speed = 1.1???
        #A taxa com que os pontos para cada alien aumentam
        self.score_scale = 1.5
        self.initialize_dynamic_settings() #inicializa os valores dos atributos que devem mudar no curso do jogo
        #cor ponints
        self.text_color = (255, 0, 0)

    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam ao decorrer do jogo"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        #fleet_direction igual a 1 representa a direita, -1 representa a esquerda
        self.fleet_direction = 1
        #Pontuação
        self.alien_points = 50
    
    def increase_speed(self):
        """Aumenta as configurações de velocidade"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)
        #ver quantas quamtos pontos valem cada alien
        #print(self.alien_points)

       
