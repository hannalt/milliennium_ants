import numpy as np
import random
from multipledispatch import dispatch
from board import *
from spot import *

class Ant:
	
	#This function creates the ant
	#param start_x:	starting x-coor
	#param start_y: starting y-coor
	#param board:	board the ant is on
	#param name:	The name of ant. This is just for fun so it has a default value. 
	#		But change it for fun or organization.
	def __init__ (self, start_x, start_y, board, name = "part of the hive"):
		self.change_name(name)
		self.board = board
		self.spot = self.board.get_spot(start_x, start_y)
		self.start_x = start_x
		self.start_y = start_y 
		self.x = start_x
		self.y = start_y
		self.time_reset()
		self.last = None
		self.last_index = -1

	#This function moves the ant and adds 10 seconds to the time
	#param diag:		default to false, but can be turned on to allow diagonal moves
	#param last_matters:	default to false, but can be turned on to not allow going back
	#			to previous location.	
	def move(self, diag= False, last_matters = False):
		self.time += 10 #seconds 
		choice = random.choice(self.spot.get_valid_spots(diag, last_matters, self.last)) #chooses a spot out of the valid spot the current spot returns. See get_valid_spots in spot.py for more info.
		self.teleport(choice) 
	
	#This function restarts the ants. Resets time and position.
	def restart(self):
		self.time_reset()
		self.teleport(self.start_x, self.start_y)
		self.last = None
		self.last_index = -1
		
	#returns current coors
	def get_location(self):
		return self.x, self.y
	
	#returns current spot
	def get_spot(self):
		return self.spot

	#returns index of current spot
	def get_spot_index(self):
		return self.board.get_spot_index(self.spot)

	#returns index of last visited spot
	def get_last_index(self):
		return self.last_index
	
	#returns time
	def get_time(self):
		return self.time
	
	#returns name
	def get_name(self):
		return self.name
  	
	#sets time to 0
	def time_reset(self):
		self.time = 0 #seconds

	#changes the name if you'd ever want to. This is just for fun again.
	def change_name(self, new_name):
		self.name = new_name
	
	#teleports ant to a different spot. 
	@dispatch(object)
	def teleport(self, spot):
		self.last_index = self.get_spot_index()
		self.last = self.spot
		self.spot = spot
		self.x = spot.get_x()	
		self.y = spot.get_y()

	#same as above but takes in the coors of the spot
	@dispatch(int, int)
	def teleport(self, x, y):
		spot = self.board.get_spot(x, y)
		self.teleport(spot)

	#prints information above the ant.
	def print_ant_info(self):
		print("x:", self.x, "y:",  self.y, "spot:", self.spot,"spot_index:", self.get_spot_index(), "time:", self.time)
