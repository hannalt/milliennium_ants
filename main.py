from board import *
from ant import *

def main():
	chess_board = Board(8, 8)
	ant_1 = Ant(0, 0, chess_board)
	ant_2 = Ant(7, 7, chess_board)
	print("ant_1")
	ant_1.print_ant_info()
	print("ant_2")
	ant_2.print_ant_info()
	for i in range(8):
		print("ant_1")
		ant_1.move()
		ant_1.print_ant_info()
		print("ant_2")
		ant_2.move()
		ant_2.print_ant_info()
	#print(this_board)

if __name__ == "__main__":
	main()
