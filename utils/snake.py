import pygame
from config import *

class Snake:

    def __init__(self):
        self.reset()

        self.head = pygame.image.load(SNAKE_HEAD_IMAGE).convert_alpha()
        self.body_img = pygame.image.load(SNAKE_BODY_IMAGE).convert_alpha()

        self.head = pygame.transform.scale(
            self.head,
            (CELL_SIZE, CELL_SIZE)
        )

        self.body_img = pygame.transform.scale(
            self.body_img,
            (CELL_SIZE, CELL_SIZE)
        )

    def reset(self):
        self.body = [(10, 10), (9, 10), (8, 10)]
        self.direction = (1, 0)
        self.grow = False

    def move(self):

        x, y = self.body[0]
        dx, dy = self.direction

        new_head = (x + dx, y + dy)

        # Wall Collision
        if (
            new_head[0] < 0 or
            new_head[0] >= COLS or
            new_head[1] < 0 or
            new_head[1] >= ROWS
        ):
            return False

        # Self Collision
        if new_head in self.body:
            return False

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

        return True

    def draw(self, screen):

        for i, segment in enumerate(self.body):

            x = segment[0] * CELL_SIZE
            y = segment[1] * CELL_SIZE

            if i == 0:

                image = self.head

                if self.direction == (1, 0):
                    image = self.head

                elif self.direction == (-1, 0):
                    image = pygame.transform.rotate(self.head, 180)

                elif self.direction == (0, -1):
                    image = pygame.transform.rotate(self.head, 90)

                elif self.direction == (0, 1):
                    image = pygame.transform.rotate(self.head, -90)

                screen.blit(image, (x, y))

            else:
                screen.blit(self.body_img, (x, y))