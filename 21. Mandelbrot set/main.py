import math

import pygame


def interpolate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)


pygame.init()
pygame.display.set_caption("Mandelbrot set")

FPS = 60
WIDTH, HEIGHT = 800, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

maxiterations = 100
scale = 1
offset = (-0.5, 0)

# Draw
for i in range(1, WIDTH - 1):
    for j in range(1, HEIGHT - 1):
        #print(str(int((i * WIDTH + j) / (WIDTH * HEIGHT) * 100)) + "%")
        a = interpolate(i, 0, WIDTH, -scale, scale) + offset[0]
        b = interpolate(j, 0, HEIGHT, -scale, scale) + offset[1]
        ca = a
        cb = b
        n = 0
        while n < maxiterations:
            aa = a * a - b * b
            bb = 2 * a * b
            a = aa + ca
            b = bb + cb
            if abs(a + b) > 16:
                break
            n += 1
        bright = interpolate(n, 0, maxiterations, 0, 255)
        if n == maxiterations:
            bright = 0
        screen.set_at((i, j), (bright, bright, bright))
    pygame.display.flip()
pygame.display.flip()
running = True
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)

pygame.quit()
