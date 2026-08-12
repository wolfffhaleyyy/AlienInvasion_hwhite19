import pygame
from pygame.sprite import Sprite
from pathlib import Path

"""
Program Name: Coral Clash
Author: Haley White
Purpose: handles the laser fired from the submarine - creating it, moving it, and drawing it
Starter Code: adapted from the starter repo (https://github.com/RedBeard41/alien_Invasion_starter.git)
              and Python Crash Course (https://learning.oreilly.com/library/view/python-crash-course/9781098156664/)
Date: July 2026
Asset attribution: coral-bullet sprite - CraftPix free assets (https://craftpix.net/), see license at https://craftpix.net/file-licenses/
"""

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the bullet image and set its rect attribute.
        image_path = Path(__file__).parent / "assets" / "images" / "coral-bullet.png"
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (10, 15)) 
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)