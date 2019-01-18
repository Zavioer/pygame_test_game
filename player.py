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
		if self.game.WIDTH - 65 > self.x > 1:	
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
	def __init__(self, game, position_x):
		self.game = game
		self.position_x = position_x
		self.y = 0
		self.change_y = 0
		self.i = 0
		#self.obj = pygame.draw.rect(self.game.screen, (0, 0, 255), ((self.position_x, -10), (16, 16)))	
		self.e_skin = pygame.image.load('pictures\\bottle.png')
		self.e_skin_rect = self.e_skin.get_rect()
		self.e_skin_rect.x = self.position_x

	def move(self, speed):
		#self.i += speed
		self.e_skin_rect.y += speed
		#self.obj.move(self.position_x, self.i)
		#print(self.i)
	
	def draw(self):
		self.game.screen.blit(self.e_skin, self.e_skin_rect)


