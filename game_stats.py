#Armazena dados estatisticos da invasão

class GameStats():
    """Armazena dados estatísticos da invasão alienigena"""

    def __init__(self, ai_setings):
        """Inicializa os dados estatisticos"""
        self.ai_settings = ai_setings
        self.reset_stats()
        self.high_score = 0
        #Inicaliza o jogo num estado inativo
        self.game_active = False
    def reset_stats(self):
        """Inicializa os dados estatisticos que podem mudar durante o jogo"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        
