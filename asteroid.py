import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rando = random.uniform(20,50)
        v1= self.velocity.rotate(rando)
        v2 = self.velocity.rotate(-rando)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        astroid = Asteroid(self.position.x,self.position.y,new_radius)
        astroid.velocity = v1 * 1.2
        astroid = Asteroid(self.position.x,self.position.y,new_radius)
        astroid.velocity = v2 * 1.2
