import pygame.font
from pathlib import Path


"""
Program Name: Coral Clash
Author: Haley White
Purpose: handles the play button so the player can start the game
Starter Code: adapted from the starter repo (https://github.com/RedBeard41/alien_Invasion_starter.git)
              and Python Crash Course (https://learning.oreilly.com/library/view/python-crash-course/9781098156664/)
Date: July 2026
"""

class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Load the custom play button image.
        image_path = Path(__file__).parent / "assets" / "images" / "play_button.png"
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        
        self.text_color = (255, 255, 255)
        font_path = Path(__file__).parent / "assets" / "fonts" / "Chewy-Regular.ttf"
        self.font = pygame.font.Font(font_path, 72)

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)