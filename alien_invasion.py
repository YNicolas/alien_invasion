#!/user/bin/python3 
import sys
import pygame

def run_game():
    #Initialize game & creat a screen object
    pygame.init()
    screen = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Alien Invasion")

    #start game loop
    while True:
        #Monitor keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Refresh screen
        pygame.display.flip()

run_game()
