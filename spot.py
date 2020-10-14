from board import *

class Spot:
	#This function saves the Spot's coordinates
	#param 	x: 		x-coordinate
	#param 	y: 		y-coordinate
	#param 	this_board:	board that the spot is on
	def __init__ (self, x, y, this_board):
		self.x = x
		self.y = y
		self.valid_diag_spots = []
		self.valid_spots = []
	
	#This function finds spots that the ant can move to if it is on this Spot
	#param	x_max:		number of spots in the x direction on the board
	#param	y_max:		number of spots in the y direction on the board
	#param	this_board:	board that the spot is on
	def find_valid_spots(self, x_max, y_max, this_board):
		#This if statements find out if the Spot of on the edge of the board
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
				#we don't want this case because it would make to this spot
				if x == 0 and y == 0:
					continue
				#valid_spots is for when diag is off, so at least x or y has to be zero for it to be a valid move.
				elif x == 0:
					self.valid_spots.append(new_spot)
				elif y == 0:
					self.valid_spots.append(new_spot)
				self.valid_diag_spots.append(new_spot)
		
	#This function gives a list of valid moves
	#param diag:		boolean for if diagonals are allowed. True means they are allowed.
	#param last_matters:	boolean for if the ant can go back to the last spot it was at. True means they are not allowed to go backward.
	#param last:		last spot the ant was on
	#return list_of_spots:	returns list of valid spots
	def get_valid_spots(self, diag, last_matters, last):

		if last_matters and diag:
			return self.last_matters(self.valid_diag_spots, last)
		if diag:
			return self.valid_diag_spots
		if last_matters:
			return self.last_matters(self.valid_spots, last)
		return self.valid_spots	

	#This function returns a list of spots without the last spot the ant was on
	#param spots: 		list of valid moves including the last move
	#param last:		spot the ant was last on
	#return	new_spots:	list of valid moves without last move
	def last_matters(self, spots, last):
		if last == None:
			return spots
		new_spots = []
		index = spots.index(last)
		for i in range(len(spots)):
			if i != index:
				new_spots.append(spots[i])
		return new_spots  
	
	#returns spot's x-coor	
	def get_x(self):
		return self.x
	
	#returns spot's y-coor
	def get_y(self):
		return self.y
	
	#prints spot's coors
	def print_spot_info(self):
		print("spot \t x:" , self.x, "\t y:", self.y)
		
