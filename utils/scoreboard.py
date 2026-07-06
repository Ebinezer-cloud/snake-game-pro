import pygame
import os

from config import *


class ScoreBoard:

    def __init__(self):

        self.score = 0
        self.high_score = 0

        self.font = pygame.font.SysFont("Arial", 28, bold=True)

        self.file = "highscore.txt"

        if os.path.exists(self.file):
            try:
                with open(self.file, "r") as f:
                    self.high_score = int(f.read())
            except:
                self.high_score = 0

    def update_high_score(self):

        if self.score > self.high_score:

            self.high_score = self.score

            with open(self.file, "w") as f:
                f.write(str(self.high_score))

    def draw(self, screen):

        self.update_high_score()

        score_text = self.font.render(
            f"Score : {self.score}",
            True,
            WHITE
        )

        high_text = self.font.render(
            f"High Score : {self.high_score}",
            True,
            YELLOW
        )

        screen.blit(score_text, (15, 10))
        screen.blit(high_text, (15, 45))