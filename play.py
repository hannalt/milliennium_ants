from board import *
from ant import *

class Game:
	#This file helps run the document. It has helper functions that decide which rules to follow and how to build the board. 

	#This function builds the board and the ants
	#param x_width:		width of board in x direction. Set to 8 like standard chess board but can be changed.
	#param y_length:	length of board in y direction. Set to 8 like standard chess board but can be changed.
	#param start_positions:	a list of lists. The first dimension is the number of ants. The second dimension is the
	#			coordinates you want those ants to begin at. This dimension should always have 2 elements
	#		        Set to 2 ants starting in the right bottom and left top corners of the board. If you 
	#			change the size of the board remember to change this too.
	def __init__(self, names, x_width= 8, y_length = 8, start_positions = [[0,0],[7,7]]):
		self.chess_board = Board(x_width, y_length)
		self.ants = []
		for ant_position in start_positions:
			ant = Ant(ant_position[0], ant_position[1], self.chess_board, names[start_positions.index(ant_position)])
			self.ants.append(ant)

	#This function has the ants move until the citeria is met.
	#param type:		This is the citeria. If type == 0  then the program will stop when at least two ants are on the
	#			same spot. If type == 1, then the program will stop when at least two ants have crossed paths.
	#param diag:		This is for turning on diagonal moves
	#param last_matters:	This is to stop the ant from going back to the most recently visited spot 
	#return time:		This returns the time it took for the ants to meet the citeria.
	def go(self, type, diag = False, last_matters = False, verbose = True):
		self.reset()
		while self.compare(type):
			#This is to stop the infinite loop that's happening when last_matters == 1 and diag == 0.
			if self.ants[0].get_time() > 200000:
				break
			self.move_ants(diag, last_matters)	
		if verbose:
			print("type:", type, "diag:", diag, "last_matters:", last_matters, "current_spot:", self.ants[0].get_spot_index(), self.ants[1].get_spot_index(), "last_spot", self.ants[0].get_last_index(), self.ants[1].get_last_index(),  "in" , self.ants[0].get_time(), "time")
		return self.ants[0].get_time()

	#This functions starts the ants over
	def reset(self):
		for ant in self.ants:
			ant.restart()

	#This function compares the ants according to the desired type. See go() for details.
	def compare(self, type):
		boolean = False
		for ant_1 in self.ants:
			for ant_2 in self.ants:
				if ant_1 == ant_2:
					continue
		
				if type:
					boolean = self.not_passing(self.ants[0], self.ants[1])
				else:
					boolean = self.not_on_same_spot(self.ants[0], self.ants[1])	
			if not boolean:
				return False
		return boolean				

	#This function checks to see if the ants are not passing eachother
	def not_passing(self, ant_1, ant_2):
		if (ant_1.get_spot_index() == ant_2.get_last_index()) and (ant_1.get_last_index() == ant_2.get_spot_index()):
			return False
		return True

	#This functions checks to see if the ants are not on the same spot
	def not_on_same_spot(self, ant_1, ant_2):
		if ant_1.get_spot_index() == ant_2.get_spot_index():
			return False
		return True

	#This function moves each of the ants
	def move_ants(self, diag, last_matters):
		for ant in self.ants:
			ant.move(diag, last_matters)
	'''
	#This is a function where I force ants to pass to test my passing.
	def cheating(ants, chess_board):
		ants[0].teleport(chess_board.get_spot(0,0))
		ants[1].teleport(chess_board.get_spot(0,1))
		ants[0].teleport(chess_board.get_spot(0,1))
		ants[1].teleport(chess_board.get_spot(0,0))
	'''
