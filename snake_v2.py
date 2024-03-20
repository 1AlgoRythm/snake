import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Define colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)  # Color for the food
white = (255, 255, 255)  # Color for text

# Font for displaying text
font = pygame.font.SysFont(None, 48)

def show_game_over_screen():
    game_over_surface = font.render('Game Over!', True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width / 2, screen_height / 4)

    play_again_surface = font.render('Play Again', True, white)
    play_again_rect = play_again_surface.get_rect()
    play_again_rect.midtop = (screen_width / 2, screen_height / 2)

    quit_surface = font.render('Quit', True, white)
    quit_rect = quit_surface.get_rect()
    quit_rect.midtop = (screen_width / 2, screen_height / 1.5)

    screen.fill(black)
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(play_again_surface, play_again_rect)
    screen.blit(quit_surface, quit_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_RETURN:
                    return True  # Play again
                if event.key == pygame.K_DOWN or event.key == pygame.K_ESCAPE:
                    return False  # Quit game

# Game initialization
def game_loop():
    # Snake properties
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    snake_color = green
    direction = 'RIGHT'
    change_to = direction

    # Food properties
    food_pos = [random.randrange(1, (screen_width // 10)) * 10, random.randrange(1, (screen_height // 10)) * 10]
    food_spawn = True
    food_color = red

    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        # Update the direction of the snake
        direction = change_to

        # Update the snake's position
        if direction == 'UP':
            snake_pos[1] -= 10
        elif direction == 'DOWN':
            snake_pos[1] += 10
        elif direction == 'LEFT':
            snake_pos[0] -= 10
        elif direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake passing through walls
        snake_pos[0] = snake_pos[0] % screen_width
        snake_pos[1] = snake_pos[1] % screen_height

        # Snake body mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            food_spawn = False
        else:
            snake_body.pop()

        # Food spawn
        if not food_spawn:
            food_pos = [random.randrange(1, (screen_width // 10)) * 10, random.randrange(1, (screen_height // 10)) * 10]
        food_spawn = True

                # Graphics
        screen.fill(black)
        for pos in snake_body:
            pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        
        # Updating the display
        pygame.display.flip()

        # Snake collision with itself
        for block in snake_body[1:]:
            if snake_pos == block:
                running = False
                break

        # Frame rate control
        pygame.time.Clock().tick(10)

    # Show the game over screen and wait for player's action
    return show_game_over_screen()

# Main game function
def main():
    while True:
        if game_loop():
            continue  # Restart the game
        else:
            break  # Exit the game

main()

