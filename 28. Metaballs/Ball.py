import math
import random
import pygame


class Ball:
    def __init__(self, w, h, r):
        self.w, self.h = w, h
        self.r = r
        self.pos = pygame.Vector2(random.randrange(self.r, w - self.r), random.randrange(self.r, h - self.r))
        self.dir = pygame.Vector2(random.random(), random.random()).normalize()
        self.speed = 3

    def update(self):
        self.pos += self.dir * self.speed
        if self.pos.x + self.r > self.w or self.pos.x - self.r < 0:
            self.dir.x *= -1
        if self.pos.y + self.r > self.h or self.pos.y - self.r < 0:
            self.dir.y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 255), self.pos, self.r)

    def distance(self, point):
        return math.dist(self.pos, point)
