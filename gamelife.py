import pygame
import numpy as np
import time

from pygame.constants import QUIT

pygame.init()
pygame.display.set_caption('El juego de la vida')

width, height = 1080, 700
screen = pygame.display.set_mode((width, height))

bg = 0,0,0
# color de fondo
screen.fill(bg)
 
# Definimos numero de celdas
nxC, nyC =100,100
# Definimos el tamaño de las celdas
dimCW = width / nxC
dimCH = height / nyC
# Estado de las celdas: Vivas definidas como 1 y Muertas como 0

estadoJuego= np.zeros((nxC,nyC))



# Control de la ejecucion del juego
pauseExect = False



 # Bucle de ejecucion
while True:

    nuevoestadoJuego = np.copy(estadoJuego)

    screen.fill(bg)
    time.sleep(0.01)

    # Asignacion de eventos de teclado y Mouse

    ev =pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()

            celX, celY = int(np.floor(posX/dimCW)),int(np.floor(posY/dimCH))
            nuevoestadoJuego[celX,celY] = not mouseClick[2]

    
    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:


                #Calculo de vecinos cercanos
                n_neight = estadoJuego[(x-1) % nxC, (y-1) % nyC ] + \
                        estadoJuego[(x) % nxC, (y-1) % nyC ] + \
                        estadoJuego[(x+1) % nxC, (y-1) % nyC ] + \
                        estadoJuego[(x-1) % nxC, (y) % nyC ] + \
                        estadoJuego[(x+1) % nxC, (y) % nyC ] + \
                        estadoJuego[(x-1) % nxC, (y+1) % nyC ] + \
                        estadoJuego[(x) % nxC, (y+1) % nyC ] + \
                        estadoJuego[(x+1) % nxC, (y+1) % nyC ] 

                # Regla del juego n1 = Una celda con 3 vecinas vivas Revive
                if estadoJuego[x,y] == 0 and n_neight ==3:
                    nuevoestadoJuego[x,y] =1
                # Regla del juego n2 = Una celda viva con menos de 2 o mas de 3 vecinas vivas Muere
                elif estadoJuego[x,y] == 1 and (n_neight < 2 or n_neight > 3):
                    nuevoestadoJuego[x,y] = 0


            # Creacion de Poligono de cada celda dibujada
            poly = [((x) * dimCW, y * dimCH),
                    ((x+1) *  dimCW, y * dimCH),
                    ((x+1) *  dimCW, (y+1) * dimCH),
                    ((x) *  dimCW, (y+1) * dimCH)]

            # Dibujo para la celda de cada par x y 
            if nuevoestadoJuego[x,y] == 0:

                pygame.draw.polygon(screen,(25,25,25), poly, 1)
            
            else:
                pygame.draw.polygon(screen,(0,128,0), poly, 0)

    # Actualizamos el estado del juego

    estadoJuego = np.copy(nuevoestadoJuego)


    # Actualizacion de la pantalla        
    pygame.display.flip()

    if event.type == QUIT:
        pygame.quit()
        SystemExit(0)




        

