import pygame
import time
import random

WIDTH, HIGHT = 800, 1000
WIN = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Dont Get Smashed!")

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    

    pygame.quit()


if __name__ == "__main__":
    main()