import pygame
from constants import * 

def main():
    pygame.init()
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True: #game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #closes program
                return
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
