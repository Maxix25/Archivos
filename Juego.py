import sys
import pygame
#Inicializamos pygame
pygame.init()
#Hacemos que muestra una ventana 800x600
size = 800, 600
screen = pygame.display.set_caption("Juego BALL")
#Comenzamos el bucle
run=True
while run:
	#Capturamos los eventos que se han producido
	for event in pygame.event.get():
		#Si el evento es salir terminamos
		if event.type == pygame.QUIT: run=False

#Salgo de pygame
pygame.quit()
