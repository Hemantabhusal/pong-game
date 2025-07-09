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
        self.rect.y = y - PADDLE_HEIGHT // 2
        if self.rect.y < 0:
            self.rect.y = 0 
        if self.rect.y > SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - PADDLE_HEIGHT  


    def reset_speed(self):
        self.speed = initial_paddle_speed


    def increase_speed(self):
        self.speed += speed_increment
