import sys

import pygame
from pygame.sprite import Sprite

class StarySky:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Stary Sky")

        self.stars = pygame.sprite.Group()

        self._create_grid()

        # Set background color
        self.bg_color = (0, 150, 225)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

    def _create_grid(self):
        """Create grid of stars."""
        # Create a star and find the number of stars in a row.
        # Spacing between each star is equal to the width of a star.
        star = Star(self)
        star_width, star_height = star.rect.size
        print(f"\nScreen size {self.screen_width}, {self.screen_height}\n")
        available_space_x = self.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Determin the number of rows of stars that fit on the screen.
        star_height = self.star.rect.height
        available_space_y = (self.screen_height - 
                                (3 * star_height) - star_height)
        number_rows = available_space_y // (2 * star_height)

        # Create the full fleet of stars.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create an star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


class Star(Sprite):
    """A class to represent a single star in the fleet."""

    def __init__(self, ai_game) -> None:
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Start each new star near the top of the left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact horizontal position.
        self.x = float(self.rect.x)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = StarySky()
    game.run_game()
