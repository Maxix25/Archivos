import pygame
from pygame.locals import *
import sys
try:
	class Background(pygame.sprite.Sprite):
	    def __init__(self, image_file, location):
	        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
	        self.image = pygame.image.load(image_file)
	        self.rect = self.image.get_rect()
	        self.rect.left, self.rect.top = location
	pygame.init()

	screen = pygame.display.set_mode((500, 500))
	bg = Background("char/adventurer-idle-00.png", (0,0))
	screen.fill((255, 255, 255))
	screen.blit(bg.image, bg.rect)
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit(0)
except:
	pygame.quit()
	sys.exit(0)