import pygame.font
from pygame.sprite import Group

from ship import Ship
from pathlib import Path

"""
Program Name: Coral Clash
Author: Haley White
Purpose: displays the score, high score, level, and remaining ships on screen
Starter Code: adapted from the starter repo (https://github.com/RedBeard41/alien_Invasion_starter.git)
              and Python Crash Course (https://learning.oreilly.com/library/view/python-crash-course/9781098156664/)
Date: July 2026
Asset attribution: HUD panel boxes (hud_score_box.png, hud_center_box.png, hud_lives_box.png) - "Paper UI Pack for Games" by loudeyes (https://loudeyes.itch.io/paper-ui-pack-for-games)
Asset attribution: Chewy font by Astigmatic, Google Fonts (https://fonts.google.com/specimen/Chewy)
"""

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (255, 131, 222)
        font_path = Path(__file__).parent / "assets" / "fonts" / "Chewy-Regular.ttf"
        self.font = pygame.font.Font(font_path, 24)

        images_path = Path(__file__).parent / "assets" / "images"
        self.score_box = pygame.transform.scale(
            pygame.image.load(images_path / "hud_score_box.png"), (140, 60))
        self.center_box = pygame.transform.scale(
            pygame.image.load(images_path / "hud_center_box.png"), (140, 60))
        self.lives_box = pygame.transform.scale(
            pygame.image.load(images_path / "hud_lives_box.png"), (200, 90))  # bigger
        self.level_box = pygame.transform.scale(
            pygame.image.load(images_path / "hud_score_box.png"), (140, 60))  # reused

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color)

        self.score_box_rect = self.score_box.get_rect()
        self.score_box_rect.right = self.screen_rect.right - 20
        self.score_box_rect.top = 20

        self.score_rect = self.score_image.get_rect()
        self.score_rect.center = self.score_box_rect.center

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        self.center_box_rect = self.center_box.get_rect()
        self.center_box_rect.centerx = self.screen_rect.centerx
        self.center_box_rect.top = 20

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.center = self.center_box_rect.center

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color)

        # Level box sits to the right, below the score box.
        self.level_box_rect = self.level_box.get_rect()
        self.level_box_rect.right = self.screen_rect.right - 20
        self.level_box_rect.top = self.score_box_rect.bottom + 10

        self.level_rect = self.level_image.get_rect()
        self.level_rect.center = self.level_box_rect.center

    def prep_ships(self):
        """Show how many ships are left."""
        self.lives_box_rect = self.lives_box.get_rect()
        self.lives_box_rect.left = 20
        self.lives_box_rect.top = 20

        ship_width, ship_height = 42, 31
        ship_gap = 6

        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.image = pygame.transform.scale(ship.image, (ship_width, ship_height))
            ship.rect = ship.image.get_rect()
            ship.rect.x = self.lives_box_rect.left + ship_number * (ship_width + ship_gap)
            ship.rect.y = self.lives_box_rect.centery - ship_height // 2
            self.ships.add(ship)

        # Center the whole row of ships inside the box.
        total_width = self.stats.ships_left * ship_width + (self.stats.ships_left - 1) * ship_gap
        start_x = self.lives_box_rect.centerx - total_width // 2
        for i, ship in enumerate(self.ships):
            ship.rect.x = start_x + i * (ship_width + ship_gap)
        
    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw the HUD panels, then the scores/level/ships on top of them."""
        self.screen.blit(self.score_box, self.score_box_rect)
        self.screen.blit(self.center_box, self.center_box_rect)
        self.screen.blit(self.lives_box, self.lives_box_rect)
        self.screen.blit(self.level_box, self.level_box_rect)

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)