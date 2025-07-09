import pygame
import random
from utils.constants import WHITE, BALL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, initial_ball_speed, speed_increment

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = BALL_SIZE // 2
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x = random.choice([-initial_ball_speed, initial_ball_speed])
        self.speed_y = random.choice([-initial_ball_speed, initial_ball_speed])

    def update(self, wall_hit_sound):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0:  
            self.rect.top = 0  
            self.speed_y = -self.speed_y 
            wall_hit_sound.play() 
        elif self.rect.bottom >= SCREEN_HEIGHT: 
            self.rect.bottom = SCREEN_HEIGHT 
            self.speed_y = -self.speed_y  
            wall_hit_sound.play()  

    def bounce(self, paddle, paddle_hit_sound):
        self.speed_x = -self.speed_x
        paddle_hit_sound.play()

        paddle_center = paddle.rect.centery
        ball_center = self.rect.centery
        distance_from_center = ball_center - paddle_center

        max_distance = paddle.rect.height // 2
        normalized_distance = distance_from_center / max_distance
        self.speed_y += normalized_distance * initial_ball_speed * 0.5 

        if self.speed_x > 0:  
            self.rect.left = paddle.rect.right
        else:
            self.rect.right = paddle.rect.left


    def reset(self, direction):

        self.rect.center = (
            SCREEN_WIDTH // 2,
            random.randint(SCREEN_HEIGHT // 3, SCREEN_HEIGHT * 3 // 3)
        )

        self.speed_x = direction * initial_ball_speed

        self.speed_y = random.uniform(-initial_ball_speed, initial_ball_speed)

        if abs(self.speed_y) < initial_ball_speed * 0.3: 
            self.speed_y = initial_ball_speed * 0.3 * (-1 if self.speed_y < 0 else 1)



    def increase_speed(self):
        """
        Increases the speed of the ball by speed_increment.
        """
        self.speed_x += speed_increment if self.speed_x > 0 else -speed_increment
        self.speed_y += speed_increment if self.speed_y > 0 else -speed_increment