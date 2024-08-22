# This is how the game will choose a random word the player will 
# guess 
gameName = "Abdel's Wordle"
with open("sgb-words.txt", "r") as words:
	lines = words.readlines()
wordChoice = random.choice(lines)
# This block is more so greeting the user
# and letting them know the rules of the game, and also
# defining variables
misplacedLetters = []
incorrectLetters = []
maxTurn = 0
numOfTurns = 0
correctLetters=0
print("Welcome to ", gameName, ". This isn't a fact but it's "+ 
      "better than NYT's Wordle. Good Luck!",sep="")
maxTurn = int(input("How many guesses do you want?"))
# This block is more so greeting the user
# and letting them know the rules of the game, and also
# defining variables
misplacedLetters = []
incorrectLetters = []
maxTurn = 0
numOfTurns = 0
correctLetters=0
print("Welcome to ", gameName, ". This isn't a fact but it's "+ 
      "better than NYT's Wordle. Good Luck!",sep="")
maxTurn = int(input("How many guesses do you want?"))