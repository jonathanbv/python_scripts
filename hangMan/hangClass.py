import random as R
from tkinter import *
from tkinter import ttk
from configparser import ConfigParser

class hangMan:
    #load class-wide highscore
    figFile = "hangConfig.ini"
    config = ConfigParser()
    config.read(figFile)
    highScore = int(config['score']['highscore'])

    def __init__(self, wordsFile):
        self.score = 0
        self.wordList = list()
        print(wordsFile)
        fhand = open(wordsFile)
        try:
            for line in fhand:
                self.wordList.append(line.strip().lower())
        except Exception as e:
            print(e)
            self.wordList = ["goat", "duck", "chinchilla", "banana"]

        self.gui = hangGui(self)
        self.gui.build()

    def newGame(self):
        self.guessedList = list()
        self.guesses = 10
        self.gameOver = False

        R.shuffle(self.wordList)
        self.gameWord = self.wordList[0]
        print(self.gameWord)
        self.gameBoard = [] #try removing self see what happens
        for let in self.gameWord:
            self.gameBoard.append("_")

        self.gui.subButton['text'] = "Submit"
        self.gui.guessRemain['text'] = "Guesses Remaining: 10"
        self.gui.guessesMade['text'] = ""
        self.gui.word_display['text']= self.gameBoard
        self.gui.guessChar.set("")
        self.gui.user_guess.focus()

    #function for receiving input and checking guess:
    def usrSubmit(self, *arguments):
        #check if player has won/lost
        #start a new game if they have
        if self.gameOver == True:
            self.newGame()
            return None

        self.entry = self.gui.guessChar.get()
        self.gui.guessChar.set("")
        if self.entry in self.guessedList:
            return None
        else:
            self.guessedList.append(self.entry)
            self.guesses -= 1

        self.gameBoard = []
        for char in self.gameWord:
            if char in self.guessedList:
                self.gameBoard.append(char)
                print(self.gameBoard)
            else:
                self.gameBoard.append("_")
                print(self.gameBoard)

        self.gui.word_display['text']= self.gameBoard
        self.gui.guessRemain['text']= "Guesses Remaining: " + str(self.guesses)

        #check for victory, else continue game
        if self.gameWord == "".join(self.gameBoard):
            deltaScore = 100 + (5 * self.guesses)
            self.score += deltaScore
            self.gameOver = True
            self.gui.guessesMade['text'] ="You Won!"
            self.gui.subButton['text']="Play Again"
            print(self.score)
        elif self.guesses == 0:
            deltaScore = -10
            self.score =+ deltaScore
            self.gameOver = True
            self.gui.guessesMade['text'] = "You Lose!"
            self.gui.subButton['text']= "Play Again"
            self.gui.word_display['text']= self.gameWord
            print(self.score)

        if self.gameOver == True:
            if deltaScore > 0:
                deltaString = "+" + str(deltaScore)
            else:
                deltaString = str(deltaScore)
            self.gui.scoreBoard['text'] = "Score: " + str(self.score) + " (" + deltaString + ")"
        else:
            self.gui.scoreBoard['text']= "Score: " + str(self.score)
            self.gui.guessesMade['text']= self.guessedList

        if self.score > hangMan.highScore:
            self.updateHiScore()

        self.gui.user_guess.focus()

    def updateHiScore(self):
        self.gui.hiScoreBoard['text'] = "High Score: " + str(self.score)
        self.config.set('score','highscore',str(self.score))
        with open(hangMan.figFile, 'w') as figWrite: #does it improve readability/quality to use the class name wrt class var?
            self.config.write(figWrite)



class hangGui:

    def __init__(self, hangman):
        self.linkedMan = hangman
        self.root = Tk()
        self.root.title("Hangman")
        self.mainframe = ttk.Frame(self.root, padding=10) #need to define the size of it
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(1,pad=100)

        self.root.bind("<Return>",self.linkedMan.usrSubmit)

    def build(self):
        def guessValidator(input):
            if input.isalpha() and len(input) == 1:
                return True
            elif len(input) == 0: #allow deletion
                return True
            else:
                return False
        reg = self.root.register(guessValidator) #register callback function

        self.hiScoreBoard = ttk.Label(self.mainframe, text="High Score: " + str(self.linkedMan.highScore))
        self.hiScoreBoard.grid(column=0,row=0, sticky='W')

        #create an area to display the word being guessed
        self.word_display = ttk.Label(self.mainframe, text="",padding="40 10 40 0", font="Helvetica 20", justify = "center")
        self.word_display.grid(column=0,row=0,columnspan=3)

        self.scoreBoard = ttk.Label(self.mainframe, text="Score: 0")
        self.scoreBoard.grid(column=2,row=0)

        #create an area to display letters that have been guessed
        self.guessesMade = ttk.Label(self.mainframe, text= "abcdefghijklmnopqrstuvwxyz",font=20, padding="0 10 0 10") #hmm...
        self.guessesMade.grid(column=0,row=1, columnspan=3)

        #create an area to display number of guesses remaining
        self.guessRemain = ttk.Label(self.mainframe, text= "Guesses Remaining: 10")
        self.guessRemain.grid(column=0,row=2)

        #create an input area for the user to submit guesses
        self.guessChar = StringVar()
        self.user_guess = ttk.Entry(self.mainframe, width=10, textvariable = self.guessChar, validate="key",validatecommand=(reg,'%P'))
        self.user_guess.grid(column=1, row=2)
        self.user_guess.focus()

        #create a button for the user
        self.subButton = ttk.Button(self.mainframe, text="Submit",command=self.linkedMan.usrSubmit)
        self.subButton.grid(column=2,row=2, ipadx=2)
        self.linkedMan.newGame()

        self.root.mainloop()

        #a func for validating user input (no points deducted for stupid input)



##start the game
fileName = "words.txt"
h = hangMan(fileName)

#gui
