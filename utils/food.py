import pygame
import random

from config import *


class Food:

    def __init__(self):

        self.image = pygame.image.load(APPLE_IMAGE).convert_alpha()

        APPLE_SIZE = int(CELL_SIZE * 1.5)

        self.image = pygame.transform.scale(
            self.image,
            (APPLE_SIZE, APPLE_SIZE)
        )

        self.randomize()

    def randomize(self):

        self.position = (
            random.randint(0, COLS - 1),
            random.randint(0, ROWS - 1)
        )

    def draw(self, screen):

        APPLE_SIZE = int(CELL_SIZE * 1.5)

        x = self.position[0] * CELL_SIZE - (APPLE_SIZE - CELL_SIZE) // 2
        y = self.position[1] * CELL_SIZE - (APPLE_SIZE - CELL_SIZE) // 2

        screen.blit(self.image, (x, y))
