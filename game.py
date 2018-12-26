import pygame, sys
from player import Player

class Game(object):
	def __init__(self):
		pygame.init()

		# Constans 
		self.resolution = (640, 480)
		self.tps_max = 60.0	
		self.delta = 0.0	
		self.bg = pygame.image.load('pictures\\tlo.jpg')

		# Window setup
		self.screen = pygame.display.set_mode(self.resolution)
		pygame.display.set_caption('Czulow Game')
		self.screen.blit(self.bg, (0, 0))

		self.clock = pygame.time.Clock()

		self.player = Player(self)

		# Main loop
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:	
					sys.exit(0)

			self.delta += self.clock.tick() / 1000
			while self.delta > 1 / self.tps_max:
				self.tick()
				self.delta -= 1 / self.tps_max

			# Painting
			self.draw()
			pygame.display.update()
			pygame.time.delay(100)

	def tick(self):
		self.player.tick()	

	def draw(self):
		self.player.draw()

if __name__ == "__main__":
	Game()
