from board import *

class Spot:
	def __init__ (self, x, y, this_board):
		self.x = x
		self.y = y
		self.valid_diag_spots = []
		self.valid_spots = []
	
	def find_valid_spots(self, x_max, y_max, this_board):
		if self.x == x_max - 1:
			x_options = [-1, 0]
		elif self.x == 0:
			x_options = [0, 1]
		else:
			x_options = [-1, 0, 1]

		if self.y == y_max - 1:
			y_options = [-1, 0]
		elif self.y == 0:
			y_options = [0, 1]
		else:
			y_options = [-1, 0, 1]
		for x in x_options:
			for y in y_options:
				new_spot = this_board.get_spot(self.x + x, self.y + y)
				if x == 0 and y == 0:
					continue
				elif x == 0:
					self.valid_spots.append(new_spot)
				elif y == 0:
					self.valid_spots.append(new_spot)
				self.valid_diag_spots.append(new_spot)
		

	def get_valid_spots(self, diag, last_matters, last):

		if last_matters and diag:
			return self.last_matters(self.valid_diag_spots, last)
		if diag:
			return self.valid_diag_spots
		if last_matters:
			return self.last_matters(self.valid_spots, last)
		return self.valid_spots	

	def last_matters(self, spots, last):
		if last == None:
			return spots
		new_spots = []
		index = spots.index(last)
		for i in range(len(spots)):
			if i != index:
				new_spots.append(spots[i])
		return new_spots  
	
	def get_x(self):
		return self.x
	
	def get_y(self):
		return self.y
	
	def print_spot_info(self):
		print("spot \t x:" , self.x, "\t y:", self.y)
		
