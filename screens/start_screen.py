import pygame
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, BLUE, GREEN
from utils.helper import draw_button

def show_start_screen(screen):
    font = pygame.font.Font(None, 74)

    # Main loop for start screen
    while True:
        screen.fill(BLACK)
        title_text = font.render("Select Game Mode", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        single_player_button = draw_button(screen, "One Player", BLUE, SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 50, 216, 55)
        two_player_button = draw_button(screen, "Two Players", GREEN, SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 50, 216, 55)

        pygame.display.flip()

        # Event loop for selecting game mode
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if single_player_button.collidepoint(event.pos):
                    return show_control_selection(screen)
                elif two_player_button.collidepoint(event.pos):
                    return "two_players"

def show_control_selection(screen):
    font = pygame.font.Font(None, 74)

    while True:
        screen.fill(BLACK)
        title_text = font.render("Choose Control", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)

        keyboard_button = draw_button(screen, "Keyboard", BLUE, SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 50, 200, 50)
        mouse_button = draw_button(screen, "Mouse", GREEN, SCREEN_WIDTH // 2 + 50, SCREEN_HEIGHT // 2 - 50, 200, 50)

        pygame.display.flip()

        # Event loop for selecting control type
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if keyboard_button.collidepoint(event.pos):
                    return "one_player_keyboard"
                elif mouse_button.collidepoint(event.pos):
                    return "one_player_mouse"
