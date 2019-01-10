import pygame
from pygame.math import Vector2

class GameObject:
	def __init__(self, game):
		self.game = game
		self.hp = 3
		self.skin = 0	
		self.name = ''

	def set_image(self, image_name):
		self.skin = pygame.image.load('pictures\\' + image_name)	
	
	def set_name(self, object_name):
		self.name = object_name
	
	def draw(self):
		self.game.screen.blit(self.skin, (100, 100))

class Player(GameObject):
	def __init__(self, game):
		self.game = game
		self.x = 10
		self.change_x = 0

	def move(self):
		# tutaj musze zwiekszac lub zmiejszac x		
		keypressed = pygame.key.get_pressed()
	
		print(pygame.event.get())
		if self.game.WIDTH - 64 > self.x > 0:	
			if keypressed[pygame.K_d]: 
				self.change_x += 1
				
			if keypressed[pygame.K_a]: 
				self.change_x -= 1
		else:	
			if self.x < 0:
				self.x = 64
			elif self.x > self.game.WIDTH:
				self.x = self.game.WIDTH - 64

		#if pygame.key.get_pressed() == pygame.KEYUP:
		
		self.x += self.change_x
		self.cahnge_x = 0

	def draw(self):
		self.game.screen.blit(self.skin, (self.x, self.game.HEIGHT - (64 + 5)))

class Enemy(GameObject):
	def __init__(self, game):
		self.game = game
		self.y = 0
		self.change_y = 0

	def move(self):
		if self.y < self.game.HEIGHT / 2:
			self.y += 10 

	def draw(self, position_x):
		#todo erase old object 
		
		self.game.screen.blit(self.skin, (10, self.y))
	
