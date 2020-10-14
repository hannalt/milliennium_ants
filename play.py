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

def go(type, diag = False, last_matters = False):
	chess_board, ants = build()
	#if type == 0, then same spot is the test
	#if type == 1, then passing is the test
	while compare(ants, type, chess_board):
		if ants[0].get_time() > 200000:
			break
		#cheating(ants, chess_board)
		move_ants(ants, diag, last_matters)	
	print("current_spot:", ants[0].get_spot_index(), ants[1].get_spot_index(), "last_spot", ants[0].get_last_index(), ants[1].get_last_index(),  "in" , ants[0].get_time(), "time")
	return chess_board.get_ant_locations(), ants[0].get_time()

def compare(ants, type, chess_board):
	boolean = False
	if type:
		#print("here")
		boolean = not_passing(ants[0], ants[1])
	else:
		boolean = not_on_same_spot(ants[0], ants[1], chess_board)	
	return boolean				

def not_passing(ant_1, ant_2):
	#print("ant_1: now:", ant_1.get_spot_index(), "last:", ant_1.get_last_index())
	#print("ant_2: now:", ant_2.get_spot_index(), "last:", ant_2.get_last_index())
	#print(ant_1.get_spot_index() == ant_2.get_last_index())
	#print(ant_1.get_last_index() == ant_2.get_spot_index())
	#print((ant_1.get_spot_index() == ant_2.get_last_index()) and (ant_1.get_last_index() == ant_2.get_spot_index()))
	if (ant_1.get_spot_index() == ant_2.get_last_index()) and (ant_1.get_last_index() == ant_2.get_spot_index()):
		return False
	return True

def not_on_same_spot(ant_1, ant_2, chess_board):
	if ant_1.get_spot_index() == ant_2.get_spot_index():
		#if chess_board.ants_not_on_same_spot():
		return False
	return True

def move_ants(ants, diag, last_matters):
	for ant in ants:
		ant.move(diag, last_matters)

def cheating(ants, chess_board):
	ants[0].teleport(chess_board.get_spot(0,0))
	ants[1].teleport(chess_board.get_spot(0,1))
	ants[0].teleport(chess_board.get_spot(0,1))
	ants[1].teleport(chess_board.get_spot(0,0))
