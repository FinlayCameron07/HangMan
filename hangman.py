# imports
from random import randint

# getting random word

def getRandomWord(fileName):
    filePath = fileName
    wordArray = []
    file = open(filePath, "r")
    for line in file:
        word = line.strip()
        wordArray.append(word.lower())
    file.close()
    ranNum = randint(0, len(wordArray))
    WORD = wordArray[ranNum]
    return WORD


    

# main game

word = getRandomWord("lotsOfWords.txt")
print(word)

class Hangman:
    def __init__(self):
        self.WORD = word
        self.DISPLAY = [str("_") for x in range(len(self.WORD))]
        self.failedAttempts = 0
        

    def linearSearch(self, data, target):
        guessedLettersPOS = []
        for x in range(len(data)):
            if data[x] == target:
                guessedLettersPOS.append(x)
        return guessedLettersPOS
    
    def StartUpDisplay(self):
        print("Welcome to Hangman!")
        print("You have 6 tries to guess the word.")
        print("The word is " + str(len(self.WORD)) + " letters long.")
        print("Good luck!")
    
    def takeGuess(self):
        self.userGuess = str(input("Guess a letter: ")).lower()
        checkGuess = self.linearSearch(self.WORD, self.userGuess)
        if self.userGuess not in self.WORD:
            self.failedAttempts +=1 
        return checkGuess
    
    def updateDisplay(self, checkGuess):
        for x in range(len(checkGuess)):
            self.DISPLAY[checkGuess[x]] = self.userGuess
        print(f"{str(self.DISPLAY)}")

    def checkWin(self,userGuess):
        if "_" not in self.DISPLAY:
            print("You win!")
            print("Thanks for playing!")
            exit()

    def hangingMan(self,failedAttempts):
        if self.failedAttempts < 1:
            print("  _______")
            print(" |/      |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|___")

        elif self.failedAttempts == 1:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|___")
        elif self.failedAttempts == 2:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |       |")
            print(" |       |")
            print(" |")
            print(" |")
            print("_|___")
        elif self.failedAttempts == 3:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|")
            print(" |       |")
            print(" |")
            print(" |")
            print("_|___")
        elif self.failedAttempts == 4:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|/")
            print(" |       |")
            print(" |")
            print(" |")
            print("_|___")
        elif self.failedAttempts == 5:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|/")
            print(" |       |")
            print(" |      /")
            print(" |")
            print("_|___")
        elif self.failedAttempts == 6:
            print("  _______")
            print(" |/      |")
            print(" |      (_)")
            print(" |      \|/")
            print(" |       |")
            print(" |      / \ ")
            print(" |")
            print("_|___")
            print("You lose!")
            print("The word was " + str(self.WORD))
            print("Thanks for playing!")
            exit()

   
    
# main program

game = Hangman()
game.StartUpDisplay()
while True:
    gameInput = game.takeGuess()
    game.checkWin(gameInput)
    game.hangingMan(game.failedAttempts)
    game.updateDisplay(gameInput)


