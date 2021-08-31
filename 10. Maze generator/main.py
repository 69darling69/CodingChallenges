import math
import random
import pygame
from Cell import Cell


pygame.init()
pygame.display.set_caption("Maze generator")

FPS = 60
WIDTH, HEIGHT = 800, 600
SIZE = 50
W_COUNT, H_COUNT = WIDTH // SIZE, HEIGHT // SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cells = {}
for i in range(W_COUNT):
    for j in range(H_COUNT):
        cells[(i, j)] = Cell()

walker = (0, 0)
stack = []

running = True
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    cells[walker].empty = False
    variants = []
    if walker[0] != 0 and cells[(walker[0] - 1, walker[1])].empty:
        variants.append((walker[0] - 1, walker[1]))
    if walker[0] != W_COUNT - 1 and cells[(walker[0] + 1, walker[1])].empty:
        variants.append((walker[0] + 1, walker[1]))
    if walker[1] != 0 and cells[(walker[0], walker[1] - 1)].empty:
        variants.append((walker[0], walker[1] - 1))
    if walker[1] != H_COUNT - 1 and cells[(walker[0], walker[1] + 1)].empty:
        variants.append((walker[0], walker[1] + 1))
    if len(variants) != 0:
        prev = walker
        walker = random.choice(variants)
        stack.append(walker)
        if prev[0] < walker[0]:
            cells[prev].right = False
            cells[walker].left = False
        elif prev[0] > walker[0]:
            cells[prev].left = False
            cells[walker].right = False
        elif prev[1] > walker[1]:
            cells[prev].top = False
            cells[walker].bottom = False
        elif prev[1] < walker[1]:
            cells[prev].bottom = False
            cells[walker].top = False
    else:
        if len(stack) == 0:
            running = False
        else:
            walker = stack.pop()

    # Draw
    screen.fill((128, 128, 128))

    for i in range(W_COUNT):
        for j in range(H_COUNT):
            if not cells[(i, j)].empty:
                pygame.draw.rect(screen, (255, 255, 255), (i * SIZE, j * SIZE, SIZE, SIZE))
            if cells[(i, j)].left:
                pygame.draw.line(screen, (0, 0, 0), (i * SIZE, j * SIZE), (i * SIZE, j * SIZE + SIZE), 2)
            if cells[(i, j)].top:
                pygame.draw.line(screen, (0, 0, 0), (i * SIZE, j * SIZE), (i * SIZE + SIZE, j * SIZE), 2)
            if cells[(i, j)].right:
                pygame.draw.line(screen, (0, 0, 0), (i * SIZE + SIZE, j * SIZE), (i * SIZE + SIZE, j * SIZE + SIZE), 2)
            if cells[(i, j)].bottom:
                pygame.draw.line(screen, (0, 0, 0), (i * SIZE, j * SIZE + SIZE), (i * SIZE + SIZE, j * SIZE + SIZE), 2)

    if len(stack) != 0:
        pygame.draw.rect(screen, (0, 128, 0), (walker[0] * SIZE + 1, walker[1] * SIZE + 1, SIZE - 1, SIZE - 1))
    pygame.display.flip()
    clock.tick(FPS)

running = True
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)

pygame.quit()
