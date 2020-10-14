from board import *
from ant import *

def build(x_width= 8, y_length = 8, start_positions = [[0,0],[7,7]]):
	chess_board = Board(x_width, y_length)
	ants = []
	for ant_position in start_positions:
		ant = Ant(ant_position[0], ant_position[1], chess_board)
		#ant.print_ant_info()
		ants.append(ant)
	return chess_board, ants

def same_end(chess_board, ants, diag = False, last_matters = False):

	while chess_board.ants_not_on_same_spot():
		for ant in ants:
			#print("ant")
			ant.move(diag, last_matters)
			#ant.print_ant_info()
		#if last_matters:
		#	print("ant loc:", chess_board.get_ant_locations())
	
	print("same_spot:", chess_board.get_ant_locations(), "in" , ants[0].get_time(), "time")

	return ants[0].get_time()

