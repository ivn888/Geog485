# Simulates one game of Hi Ho! Cherry-O
 
import random

# Create a list to hold the number of turns to win a game
turnsToWin = []

for num in range(0,10000):

    spinnerChoices = [-1, -2, -3, -4, 2, 2, 10]
    turns = 0
    cherriesOnTree = 10
     
    # Take a turn as long as you have more than 0 cherries
    while cherriesOnTree > 0:
     
        # Spin the spinner
        spinIndex = random.randrange(0, 7)
        spinResult = spinnerChoices[spinIndex]
     
        # Add or remove cherries based on the result
        cherriesOnTree += spinResult
     
        # Make sure the number of cherries is between 0 and 10   
        if cherriesOnTree > 10:
            cherriesOnTree = 10
        elif cherriesOnTree < 0:
            cherriesOnTree = 0
     
        turns += 1

    turnsToWin.append(turns)

print "The average turns to win a game of Hi Ho! Cherry-O is " + str(sum(turnsToWin)/len(turnsToWin))