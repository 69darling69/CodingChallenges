import random

import pygame
import math
from Ball import Ball

pygame.init()
pygame.display.set_caption("Mandelbrot set")

FPS = 2
WIDTH, HEIGHT = 400, 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

balls_count = 15
balls = [Ball(WIDTH, HEIGHT, random.randrange(20)) for _ in range(balls_count)]

running = True
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for ball in balls:
        ball.update()
        # ball.draw(screen)

    # Draw
    for i in range(WIDTH):
        for j in range(HEIGHT):
            s = 0
            for ball in balls:
                s += 100 * ball.r / ball.distance((i, j))
            if s < 0:
                s = 0
            if s > 255:
                s = 255
            screen.set_at((i, j), (s, s, s))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
