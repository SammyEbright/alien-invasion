import sys

import pygame
from pygame.sprite import Sprite

class Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()

        # self.screen = pygame.display.set_mode((1200, 800))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rocket Game")

        self.shooter = Shooter(self)
        
        self.bullet = Bullet(self)
        self.bullets = pygame.sprite.Group()
        self.bullets_allowed = self.bullet.allowed

        # Set the background color.
        self.bg_color = (0, 150, 225)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.shooter.update()
            self._update_bullet()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.shooter.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.shooter.moving_left = True
        elif event.key == pygame.K_UP:
            self.shooter.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.shooter.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.shooter.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.shooter.moving_left = False
        elif event.key == pygame.K_UP:
            self.shooter.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.shooter.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        """Update the position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_width:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self.shooter.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


class Shooter:
    """A class to manage the shooter."""
    
    def __init__(self, my_game) -> None:
        """Initialize the shooter and set its starting position."""
        self.screen = my_game.screen
        self.screen_rect = my_game.screen.get_rect()

        # Load the shooter image and get its rect.
        self.image = pygame.image.load('images/shooter.bmp')
        self.rect = self.image.get_rect()

        # Start each new shooter at the center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Rocket speed
        self.shooter_speed = 1.5

        # Store a decimal value for the shooter's positions.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the shooter's position based on the movement flag."""
        # Update the shooter's x and y values not the rect:
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.x += self.shooter_speed
            pass
        if self.moving_left and self.rect.left > 0:
            # self.x -= self.shooter_speed
            pass
        if self.moving_up and self.rect.top > 0:
            self.y -= self.shooter_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.shooter_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the shooter at its current location."""
        self.screen.blit(self.image, self.rect)


class Bullet(Sprite):
    """A class to manage bullets fired from the shooter"""

    def __init__(self, ai_game):
        """Create a bullet object at the shooter's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.color = (100, 0, 0)
        self.speed = 1.0
        self.width = 7.5
        self.height = 3
        self.allowed = 3

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, 
            self.width, 
            self.height)
        self.rect.midright = ai_game.shooter.rect.midright

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen."""
        # Update the decimal position of the bullet.
        self.x += self.speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
