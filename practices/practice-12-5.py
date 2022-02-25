import sys

import pygame

class Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("My Game")

        # Set the background color.
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
            if event.type == pygame.KEYDOWN:
                print(event)

    def _update_screen(self):
        """Redraw the screen and flip to update."""
        self.screen.fill(self.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
