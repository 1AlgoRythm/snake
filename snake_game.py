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

# Snake properties
snake_pos = [100, 50]  # Starting position of the snake head
snake_body = [[100, 50], [90, 50], [80, 50]]  # Initial snake body segments (head and two more segments)
snake_color = green
dx, dy = 10, 0  # dx, dy represents the change in x, y direction

food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
food_spawn = True
food_color = (255, 0, 0)  # Red color for the food

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dx, dy = 0, -10
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, 10
            elif event.key == pygame.K_LEFT:
                dx, dy = -10, 0
            elif event.key == pygame.K_RIGHT:
                dx, dy = 10, 0

    # Update the snake's position
    snake_pos[0] += dx
    snake_pos[1] += dy
    snake_body.insert(0, list(snake_pos))  # Add a new segment at the front for the head
    snake_body.pop()  # Remove the last segment of the snake

    # Drawing everything
    screen.fill(black)

    if snake_pos == food_pos:
        food_spawn = False
        snake_body.insert(-1, list(snake_pos))  # Add a new segment to the snake to make it longer
    else:
        food_spawn = True
    #respawning food
    if not food_spawn:
        food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
    food_spawn = True

    #food spawning
    if food_spawn:
        pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    #collision handing
    if snake_pos[0] < 0 or snake_pos[0] > screen_width-10:
        running = False
    
    #self collision 
    for block in snake_body[1:]:
        if snake_pos == block:
            running = False
            break


    for pos in snake_body:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))

    # Updating the display
    pygame.display.flip()

    # Frame rate control
    pygame.time.Clock().tick(10)  # This will make the loop run at 10 frames per second

# Clean up
pygame.quit()
sys.exit()
