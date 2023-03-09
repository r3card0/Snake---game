import pygame
# import time
from pygame.locals import *

def dibujar_bloque():
    window_game.fill((171, 179, 64))
    window_game.blit(bloque,(bloque_x,bloque_y))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    window_game = pygame.display.set_mode(size=(500,500))
    window_game.fill((171, 179, 64))

    # cargar un bloque - image
    bloque = pygame.image.load('img/rect815.png').convert()
    bloque_x = 100
    bloque_y = 100
    # window_game.blit(bloque,(0,0))

    pygame.display.flip() # actualiza la pantalla del juego
    # time.sleep(5)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                
                if event.key == K_UP:   # se refiere a la tecla de la flecha hacia arriba
                    bloque_y -= 10      # que se mueva 10 posiciones a la inicial
                    dibujar_bloque()    # después del movimiento, que dibuje el bloque

                if event.key == K_DOWN: # se refiere a la tecla de la flecha hacia abajo
                    bloque_y += 10      # que se mueva 10 posiciones a la inicial
                    dibujar_bloque()    # después del movimiento, que dibuje el bloque

                if event.key == K_LEFT:
                    bloque_x -= 10
                    dibujar_bloque()    # después del movimiento, que dibuje el bloque

                if event.key == K_RIGHT:
                    bloque_x += 10
                    dibujar_bloque()    # después del movimiento, que dibuje el bloque
                    

            elif event.type == QUIT:
                running = False