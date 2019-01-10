import pygame, sys
import random
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

		# Programming of success
		for i in range(16):
			self.objects.append(Enemy(self)) 
			self.objects[i].set_image('bottle.png')
			self.objects[i].move()


		# Window setup
		self.screen = pygame.display.set_mode(self.resolution)
		pygame.display.set_caption('Czulow Game')
		self.screen.blit(self.bg, (0, 0))

		self.clock = pygame.time.Clock()

		# Game objects
		self.player = Player(self)
		self.player.set_image('postac.png')

		#self.bottle = Enemy(self)	
		#self.bottle.set_image('bottle.png')
		# Colors
		self.black = (0, 0, 0)
		self.white = (255, 255, 255)

		self.start_screen()
	
	# Main loop
	def main(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit(0)
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:	
					pygame.quit()
					sys.exit(0)

			self.delta += self.clock.tick() / 1000
			while self.delta > 1 / self.tps_max:
				self.tick()
				#self.random_resp()
				self.delta -= 1 / self.tps_max

			# Painting
			self.draw()
			pygame.display.update()
			#pygame.time.delay(100)

#	def random_resp(self): 
		#while True:
		
#		for i in range(16):
#			self.objects.append(Enemy(self)) 
#			self.objects[i].set_image('bottle.png')
#			self.objects[i].move()
		
	def tick(self):
		#self.bottle.move()
		self.player.move()
		for i in range(16):
			self.objects[i].move()
		
		
	def draw(self):
		self.screen.blit(self.bg, (0, 0))
		self.player.draw()
		for i in range(16):
			self.objects[i].draw(random.randint(1, 101))
		#self.bottle.draw()
	
	def start_screen(self):
		intro = True

		while intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
					

			self.screen.fill(self.white)

			self.button(100, self.HEIGHT / 2,
			'start_button.png',
			'start_button_ac.png', self.main)
		
			pygame.display.update()

	# Buttons drawing and events loop
	def button(self, x, y, image, active_img, action=None):	
		mouse = pygame.mouse.get_pos()	
		click = pygame.mouse.get_pressed()
		 
		if (x + 100) > mouse[0] > x and (y + 50) > mouse[1] > y:
			skin = pygame.image.load('pictures\\' + active_img)
			
			if click[0] == 1 and action != None: 
				action()	
		else:
			skin = pygame.image.load('pictures\\' + image)

		self.screen.blit(skin, (x, y))
		print(mouse)

			


if __name__ == "__main__":
	Game()
