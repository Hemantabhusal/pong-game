import pygame
from utils.constants import WHITE, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT

def draw_dotted_line(screen):
    center_x = SCREEN_WIDTH // 2
    for y in range(0, SCREEN_HEIGHT, 35):
        pygame.draw.line(screen, WHITE, (center_x, y), (center_x, y + 15), 4)

def draw_button(screen, text, color, x, y, width, height, text_color=(0, 0, 0), border_color=(0, 0, 0), font=None, border_radius=18):
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=border_radius)

    if border_color:
        pygame.draw.rect(screen, border_color, (x, y, width, height), 2, border_radius=border_radius)

    if not font: 
        font = pygame.font.Font(None, 50)
    button_text = font.render(text, True, text_color)
    text_rect = button_text.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(button_text, text_rect)

    return pygame.Rect(x, y, width, height)


def show_countdown(screen):
    font = pygame.font.Font(None, 100)
    for count in range(0, 0, -1):
        screen.fill(BLACK)
        countdown_text = font.render(str(count), True, WHITE)
        countdown_rect = countdown_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(countdown_text, countdown_rect)
        pygame.display.flip()
        pygame.time.wait(1000)

    screen.fill(BLACK)
    go_text = font.render("GO!", True, WHITE)
    go_rect = go_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(go_text, go_rect)
    pygame.display.flip()
    pygame.time.wait(1000)

