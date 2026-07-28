"""
Program Name: Coral Clash
Author: Haley White
Purpose: tracks game stats like score, level, and how many ships are left
Starter Code: adapted from the starter repo (https://github.com/RedBeard41/alien_Invasion_starter.git)
              and Python Crash Course (https://learning.oreilly.com/library/view/python-crash-course/9781098156664/)
Date: July 2026
"""

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1