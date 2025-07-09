import pygame
import time
import os
import sys
from utils.constants import *
from screens.start_screen import show_start_screen
from screens.end_screen import show_end_screen
from game_objects.paddle import Paddle
from game_objects.ball import Ball
from utils.helper import draw_dotted_line, show_countdown

pygame.init()
pygame.mixer.init()

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

clock = pygame.time.Clock()

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

paddle_hit_sound = pygame.mixer.Sound(resource_path("sounds/paddle_hit_sound.wav"))
wall_hit_sound = pygame.mixer.Sound(resource_path("sounds/wall_hit_sound.wav"))

# Optional: Adjust volume if needed
paddle_hit_sound.set_volume(0.5)  
wall_hit_sound.set_volume(0.5)  

def main(game_mode=None):
    global left_score, right_score
    if not game_mode:
        game_mode = show_start_screen(screen)
        if not game_mode:
            pygame.quit()
            return
        
    show_countdown(screen)

    # Initialize paddles, ball, and scores
    left_paddle = Paddle(30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    right_paddle = Paddle(SCREEN_WIDTH - 40, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball()
    all_sprites = pygame.sprite.Group(left_paddle, right_paddle, ball)
    left_score = 0
    right_score = 0

    # Initialize single-player control paddle
    control_paddle = right_paddle if ball.speed_x > 0 else left_paddle

    start_time = time.time()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if game_mode == "one_player_keyboard":  # Single-player mode
            if keys[pygame.K_UP]:
                control_paddle.move_up()
            if keys[pygame.K_DOWN]:
                control_paddle.move_down()

        elif game_mode == "one_player_mouse":
            mouse_y = pygame.mouse.get_pos()[1]  #Get the mouse's vertical position
            control_paddle.move_to(mouse_y)  #Center the paddle around the mouse's Y position

        elif game_mode =="two_players":  # Two-player mode
            if keys[pygame.K_w]:
                left_paddle.move_up()
            if keys[pygame.K_s]:
                left_paddle.move_down()
            if keys[pygame.K_UP]:
                right_paddle.move_up()
            if keys[pygame.K_DOWN]:
                right_paddle.move_down()

        # Automatically switch control paddle based on ball direction in single-player modes
        if game_mode in ["one_player_keyboard", "one_player_mouse"]:
            if ball.speed_x > 0:
                control_paddle = right_paddle
            else:
                control_paddle = left_paddle

        # Ball movement
        ball.update(wall_hit_sound)
        if pygame.sprite.collide_rect(ball, left_paddle):
            ball.bounce(left_paddle, paddle_hit_sound)
        elif pygame.sprite.collide_rect(ball, right_paddle):
            ball.bounce(right_paddle, paddle_hit_sound)


        # Ball respawn and reset logic
        if ball.rect.left <= 0:
            right_score += 1
            ball.reset(1) 
            left_paddle.reset_speed()  
            right_paddle.reset_speed()  
        elif ball.rect.right >= SCREEN_WIDTH:
            left_score += 1
            ball.reset(-1) 
            left_paddle.reset_speed()
            right_paddle.reset_speed()  


        # Speed increment logic
        if time.time() - start_time > speed_increment_time:
            ball.increase_speed()
            left_paddle.increase_speed()
            right_paddle.increase_speed()
            start_time = time.time() 
        

        # Draw everything
        screen.fill(BLACK)
        draw_dotted_line(screen)
        all_sprites.draw(screen)
        font = pygame.font.Font(None, 74)
        left_text = font.render(str(left_score), True, WHITE)
        right_text = font.render(str(right_score), True, WHITE)
        screen.blit(left_text, (SCREEN_WIDTH // 4, 20))
        screen.blit(right_text, (SCREEN_WIDTH * 3 // 4, 20))
        pygame.display.flip()

        clock.tick(60)

        if left_score >= 5 or right_score >= 5:
            winner = "Left Player" if left_score > right_score else "Right Player"
            result = show_end_screen(screen, f"{winner} Wins!")
            
            if result == "play_again":
                main(game_mode)
            elif result == "home":
                main() 
            elif result == "exit":
                pygame.quit()
                return

if __name__ == "__main__":
    main()
