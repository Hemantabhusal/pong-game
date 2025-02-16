import pygame
from utils.constants import WHITE, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT

def draw_dotted_line(screen):
    """
    Draws a vertical dotted line in the center of the screen.
    """
    center_x = SCREEN_WIDTH // 2
    for y in range(0, SCREEN_HEIGHT, 35):
        pygame.draw.line(screen, WHITE, (center_x, y), (center_x, y + 15), 4)

def draw_button(screen, text, color, x, y, width, height, text_color=(0, 0, 0), border_color=(0, 0, 0), font=None, border_radius=18):
    """
    Draws a button with customizable font, colors, and border radius (for rounded corners).

    Parameters:
        - screen: Pygame display surface.
        - text: Text displayed on the button.
        - color: Background color of the button.
        - x, y: Top-left corner of the button.
        - width, height: Size of the button.
        - text_color: Color of the text (default black).
        - border_color: Color of the button border (default white).
        - font: Pygame font object to use for the button text.
        - border_radius: Radius for rounded corners (default 0 = square corners).

    Returns:
        - A Pygame Rect object for the button.
    """
    # Draw the button rectangle (background)
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=border_radius)
    
    # Draw the border around the button
    if border_color:
        pygame.draw.rect(screen, border_color, (x, y, width, height), 2, border_radius=border_radius)

    # Render the text
    if not font:  # Use default font if none provided
        font = pygame.font.Font(None, 50)
    button_text = font.render(text, True, text_color)
    text_rect = button_text.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(button_text, text_rect)

    return pygame.Rect(x, y, width, height)


def show_countdown(screen):
    """
    Displays a 2-second countdown before the game starts.
    """
    font = pygame.font.Font(None, 100)
    for count in range(0, 0, -1):  # Countdown from 3 to 1
        screen.fill(BLACK)
        countdown_text = font.render(str(count), True, WHITE)
        countdown_rect = countdown_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(countdown_text, countdown_rect)
        pygame.display.flip()
        pygame.time.wait(1000)  # Wait for 1 second

    # Display "GO" before starting
    screen.fill(BLACK)
    go_text = font.render("GO!", True, WHITE)
    go_rect = go_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(go_text, go_rect)
    pygame.display.flip()
    pygame.time.wait(1000)  # Wait for 1 second

