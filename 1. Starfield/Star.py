import math
import random
import pygame

class Star:
    def __init__(self, width, height, position=None):
        # Constants
        self.w = width
        self.h = height
        self.radius = 1

        if not position:
            self.position = pygame.math.Vector2(random.randrange(width), random.randrange(height))
        else:
            self.position = position
        try:
            self.direction = pygame.math.Vector2(self.position[0] - width // 2, self.position[1] - height // 2).normalize()
        except ValueError:
            self.direction = pygame.math.Vector2(random.random() * 2 - 1, random.random() * 2 - 1)

        # Parameters
        self.speed = 1

    def update(self):
        self.radius = max(Star.distance(self.position, (self.w // 2, self.h // 2)) // 50, 0.5)
        self.position += self.direction * self.speed * self.radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)
        pygame.draw.line(screen, (255, 255, 255), self.position, self.position - self.direction * self.radius * 10)

    def away(self):
        return Star.distance(self.position, (self.w // 2, self.h // 2)) > max(self.w, self.h) * 2

    @staticmethod
    def distance(a, b):
        return math.sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))
