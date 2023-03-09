import pygame
# import time
from pygame.locals import *

def bloque():
    window_game.fill((171, 179, 64))
    window_game.blit(bloque,(0,0))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    window_game = pygame.display.set_mode(size=(500,500))
    window_game.fill((171, 179, 64))

    # cargar un bloque - image
    bloque = pygame.image.load('img/rect815.png').convert()
    window_game.blit(bloque,(0,0))

    pygame.display.flip() # actualiza la pantalla del juego
    # time.sleep(5)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False