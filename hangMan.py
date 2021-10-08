import random as R
from tkinter import *
from tkinter import ttk

#goal: To create a simple hangman game

#initial setup

#create a list of guessed words

def newGame():
    global guessedList
    global guesses
    global gameOver
    global wordList
    global gameWord
    global gameBoard
    global buttText

    guessedList = list()
    guesses = 10
    gameOver = False

    #create a list of words and choose one for the game
    wordList = ["goat", "duck", "chinchilla", "banana"]
    R.shuffle(wordList)
    gameWord = wordList[0]
    gameBoard = []
    for let in gameWord:
        gameBoard.append("_")

    #reset board
    try:
        subButton['text'] = "Submit"
        guessRemain['text'] = "Guesses Remaining: 10"
        guessesMade['text'] = ""
        word_display['text']= gameBoard
        guessChar.set("")
        user_guess.focus()
    except:
        pass

#function for updating the output:
def usrSubmit():
    global guesses
    global gameOver
    global gameBoard

    #check if player has won
    #start a new game if they have
    if gameOver == True:
        newGame()
        return None

    #check for loss

    entry = guessChar.get()
    guessChar.set("")
    print(entry)
    if entry in guessedList:
        return None
    else:
        guessedList.append(entry)
        guesses -= 1

    gameBoard = []
    for char in gameWord:
        if char in guessedList:
            gameBoard.append(char)
            print(gameBoard)
        else:
            gameBoard.append("_")
            print(gameBoard)


    guessesMade['text']= guessedList
    guessRemain['text']= "Guesses Remaining: " + str(guesses)
    word_display['text']=gameBoard
    user_guess.focus()
    #check for victory, else continue game
    if gameWord == "".join(gameBoard):
        gameOver = True
        guessesMade['text'] ="You Won!"
        subButton['text']="Play Again"
        return None
    elif guesses == 0:
        gameOver = True
        guessesMade['text'] = "You Lose!"
        subButton['text']= "Play Again"
        word_display['text']= gameWord

##start the game
newGame()

#gui
root = Tk()
root.title("Hangman")
mainframe = ttk.Frame(root, padding=10) #need to define the size of it
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(1,pad=100)
#create an area to display the word being guessed
word_display = ttk.Label(mainframe, text=gameBoard,padding="40 10 40 0", font="Helvetica 20", justify = "center")
word_display.grid(column=0,row=0,columnspan=3)
#create an area to display letters that have been guessed

guessesMade = ttk.Label(mainframe, text= "abcdefghijklmnopqrstuvwxyz",font=20, padding="0 10 0 10")
guessesMade.grid(column=0,row=1, columnspan=3)

#create an area to display number of guesses remaining
guessRemain = ttk.Label(mainframe, text= "Guesses Remaining: 10")
guessRemain.grid(column=0,row=2)
#create an input area that for the user to submit guesses
guessChar = StringVar()
user_guess = ttk.Entry(mainframe, width=10, textvariable = guessChar)
user_guess.grid(column=1, row=2)
user_guess.focus()
#create a button for user submissions or whatever
#ideally this button would sit near the entry
subButton = ttk.Button(mainframe, text="Submit",command=usrSubmit)
subButton.grid(column=2,row=2, ipadx=2)
root.bind("<Return>", usrSubmit)

root.mainloop()
