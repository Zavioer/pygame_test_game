import pygame
from pygame.math import Vector2

class Player(object):
	def __init__(self, game):
		self.game = game
		self.hp = 3

		self.skin = pygame.image.load('pictures\\postac.png').convert()	
	
		# Movement
		self.pos = Vector2(10, 10)
		self.vel = Vector2(0, 0)
		self.acc = Vector2(0, 0)

		self.game.screen.blit(self.skin, (self.pos.x, self.pos.y))
	

	def add_force(self, force):
		self.acc += force	

	def tick(self):
		keypressed = pygame.key.get_pressed()
		if keypressed[pygame.K_a]:
			self.add_force(Vector2(-1, 0))
		if keypressed[pygame.K_d]:
			self.add_force(Vector2(1, 0))
	
		# Physics 
		self.vel *= 0.9 

		self.vel += self.acc
		self.pos += self.vel
		self.acc *= 0

	def draw(self):
		print(self.pos.x)
		# buff_position = self.skin.get_rect()
		# self.game.screen.blit(self.game.bg, buff_position, buff_position)
		self.game.screen.blit(self.skin, (self.pos.x, self.pos.y))
		self.game.screen.blit(self.game.bg, (self.pos.x, self.pos.y))


