import pygame
import random
import sys

pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Snake starting position
snake = [(300, 200), (280, 200), (260, 200)]
direction = (CELL_SIZE, 0)

# Food position
food = (
    random.randrange(0, WIDTH, CELL_SIZE),
    random.randrange(0, HEIGHT, CELL_SIZE)
)

score = 0

font = pygame.font.SysFont(None, 30)


def draw_snake():
    for x, y in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (x, y, CELL_SIZE, CELL_SIZE)
        )


def draw_food():
    pygame.draw.rect(
        screen,
        RED,
        (food[0], food[1], CELL_SIZE, CELL_SIZE)
    )


def game_over():
    screen.fill(BLACK)

    message = font.render(
        "Game Over! Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(
        message,
        (WIDTH // 2 - 120, HEIGHT // 2)
    )

    pygame.display.update()
    pygame.time.wait(2000)


# Main game loop
while True:

    # Handle keyboard events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)

            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)

            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)

            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    # Move snake
    head_x, head_y = snake[0]

    new_head = (
        head_x + direction[0],
        head_y + direction[1]
    )

    # Check wall collision
    if (
        new_head[0] < 0
        or new_head[0] >= WIDTH
        or new_head[1] < 0
        or new_head[1] >= HEIGHT
    ):
        game_over()
        break

    # Check self collision
    if new_head in snake:
        game_over()
        break

    snake.insert(0, new_head)

    # Check food collision
    if new_head == food:
        score += 1

        while True:
            food = (
                random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE)
            )

            if food not in snake:
                break
    else:
        snake.pop()

    # Draw everything
    screen.fill(BLACK)

    draw_snake()
    draw_food()

    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(score_text, (10, 10))

    pygame.display.update()

    clock.tick(10)

pygame.quit()
