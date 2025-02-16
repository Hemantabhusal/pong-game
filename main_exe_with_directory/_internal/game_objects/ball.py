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

        # Bounce off top and bottom
        if self.rect.top <= 0:  # Top boundary
            self.rect.top = 0  # Keep ball within bounds
            self.speed_y = -self.speed_y  # Reverse vertical direction
            wall_hit_sound.play()  # Play wall hit sound
        elif self.rect.bottom >= SCREEN_HEIGHT:  # Bottom boundary
            self.rect.bottom = SCREEN_HEIGHT  # Keep ball within bounds
            self.speed_y = -self.speed_y  # Reverse vertical direction
            wall_hit_sound.play()  # Play wall hit sound

    def bounce(self, paddle, paddle_hit_sound):
        """
        Handles the ball's bounce logic when it collides with a paddle.
        Adjusts horizontal and vertical speed based on collision position.
        """
        # Reverse horizontal direction
        self.speed_x = -self.speed_x
        paddle_hit_sound.play()

        # Adjust vertical speed based on where the ball hits the paddle
        paddle_center = paddle.rect.centery
        ball_center = self.rect.centery
        distance_from_center = ball_center - paddle_center

        # Normalize the impact position (distance) and apply a vertical speed adjustment
        max_distance = paddle.rect.height // 2
        normalized_distance = distance_from_center / max_distance  # Range: -1 to 1
        self.speed_y += normalized_distance * initial_ball_speed * 0.5  # Adjust vertical speed

        # Ensure the ball doesn't overlap the paddle
        if self.speed_x > 0:  # Ball is moving to the right
            self.rect.left = paddle.rect.right
        else:  # Ball is moving to the left
            self.rect.right = paddle.rect.left


    def reset(self, direction):
        """
        Resets the ball's position to a random vertical position near the center 
        of the screen and randomizes its vertical speed.
        The horizontal speed is determined by the direction.
        """
        # Center the ball horizontally, randomize vertically within a range
        self.rect.center = (
            SCREEN_WIDTH // 2,  # Horizontal center
            random.randint(SCREEN_HEIGHT // 3, SCREEN_HEIGHT * 3 // 3)  # Vertical position (25% to 75% of screen height)
        )

        # Set horizontal speed based on direction
        self.speed_x = direction * initial_ball_speed

        # Randomize vertical speed with some variability
        self.speed_y = random.uniform(-initial_ball_speed, initial_ball_speed)

        # Ensure vertical speed is not too low (to avoid a nearly horizontal ball movement)
        if abs(self.speed_y) < initial_ball_speed * 0.3:  # 30% of initial speed
            self.speed_y = initial_ball_speed * 0.3 * (-1 if self.speed_y < 0 else 1)



    def increase_speed(self):
        """
        Increases the speed of the ball by speed_increment.
        """
        self.speed_x += speed_increment if self.speed_x > 0 else -speed_increment
        self.speed_y += speed_increment if self.speed_y > 0 else -speed_increment