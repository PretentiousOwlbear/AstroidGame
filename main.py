# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from Player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, drawable, updateable)

    player = Player(x, y)
    asteroidfield = AsteroidField()
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)
        for ast in asteroids:
             if ast.collision(player):
                  print("Game over!")
                  sys.exit()
        
        
             for shot in shots:
                  if ast.collision(shot):
                       ast.split()
                       shot.kill()

        screen.fill('black')

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
        main()