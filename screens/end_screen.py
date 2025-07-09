import pygame
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, GREEN, RED, BLUE
from utils.helper import draw_button

def show_end_screen(screen, winner_text):
    font = pygame.font.Font(None, 74)

    while True:
        screen.fill(BLACK)

        title_text = font.render(winner_text, True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        play_again_button = draw_button(screen, "Play Again", GREEN, SCREEN_WIDTH // 4 - 75, SCREEN_HEIGHT // 2, 180, 55)
        home_button = draw_button(screen, "Home", BLUE, SCREEN_WIDTH // 2 + 75, SCREEN_HEIGHT // 2, 150, 55)
        exit_button = draw_button(screen, "Exit", RED, SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 100, 150, 55)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                    return "play_again"
                elif home_button.collidepoint(event.pos):
                    return "home"
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()
