import pygame, sys
from player import GameObject, Player, Enemy

class Game(object):
	def __init__(self):
		pygame.init()

		# Constans 
		self.WIDTH = 640
		self.HEIGHT = 480
		self.resolution = (self.WIDTH, self.HEIGHT)
		self.tps_max = 60.0	
		self.delta = 0.0	
		self.bg = pygame.image.load('pictures\\tlo.jpg')
		self.objects = []

		# Window setup
		self.screen = pygame.display.set_mode(self.resolution)
		pygame.display.set_caption('Czulow Game')
		self.screen.blit(self.bg, (0, 0))

		self.clock = pygame.time.Clock()

		# Game objects
		self.player = Player(self)
		self.player.set_image('postac.png')

		self.bottle = Enemy(self)	
		self.bottle.set_image('bottle.png')

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
			#pygame.time.delay(100)

	def tick(self):
		self.bottle.move()
		self.player.move()

	def draw(self):
		self.screen.blit(self.bg, (0, 0))
		self.player.draw()
		self.bottle.draw()

if __name__ == "__main__":
	Game()
