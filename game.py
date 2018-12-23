import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Czulow Game')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)


		test = pygame.image.load('087.png')
		screen.blit(test, (20, 20))
		pygame.display.flip()
