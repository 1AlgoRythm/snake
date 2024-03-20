# Snake Game Implementation with emphasis on Data Structures and Algorithms (DSA) concepts

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

# Snake properties
snake_pos = [100, 50]  # Starting position of the snake head - DSA: Variable
snake_body = [[100, 50], [90, 50], [80, 50]]  # Initial snake body segments (head and two more segments) - DSA: List
snake_color = green
dx, dy = 10, 0  # dx, dy represents the change in x, y direction - DSA: Tuple (immutable)

# Food properties
food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]  # Random position - DSA: Array
food_spawn = True
food_color = red

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
    snake_body.insert(0, list(snake_pos))  # Insert new position at the front of the list - DSA: Queue/Deque operation
    if snake_pos == food_pos:  # Check for collision with food - DSA: Collision detection
        food_spawn = False  # Prevents immediate respawning of food; snake grows
    else:
        snake_body.pop()  # Remove the last segment of the snake if no food has been eaten - DSA: List operation

    # Respawn food if needed
    if not food_spawn:
        food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
    food_spawn = True

    # Drawing everything
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))  # Drawing the snake - DSA: Iterating through List
    pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))  # Drawing the food - DSA: Direct access (Array/Indexing)

    # Check for collisions with the wall
    if snake_pos[0] < 0 or snake_pos[0] >= screen_width or snake_pos[1] < 0 or snake_pos[1] >= screen_height:
        running = False  # End game if snake hits the boundaries

    # Check for self collision (if the snake runs into itself)
    for block in snake_body[1:]:
        if snake_pos == block:  # DSA: Collision detection within a List
            running = False
            break

    # Updating the display
    pygame.display.flip()

    # Frame rate control
    pygame.time.Clock().tick(10)  # Controls the speed of the game - DSA: Timing and Control

# Clean up
pygame.quit()
sys.exit()
