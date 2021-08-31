import random

import pygame
from Star import Star


pygame.init()
pygame.display.set_caption("Starfield")

FPS = 60
RES = 800

screen = pygame.display.set_mode((RES, RES))
clock = pygame.time.Clock()

stars = []

running = True
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    if random.randrange(101) >= 75:
        stars.append(Star(RES, RES, (RES // 2, RES // 2)))

    for star in stars:
        if star.away():
            stars.remove(star)
            continue
        star.update()

    # Draw
    screen.fill((0, 0, 0))
    for star in stars:
        star.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
