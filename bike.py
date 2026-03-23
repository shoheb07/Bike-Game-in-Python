import pygame
import random

# Initialize
pygame.init()

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bike Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GRAY = (50, 50, 50)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Bike
bike_width = 40
bike_height = 60
bike_x = WIDTH // 2 - bike_width // 2
bike_y = HEIGHT - bike_height - 10
bike_speed = 5

# Obstacles
obstacle_width = 40
obstacle_height = 60
obstacles = []
obstacle_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 30)

def draw_bike(x, y):
    pygame.draw.rect(screen, (0, 150, 255), (x, y, bike_width, bike_height))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, obstacle_width, obstacle_height))

def show_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over():
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, (WIDTH//2 - 80, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(2000)

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(GRAY)

    # Road lines
    for i in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, WHITE, (WIDTH//2 - 5, i, 10, 20))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bike_x > 0:
        bike_x -= bike_speed
    if keys[pygame.K_RIGHT] and bike_x < WIDTH - bike_width:
        bike_x += bike_speed

    # Spawn obstacles
    if random.randint(1, 30) == 1:
        x = random.randint(0, WIDTH - obstacle_width)
        obstacles.append([x, -obstacle_height])

    # Move obstacles
    for obs in obstacles:
        obs[1] += obstacle_speed

    # Collision
    for obs in obstacles:
        if (bike_x < obs[0] + obstacle_width and
            bike_x + bike_width > obs[0] and
            bike_y < obs[1] + obstacle_height and
            bike_y + bike_height > obs[1]):
            game_over()
            running = False

    # Remove passed obstacles
    obstacles = [obs for obs in obstacles if obs[1] < HEIGHT]

    # Draw obstacles
    for obs in obstacles:
        draw_obstacle(obs[0], obs[1])

    # Draw bike
    draw_bike(bike_x, bike_y)

    # Score update
    score += 1
    show_score()

    pygame.display.update()

pygame.quit()
