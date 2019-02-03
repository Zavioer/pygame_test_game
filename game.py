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
		self.bg = pygame.image.load('pictures\\background.png')

		# Window setup
		self.screen = pygame.display.set_mode(self.resolution)
		pygame.display.set_caption('Catch a Bottle!')
		self.screen.blit(self.bg, (0, 0))

		# Clock setup
		self.clock = pygame.time.Clock()
		
		# Sounds setup
		self.catch_sound = pygame.mixer.Sound('sounds\catch.wav')
		self.game_over_sound = pygame.mixer.Sound('sounds\gameover.wav')

		# Game objects
		self.x = random.randint(1, self.WIDTH - 32)
		self.difficulty = 5
		self.difficulty_counter = 0
		self.point_buff = 0 

		self.player = Player(self)
		self.player.set_image('character.png')
		self.enemy = Enemy(self, self.x)

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
				self.delta -= 1 / self.tps_max

			### Collisions detector
			if self.collisions_detector(self.player.x, self.player.y,
				self.enemy.e_skin_rect.x, self.enemy.e_skin_rect.y,
				32, 32) == True:	
				self.player.points += 1
				self.difficulty_counter += 1
				self.x = random.randint(1, self.WIDTH - 32)
				self.enemy = Enemy(self, self.x)
			###
			# Score counter

			# End of map enemy action 
			if self.enemy.e_skin_rect.y > self.HEIGHT:
				self.x = random.randint(1, self.WIDTH - 32)
				self.enemy = Enemy(self, self.x)
				self.player.hp -= 1
			
			# Break loop statement	
			if self.player.is_alive() == False:
				self.point_buff = self.player.points
				self.player.default_valuse()
				self.difficulty = 5
				self.game_over_screen()


			# Change difficulty
			if self.difficulty_counter == 5:
				self.difficulty += 1.5
				self.difficulty_counter = 0
				

			# Painting
			self.draw()
			pygame.display.update()

	def collisions_detector(self, ply_x, ply_y, obj_x, obj_y, obj_w, obj_h):
		if ply_y < obj_y + obj_h:
			if ply_x > obj_x and ply_x < obj_x + obj_w or ply_x + 42 > obj_x and ply_x + 42 < obj_x + obj_w:
				pygame.mixer.Sound.play(self.catch_sound)
				return True

	def quit_game(self):
		pygame.quit()
		quit()
		
	def tick(self):
		self.player.move()
		self.enemy.move(self.difficulty)
		
	def draw(self):
		self.screen.blit(self.bg, (0, 0))
		self.player.draw()
		self.enemy.draw()	
		self.print_score(self.player.points)
		self.print_lives(self.player.hp)
	
	### Scenes
	def start_screen(self):
		while True:
			for self.event in pygame.event.get():
				if self.event.type == pygame.QUIT:
					pygame.quit()
					quit()
					
			# Load and set imaga as background
			start_background = pygame.image.load('pictures\\menu.png')
			self.screen.blit(start_background, (0, 0))

			# START button
			self.button(100, self.HEIGHT / 2,
			'start_button.png',
			'start_button_ac.png', self.main)
			# EXIT button
			self.button(self.WIDTH - 200, self.HEIGHT / 2,
			'end_button.png',
			'end_button_ac.png', self.quit_game)
	
			pygame.display.update()

	def game_over_screen(self):
		pygame.mixer.music.stop()
		pygame.mixer.Sound.play(self.game_over_sound)

		while True:
			for self.event in pygame.event.get():
				if self.event.type == pygame.QUIT:
					pygame.quit()
					quit()
					
			# Load and set imaga as background
			start_background = pygame.image.load('pictures\\game_over.png')
			self.screen.blit(start_background, (0, 0))

			# RESET button
			self.button(self.WIDTH / 2 - 50, self.HEIGHT / 2 + 10,
			'reset_button.png',
			'reset_button_ac.png', self.start_screen)

			font = pygame.font.SysFont(None, 30)
			text = font.render('Your finale score is ' + str(self.point_buff) + ' bottles!', True, (0, 255, 0))
			self.screen.blit(text, (80, self.HEIGHT / 2 + 80))	

			pygame.display.update()
	###

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

	def print_score(self, count):	
		font = pygame.font.SysFont(None, 30)
		text = font.render('You caught ' + str(count) + ' bottles!', True, self.white)

		self.screen.blit(text, (0, 0))
			
	def print_lives(self, count):	
		font = pygame.font.SysFont(None, 30)
		text = font.render('Lives: ' + str(count), True, self.white)

		self.screen.blit(text, (0, 31))

if __name__ == "__main__":
	Game()
