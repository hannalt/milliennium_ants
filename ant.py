import numpy as np
import random
from multipledispatch import dispatch
from board import *
from spot import *

class Ant:

	def __init__ (self, start_x, start_y, board, name = "part of the hive"):
		self.change_name(name)
		self.board = board
		self.spot = self.board.get_spot(start_x, start_y)
		self.x = start_x
		self.y = start_y
		self.board.start_locations(self.spot)
		self.time_reset()
		self.last = None
	
	def move(self, diag= False, last_matters = False):
		self.time += 10 #seconds 
		#x_choice is the movement in the x direction, y_choice is the movement in the y.
		choice = random.choice(self.spot.get_valid_spots(diag, last_matters, self.last))
		self.teleport(choice)
		
	def get_location(self):
		return self.x, self.y

	def get_spot(self):
		return self.spot
	
	def get_time(self):
		return self.time
	
	def get_name(self):
		return self.name
  	
	def time_reset(self):
		self.time = 0 #seconds

	def change_name(self, new_name):
		self.name = new_name
	
	@dispatch(object)
	def teleport(self, spot):
		self.last = self.spot
		self.board.update_ant(self.last, spot)
		self.spot = spot
		self.x = spot.get_x()	
		self.y = spot.get_y()

	@dispatch(int, int)
	def teleport(self, x, y):
		spot = self.board.get_spot(x, y)
		self.teleport(spot)

	def print_ant_info(self):
		print("x:", self.x, "y:",  self.y, "spot:", self.spot,"spot_index:", self.board.get_spot_index(self.spot), "time:", self.time)
