import pygame
from pygame.locals import *
import time

class Snake:
    def __init__(self,window_game) -> None:
        self.window_game = window_game
        self.block = pygame.image.load('img/rect815.png')
        self.x = 100
        self.y = 100
        self.direction = 'down'

    def dibujar_bloque(self):
        self.window_game.fill((117,179,64))
        self.window_game.blit(self.block,(self.x,self.y))
        pygame.display.flip()

    # Instance methods - metodos para mover el bloque
    def move_left(self):
        self.direction = 'left'
        # self.x -= 10
        # self.dibujar_bloque()

    def move_right(self):
        self.direction = 'right'
        # self.x += 10
        # self.dibujar_bloque()

    def move_up(self):
        self.direction = 'up'
        # self.y -= 10
        # self.dibujar_bloque()
    
    def move_down(self):
        self.direction = 'down'
        # self.y += 10
        # self.dibujar_bloque()

    def walk(self):
        if self.direction == 'up':
            self.y -= 10
        if self.direction == 'down':
            self.y += 10
        if self.direction == 'left':
            self.x -= 10
        if self.direction == 'right':
            self.x += 10

        self.dibujar_bloque()


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window_game = pygame.display.set_mode(size=(500,500))
        self.window_game.fill((171,179,64))
        self.snake = Snake(self.window_game) # ? para heredar los atributos de la clase Snake a la clase Game
        self.snake.dibujar_bloque() # ?

    # Instance method
    def run(self):
        running = True

        while running:
            for event in pygame.event.get(): # ?
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                        self.snake.dibujar_bloque()
                    
                    if event.key == K_DOWN:
                        self.snake.move_down()
                        self.snake.dibujar_bloque()

                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        self.snake.dibujar_bloque()

                    if event.key == K_LEFT:
                        self.snake.move_left()
                        self.snake.dibujar_bloque()
                
                elif event.type == QUIT:
                    running = False
            
            self.snake.walk()
            time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()