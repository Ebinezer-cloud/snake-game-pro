import pygame
import random

from config import *


class Food:

    def __init__(self):

        self.image = pygame.image.load(APPLE_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (CELL_SIZE, CELL_SIZE)
        )

        self.randomize()

    def randomize(self):

        self.position = (
            random.randint(0, COLS - 1),
            random.randint(0, ROWS - 1)
        )

    def draw(self, screen):

        x = self.position[0] * CELL_SIZE
        y = self.position[1] * CELL_SIZE

        screen.blit(self.image, (x, y))