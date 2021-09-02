import copy
import random

import pygame


def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


pygame.init()
pygame.display.set_caption("Reaction Diffusion")

FPS = 60
WIDTH, HEIGHT = 100, 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

old = [[[1, 0] for _ in range(WIDTH)] for _ in range(HEIGHT)]
size = 25
for i in range(WIDTH // 2 - size, WIDTH // 2 + 1 + size):
    for j in range(HEIGHT // 2 - size, HEIGHT // 2 + 1 + size):
        old[i][j] = [0, 1]
new = [[[1, 0] for _ in range(WIDTH)] for _ in range(HEIGHT)]

Da = 1.0
Db = 0.5
f = 0.055
k = 0.062

def laplas(arr, a, b, num):
    sum = 0
    sum += arr[a - 1][b - 1][num]
    sum += arr[a + 1][b - 1][num]
    sum += arr[a + 1][b + 1][num]
    sum += arr[a - 1][b + 1][num]
    sum *= 0.25
    sum += arr[a-1][b][num]
    sum += arr[a+1][b][num]
    sum += arr[a][b+1][num]
    sum += arr[a][b-1][num]
    sum *= 0.2
    sum -= arr[a][b][num]
    return sum

running = True
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    for i in range(1, WIDTH - 1):
        for j in range(1, HEIGHT - 1):
            A = old[i][j][0]
            B = old[i][j][1]
            ABB = A * B * B
            laplasA = laplas(old, i, j, 0)
            laplasB = laplas(old, i, j, 1)
            new[i][j][0] = constrain(A + (Da * laplasA - ABB + f * (1 - A)), 0, 1)
            new[i][j][1] = constrain(B + (Db * laplasB + ABB - (k + f) * B), 0, 1)

    old = copy.deepcopy(new)

    # Draw
    for i in range(1, WIDTH - 1):
        for j in range(1, HEIGHT - 1):
            c = constrain(old[i][j][0] - old[i][j][1], 0, 1) * 255
            screen.set_at((i, j), (c, c, c))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
