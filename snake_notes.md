# Snake 

[repository](https://github.com/codebasics/python_projects)


# Screen moving block
1. import libraries

import pygame, es la librería principal

import pygame.locals import *; para que se importa? cual es la razón?

¿Porque pone el entry point al inicio?

2. pygame.init() -> Es importante usar esta clase porque es la que inicia el módulo completo.
3. Creación de "surfaces". Una surface es . . . para eso se usará el comando/clase *set_mode* el cual inicia la ventana del juego. Es un paso básico para que corra el juego. [set_mode -documentation](https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode). El primer argumento es *size*, el cual permite indicar el tamaño de la ventana del juego. Las unidades del tamaño es en pixeles. 

````
import pygame
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode(size=(500,500))
````
con este código, parece que se abre algo, pero no pasa y se despliega un mensaje en la terminal

````
rsaldivar@1MXLRODRIGUE2:/mnt/c/Users/rodrigue2/code/training/python/games/snake$ python3 screen_moving_block.py
pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
````
Esto ocurrió porque al parecer aún no se termina de escribir el código. Para esto, el instructor propuso agregar import time y time.sleep(5) para que se vea la ventana 5 segundos y poder ver lo que el código puede hacer hasta este punto.

````
import pygame
import time
# from pygame.locals import *

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode(size=(500,500))
    time.sleep(5)
````
3. window_game.fill() -> En este punto la ventana del juego es negra y se puede cambiar. Para cambiar el color de la ventan del juego, usamos la función *fill()*. el formato de los colores son RGB, por lo que es necesario usar las 3 combinaciones que inician desde 0 hasta 255. [color - documentacion](https://www.pygame.org/docs/ref/color.html). Al la combinacion de 255,255,255, en esta linea. ```` window_game.fill((255,255,255))````, se busca que la pantalla tenga un fondo de color blanco
4. pygame.display.flip() -> en el punto anterior (3), cuando se corrio el programa, no sucedio nada y esto fue porque era necesario agregar pygame.display.flip(). esta linea permite actualizar el cambio que se aplico en la punto (3) en la pantalla, en este caso color blanco. Para ver la gama de combinaciones de colores con RGB, ver los colores en base a las combianciones, buscar en google "rgb color picker" y se mostrara un menú que permitira ver opciones.
5. Event loop. Es aplicar un loop para que mantenga abierta la ventana del juego en vez de usar el sleep statement (tiempo). Este loop, tendrá condiciones en las cuales permita al usuario, cerrar la pantalla. Primero de definira una variable asignandole el boleano True. running = True. Después, se abrira el loop *while*

Un event loop espera un input del usuario. Espera una acción a través del mouse, teclado, etc. Un event loop es fundamental en cualquier aplicación de programación. 

El event loop para este caso se creara con el loop *while*. El while es un infinite loop. 

Pygame cuenta con *event* [event -documentacion](https://www.pygame.org/docs/ref/event.html) el cual, permite indicar que acciones se deben realizar para cerrar la ventana del juego.Las acciones se pueden indicar implementando *type*. type contiene una lista de las acciones que se pueden ejecutar. Para poder implementar event.type debidamente, es necesario importar *locals* [locals -documentacion](https://www.pygame.org/docs/ref/locals.html). Locals sirve para importar algunas variables globales que serán usadas en la ventana del juego. Un ejemplo de esto, locals, permite el acceso a la constante KEYDOWN 

Salir de la pantalla del juego. Dentro del event loop, la linea:
````
elif event.type == QUIT:
    running = False
````
Indica que si el event.type es igual a QUIT, entonces, running es igual a False, lo que significaria cerrar la pantalla del juego. Y como se cierra la pantalla del juego? por algo tan simple que ya conozco, cerrar la pantalla y con el mouse dar click en la tachita y se cierra la pantalla del juego. 

Tambien se puede cerrar la pantalla del juego cuando se presiona la tecla ESC.
````
if event.type == KEYDOWN:
    if event.key == K_ESCAPE:
        running = False
````
6. Dibujar un bloque. Para dibujar un bloque en la pantalla del juego se necesita una imagen del bloque. el formato de la imagen es *jpg* y con el siguient código se carga (load) la imagen:
````
bloque = pygame.image.load(path).convert()
````

Quiero saber el tamaño del bloque del instructor 1.34 KB. Ya agregúe un bloque que hice en Inkscape

Este bloque se verá en la pantalla del juego, y con la siguiente línea, se puede indicar la variable de la imange y la posición de la imágen en la pantalla del juego:
````
window_game.blit(bloque,(50,50))
````
otra forma de indicar la posicion de la imagen es como sige, pero no lo aplicare:
````
block_x = 100
block_y = 100

window_game.blit(bloque,(block_x,block_y))
````
Se puede crar un función para dibujar el bloque en el juego

````
def bloque():
    window_game.fill((171, 179, 64))
    window_game.blit(bloque,(0,0))
    pygame.display.flip()
````
La idea de usar una función es para que 