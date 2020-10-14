from play import *
def main(verbose = False, x_width = 8, y_length= 8, start_positions = [[0,0],[7,7]], names=["sally", "john"]):

	#the first yes or no refers to the diag and the second refers to the previous. The array is two dimensions
	#the first dimension is for same square citeria and the second is for passing citeria
	no_no = [[],[]]
	no_yes = [[],[]]
	yes_no = [[],[]]
	yes_yes = [[],[]]
	N = 5
	game = Game(names, x_width, y_length, start_positions)
	
	#This for loop plays each rule set N times and stores the answers in one of 4 arrays.
	for n in range(N):
		#i decides the type of citeria i == 0 means same square and i == 1 means passing. Look at go() in play.py for nore info.
		for i in range(2):
			no_no[i].append(game.go(i,verbose=verbose))
			yes_no[i].append(game.go(i, True, verbose=verbose))
			no_yes[i].append(game.go(i, False, True, verbose = verbose))
			yes_yes[i].append(game.go(i, True, True, verbose=verbose))

	no_no_avg = avg(no_no)
	no_yes_avg = avg(no_yes)
	yes_no_avg = avg(yes_no)
	yes_yes_avg = avg(yes_yes)

	
	print("Average time until the ants move onto the same square after ", N, " simulations:")
	print("+----------------------+----------------------+----------------------+")
	print("|                      |Move To Previous:Yes  |Move to Previous: No  |")
	print("+----------------------+----------------------+----------------------+")
	print("|Move Diagonally: No   |", no_yes_avg[0], "\t\t\t|", no_no_avg[0], "\t\t|")
	print("+----------------------+----------------------+----------------------+")
	print("|Move Diagonally: Yes  |", yes_yes_avg[0], "\t\t|", yes_no_avg[0], "\t\t|")
	print("+----------------------+----------------------+----------------------+")

	print("Average time until the ants cross pathes after ", N, " simulations:")
	print("+----------------------+----------------------+----------------------+")
	print("|                      |Move To Previous:Yes  |Move to Previous: No  |")
	print("+----------------------+----------------------+----------------------+")
	print("|Move Diagonally: No   |", no_yes_avg[1], "\t\t|", no_no_avg[1], "\t\t|")
	print("+----------------------+----------------------+----------------------+")
	print("|Move Diagonally: Yes  |", yes_yes_avg[1], "\t\t|", yes_no_avg[1], "\t\t|")
	print("+----------------------+----------------------+----------------------+")

#This function takes the averages of the two lists in the no/yes_no/yes arrays.
def avg(two_times):
	return_list = []
	for times in two_times:
		sum = 0
		for time in times:
			sum += time
		return_list.append(sum/len(times))
	return return_list

if __name__ == "__main__":
	main()

