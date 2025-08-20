import pygame # type: ignore
from constants import * 
from player import *

def main():
    pygame.init()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #set display mode
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True: #game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if quit event type
                return                    #return nothing, quit program
        
        screen.fill("black")
        for updatable in updatables:
            updatable.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()

        #limit to  60 fps
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
