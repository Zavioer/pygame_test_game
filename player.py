import pygame
from pygame.math import Vector2

class GameObject:
	def __init__(self, game):
		self.game = game
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
		self.y = self.game.HEIGHT - (61 + 5)
		self.x = 10
		self.hp = 3000
		self.points = 0

	def move(self):
		# Keyboard input handling
		keypressed = pygame.key.get_pressed()

		if keypressed[pygame.K_d]: 
			self.x += 5
		if keypressed[pygame.K_a]: 
			self.x += -5
			
		print('Wartosc x ' + str(self.x))

	def is_alive(self):
		if self.hp <= 0:
			return False
		else:	
			return True

	def draw(self):
		self.game.screen.blit(self.skin, (self.x, self.y))
		print(self.hp)

	# I Dont know 
	def default_valuse(self):
		self.hp = 3
		self.points = 0

class Enemy(GameObject):
	def __init__(self, game, position_x):
		self.game = game
		self.position_x = position_x
		self.e_skin = pygame.image.load('pictures\\bottle.png')
		self.e_skin_rect = self.e_skin.get_rect()
		self.e_skin_rect.x = self.position_x

	def move(self, speed):
		self.e_skin_rect.y += speed
	
	def draw(self):
		self.game.screen.blit(self.e_skin, self.e_skin_rect)


