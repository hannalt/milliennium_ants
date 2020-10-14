from play import *
def main():
	chessboard, ants = build()
	print("normal")
	same_end(chessboard, ants)
	print("diagonal")
	chessboard, ants = build()
	same_end(chessboard, ants, True)
	print("last matters")
	chessboard, ants = build()
	same_end(chessboard, ants, False, True)
	print("last matters and diag")
	chessboard, ants = build()
	same_end(chessboard, ants, True)


if __name__ == "__main__":
	main()


