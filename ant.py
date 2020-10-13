import numpy as np
import random
from board import *
from spot import *

class Ant:

	def __init__ (self, start_x, start_y, board, name = "part of the hive"):
		self.change_name(name)
		self.board = board
		self.teleport(start_x, start_y)	
		self.time_reset()
	
	def move(self, diag= False):
		self.time += 10 #seconds 
		#x_choice is the movement in the x direction, y_choice is the movement in the y.
		y_choice = 0
		x_choice = 0
		while y_choice == 0 and x_choice == 0:
			x_choice, y_choice = self.choose()
			print("x c:", x_choice)
			print("y c:", y_choice)
		if not diag and x_choice != 0 and y_choice != 0:
			#if diag isn't true the ant can only keep one of the choices
			x = random.randint(0,1)
			if x:
				y_choice = 0
			else:
				x_choice = 0
		self.teleport(self.x + x_choice, self.y + y_choice)
	def choose(self):
		return random.choice(self.spot.get_x_options()), random.choice(self.spot.get_y_options())
		
	def get_location(self):
		return self.x, self.y

	def get_spot(self):
		return self.spot
	
	def get_time(self):
		return time
	
	def get_name(self):
		return name
  	
	def time_reset(self):
		self.time = 0 #seconds

	def change_name(self, new_name):
		self.name = new_name

	def teleport(self, x, y):
		self.spot = self.board.get_spot(x, y)
		self.x = x
		self.y = y

	def print_ant_info(self):
		print("x:", self.x, "y:",  self.y, "spot:", self.spot,"spot_index:", self.board.get_spot_index(self.spot), "time:", self.time)
