from spot import *
from multipledispatch import dispatch

class Board:
	#This function sets the width and length of the board and creates an array of Spots that make up the board.
	#param x_width:		width of board in x direction
	#param y_length:	length of board in y direction	
	def __init__ (self, x_width, y_length):
		self.x_width = x_width
		self.y_length = y_length
		self.spots = []

		#this loop creates the spots
		for y in range(y_length):
			for x in range(x_width):
				self.spots.append(Spot(x, y, self))
		
		#once all spots are created this has them find their neighbors 			
		for spot in self.spots:
			spot.find_valid_spots(self.x_width, self.y_length, self)

	#returns the spot
	def get_spot(self, x, y):
		return (self.spots[(self.x_width* y) + x])
	
	#returns the width
	def get_x_width(self):
		return self.x_width
	
	#returns the length
	def get_y_length(self):
		return self.y_length
	
	#returns the index of the spot
	@dispatch(object)
	def get_spot_index(self, spot):
		return self.spots.index(spot)
	
	#same as above but it takes in x and y coordinates
	@dispatch(int, int)
	def get_spot_index(self, x, y):
		return (self.x_width * y) + x
