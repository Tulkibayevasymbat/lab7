import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up ball parameters
ball_radius = 25
ball_x, ball_y = width // 2, height // 2
ball_speed = 20

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - ball_speed, ball_radius)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + ball_speed, height - ball_radius)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - ball_speed, ball_radius)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + ball_speed, width - ball_radius)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()