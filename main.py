from play import *
def main():

	for i in range(2):
		print("type", i)
		print("normal")
		go(i)
		print("diagonal")
		go(i, True)
		print("last matters")
		go(i, False, True)
		print("last matters and diag")
		go(i, True, True)
	


if __name__ == "__main__":
	main()


