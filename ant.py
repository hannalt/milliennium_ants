import numpy as np
import random
from multipledispatch import dispatch
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
		choice = random.choice(self.spot.get_valid_spots(diag))
		self.teleport(choice)
		
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
	
	@dispatch(object)
	def teleport(self, spot):
		self.spot = spot
		self.x = spot.get_x()	
		self.y = spot.get_y()

	@dispatch(int, int)
	def teleport(self, x, y):
		self.spot = self.board.get_spot(x, y)
		self.x = x
		self.y = y

	def print_ant_info(self):
		print("x:", self.x, "y:",  self.y, "spot:", self.spot,"spot_index:", self.board.get_spot_index(self.spot), "time:", self.time)
