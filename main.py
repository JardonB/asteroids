import pygame # type: ignore
from constants import * 
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()

    #create containers
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #assign containers
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)

    #game initialization
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #set display mode
    clock = pygame.time.Clock()                                     #game clock
    dt = 0                                                          #delta time
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)                #initialize player at center of screen
    asteroid_field = AsteroidField()

    while True: #game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if quit event type
                return                    #return nothing, quit program
        
        screen.fill("black") #fill the screen black

        #update all in updatables container
        for updatable in updatables:
            updatable.update(dt)

        #check if each asteroid is colliding with player
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                return

        #draw all in drawables container
        for drawable in drawables:
            drawable.draw(screen)
        
        pygame.display.flip() #refresh display

        #limit to  60 fps and assign delta time
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
