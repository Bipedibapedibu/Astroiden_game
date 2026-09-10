import pygame
import sys
from constants import *
from logger import log_state,log_event
from player import Player
from astroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable,updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable,updatable,shots)
    Clock = pygame.time.Clock()
    dt: float = 0.0
    player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for objekt in drawable:
            objekt.draw(screen)
        for objekt in asteroids:
            k = False
            for object in shots:
                if objekt.collides_with(object):
                    log_event("asteroid_shot")
                    object.kill()
                    objekt.split()
                    k = True
                    break 
            if k:
                continue  
            if objekt.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        dt = Clock.tick(60) / 1000
        pygame.display.flip()
       

if __name__ == "__main__":
    main()