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
    shots = pygame.sprite.Group()

    #assign containers
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    #game initialization
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #set display mode
    clock = pygame.time.Clock()                                     #game clock
    dt = 0                                                          #delta time
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)                #initialize player at center of screen
    asteroid_field = AsteroidField()                                #create the asteroid field
    score = 0                                                       #set starting score to 0
    lives_remaining = PLAYER_LIVES                                  #set starting lives

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
                lives_remaining -= 1 #player loses 1 life on asteroid collision
                
                if lives_remaining <= 0:
                    print(f"Game over! Your score was: {score} points")
                    return
                
                #kill all and respawn
                pygame.sprite.Sprite.kill(player)
                for asteroid in asteroids: pygame.sprite.Sprite.kill(asteroid)
                player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        
        #check if each asteroid is colliding with each shot
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding(shot):
                    score += 1
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)

        #draw all in drawables container
        for drawable in drawables:
            drawable.draw(screen)
        
        pygame.display.flip() #refresh display

        #limit to  60 fps and assign delta time
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
