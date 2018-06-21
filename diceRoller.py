from random import randint
from msvcrt import getch

def wait():
	print("Press ESC to quit, press any other key to repeat\n")
	while True:
		key = ord(getch())
		if key == 27:
			break
		else:
			rollDice()

def rollDice():
	
	print("---------------------------------------------\n")
	
	diceAmount = int(input("How many dice to roll?: "))
	print("")
	diceSides = int(input("How many sides on the die?: "))

	total = [randint(1,diceSides) for _ in range(diceAmount)]
	
	print("\n")
	print("Total: " + str(sum(total)) + "\n\nIndividual Die: " + str(total) + "\n")
	
	print("---------------------------------------------\n")
	wait()

rollDice()

