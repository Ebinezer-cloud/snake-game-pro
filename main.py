import pygame
import sys
import os

from config import *
from utils.snake import Snake
from utils.food import Food
from utils.scoreboard import ScoreBoard

pygame.init()
pygame.mixer.init()

# ----------------------------
# Window
# ----------------------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# ----------------------------
# Icon
# ----------------------------
if os.path.exists(ICON_IMAGE):
    icon = pygame.image.load(ICON_IMAGE)
    pygame.display.set_icon(icon)

# ----------------------------
# Background
# ----------------------------
background = None

if os.path.exists(BACKGROUND_IMAGE):
    background = pygame.image.load(BACKGROUND_IMAGE)
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# ----------------------------
# Sounds
# ----------------------------
eat_sound = None
gameover_sound = None

if os.path.exists(EAT_SOUND):
    eat_sound = pygame.mixer.Sound(EAT_SOUND)

if os.path.exists(GAMEOVER_SOUND):
    gameover_sound = pygame.mixer.Sound(GAMEOVER_SOUND)

if os.path.exists(BG_MUSIC):
    pygame.mixer.music.load(BG_MUSIC)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and snake.direction != (0, 1):
                snake.direction = (0, -1)

            elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                snake.direction = (0, 1)

            elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                snake.direction = (-1, 0)

            elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                snake.direction = (1, 0)

    alive = snake.move()
       # ----------------------------
    # Game Over
    # ----------------------------
    if not alive:

        if gameover_sound:
            gameover_sound.play()

        font_big = pygame.font.SysFont("Arial", 60, True)
        font_small = pygame.font.SysFont("Arial", 30)

        waiting = True

        while waiting:

            if background:
                screen.blit(background, (0, 0))
            else:
                screen.fill((20, 20, 30))

            title = font_big.render("GAME OVER", True, (255, 0, 0))
            message = font_small.render(
                "Press R to Restart | ESC to Exit",
                True,
                (255, 255, 255)
            )

            screen.blit(
                title,
                (
                    WIDTH // 2 - title.get_width() // 2,
                    HEIGHT // 2 - 60,
                ),
            )

            screen.blit(
                message,
                (
                    WIDTH // 2 - message.get_width() // 2,
                    HEIGHT // 2 + 20,
                ),
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_r:

                        snake.reset()
                        scoreboard.score = 0
                        food.randomize()

                        waiting = False

                    elif event.key == pygame.K_ESCAPE:

                        pygame.quit()
                        sys.exit()

    # ----------------------------
    # Food Collision
    # ----------------------------
    if snake.body[0] == food.position:

        if eat_sound:
            eat_sound.play()

        snake.grow = True
        food.randomize()
        scoreboard.score += 10

    # ----------------------------
    # Draw Background
    # ----------------------------
    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill((20, 20, 30))

    # ----------------------------
    # Draw Objects
    # ----------------------------
    snake.draw(screen)
    food.draw(screen)
    scoreboard.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()