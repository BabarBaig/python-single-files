""" This game feels like a simplified version of Tetris """

import pygame
import random
from dataclasses import dataclass
from typing import Final

BLACK: Final = (0,   0,   0)
RED:   Final = (255, 0,   0)
BLUE:  Final = (0,   0, 255)
YELLOW:Final = (255, 255, 0)

@dataclass
class Screen():
	width: int
	height: int

@dataclass()
class Player:
	size: int
	speed: int
	max_right: int
	max_left: int
	pos_x : int
	pos_y : int

	def __init__(self, max_right, max_left=0, pos_x=0, pos_y=0, size=50, speed=1):
		self.max_right = max_right
		self.max_left = max_left
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.size = size
		self.speed = speed

class Game():

	def drop_enemies(self, enemy_list, screen_sz):
		delay = random.random()
		difficulty = 8
		if len(enemy_list) < difficulty and delay < 0.1:
			size1 = 50
			max_right1 = screen_sz.width-size1
			pos_x1 = random.randrange(0, max_right1)
			enemy = Player(size=size1, max_right=max_right1, pos_x=pos_x1, speed=7)
			enemy_list.append(enemy)

	def draw_enemies(self, enemy_list, screen):
		for enemy in enemy_list:
			pygame.draw.rect(screen, BLUE, (enemy.pos_x, enemy.pos_y, enemy.size, enemy.size))

	def update_enemy_posn(self, enemy_list, screen_sz, score):
		for enemy in enemy_list:
			y = enemy.pos_y
			if  y >= 0 and y < screen_sz.height:
				y += enemy.speed
			else:				# Start new descent
				enemy.pos_x = random.randrange(0, enemy.max_right)
				y = 0
				score += 100
			enemy.pos_y = y
		return score

	def collision_check(self, enemy_list, playr):
		for enemy in enemy_list:
			if self.detect_collision(enemy, playr):
				return True
		return False

	def detect_collision(self, enemy, playr):
		p_x = playr.pos_x
		p_y = playr.pos_y
		e_x = enemy.pos_x
		e_y = enemy.pos_y

		isxcoll = False
		isycoll = False

		if   (e_x >= p_x) and (e_x < p_x + playr.size):		isxcoll = True
		elif (e_x <= p_x) and (e_x + enemy.size > p_x):		isxcoll = True
		if   (e_y <= p_y) and (e_y + enemy.size > p_y):		isycoll = True
		elif (e_y >= p_y) and (e_y < p_y + playr.size):		isycoll = True

		return isxcoll and isycoll

	def play(self):
		score = 0
		enemy_list = []
		screen_sz:Final = Screen(width=800, height=600)	# Screen Dimensions

		size1 = 50
		max_right1 = screen_sz.width - size1
		pos_x1 = screen_sz.width//2
		pos_y1 = screen_sz.height-size1
		playr = Player(size=size1, max_right=max_right1, pos_x=pos_x1, pos_y=pos_y1)

		pygame.init()
		score_font = pygame.font.SysFont("monospace", 30)
		BGColor = BLACK
		screen = pygame.display.set_mode((screen_sz.width, screen_sz.height))
		clock = pygame.time.Clock()
		not_done = True
		while not_done:
			for event in pygame.event.get():
				x = playr.pos_x
				if event.type == pygame.QUIT:
					not_done = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						x -= playr.size // 2
						if x < playr.max_left:
							x = playr.max_right
					elif event.key == pygame.K_RIGHT:
						x += playr.size // 2
						if x > playr.max_right:
							x = playr.max_left
					playr.pos_x = x

			screen.fill(BGColor)	# Refresh screen before redrawing square
			self.drop_enemies(enemy_list, screen_sz)
			score = self.update_enemy_posn(enemy_list, screen_sz, score)
			text = 'Score: ' + str(score)
			label = score_font.render(text, 1, YELLOW)
			screen.blit(label, (screen_sz.width-200, screen_sz.height-35))
			# print('Score:', score)
			if self.collision_check(enemy_list, playr):
				not_done = False
			self.draw_enemies(enemy_list, screen)
			pygame.draw.rect(screen, RED,  (playr.pos_x, playr.pos_y, playr.size, playr.size))
			clock.tick(30)
			pygame.display.update()
		print('Score:', score)

def main():
	game = Game()
	game.play()

if __name__ == '__main__':
	main()
