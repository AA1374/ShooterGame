class GameStats:
    """Track statistics for alien invasion"""

    def __init__(self, ai_game):
        """Initaialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        #Start alien Invasion in an inactive state
        self.game_active = False

        #High score should be reset
        self.high_score = 0

    def reset_stats(self):
        """Initaialize statisticsthat can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        
