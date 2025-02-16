import pygame
from utils.constants import WHITE, PADDLE_WIDTH, PADDLE_HEIGHT, SCREEN_HEIGHT, initial_paddle_speed, speed_increment

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = initial_paddle_speed

    def move_up(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - PADDLE_HEIGHT

    def move_to(self, y):
        """
    Moves the paddle to the given vertical position (Y-coordinate).
    Ensures the paddle stays within the screen bounds.
    """
        self.rect.y = y - PADDLE_HEIGHT // 2  # Center paddle on the given Y-coordinate
        if self.rect.y < 0:
            self.rect.y = 0  # Prevent moving above the screen
        if self.rect.y > SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - PADDLE_HEIGHT  # Prevent moving below the screen


    def reset_speed(self):
        """
        Resets the paddle's speed to its initial value.
        """
        self.speed = initial_paddle_speed


    def increase_speed(self):
        """
        Increases the paddle's speed by speed_increment.
        """
        self.speed += speed_increment
