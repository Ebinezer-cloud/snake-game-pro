import pygame


def draw_text(screen, text, font, color, x, y):

    render = font.render(text, True, color)

    screen.blit(render, (x, y))