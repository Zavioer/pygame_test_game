import pygame, sys
from player import Player

class Game(object):
	def __init__(self):
		self.resolution = (640, 480)
		self.tps_max = 60.0	
		self.delta = 0.0	

		self.player = Player(self)

		self.screen = pygame.display.set_mode(self.resolution)
		pygame.display.set_caption('Czulow Game')
		self.clock = pygame.time.Clock()

		pygame.init()
		# Main loop
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:	
					sys.exit(0)

			self.delta += self.clock.tick() / 1000
			while self.delta > 1 / self.tps_max:
				self.delta -= 1 / self.tps_max

			# Painting
			# Backgound thigs
			self.bg = pygame.image.load('grafiki\\tlo.jpg')
			self.screen.blit(self.bg, (0, 0))
			self.draw()
			pygame.display.update()
			pygame.time.delay(100)
			# pygame.display.flip()

	def tick(self):
		pass

	def draw(self):
		self.player.draw()

if __name__ == "__main__":
	Game()
