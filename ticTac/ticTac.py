#a simple tictactoe game
#sends information to ticTacgui
import random as rnd
import ticTacgui as gui

class ticTacToe:
    #class variables
    validCol = {
    'a': 0, 'A': 0,
    'b': 1, 'B': 1,
    'c': 2, 'C': 2
    }
    validRow = [1,2,3]

    #constructor
    def __init__(self):
        self.board = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "],
        ]
        self.running = True
        self.interf = gui.ticTacGui(self)
        self.mainloop()

    def validateGuess(self, guess):
        #return true or false depending on whether guess was valid?
        #either keep that in this function or make that part of the
        #main logic
        validGuess = False
        while validGuess == False:
            if (len(userInput) > 0
            and userInput[0] in ticTacToe.validCol
            and int(userInput[1]) in ticTacToe.validRow):
                column = self.validCol[userInput[0]]
                row = int(userInput[1]) - 1
                if self.board[row][column] != " ":
                    print("Space already full. Try again")
                else:
                    validGuess = True
                    self.board[row][column] = "X"
                    self.printBoard()
            else:
                print("Invalid input. Try again")
        self.checkBoard()

    def receiveMove(self):
        validGuess = False
        print("Beep boop...bot is making a decision.")
        while validGuess == False:
            col = rnd.randint(0,2)
            row = rnd.randint(0,2)
            if self.board[row][col] != " ": #infinite loop possible
                #add: check for gameover condition
                continue
            else:
                validGuess = True
                self.board[row][col] = "O"
                self.printBoard()
        self.checkBoard()
    def checkBoard(self):    #check for gameOver condition
        winner = None
        #is there a vertical win?
        for pair in enumerate(self.board[0]):
            if pair[1] == self.board[1][pair[0]] == self.board[2][pair[0]]:
                winner = pair[1]
                break
        #is there a horizontal win?
        for list in self.board:
            if list.count("X") == 3 or list.count("O") == 3:
                winner = list[0]
                break
        #is there a diagonal win?
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]
        or self.board[0][2] == self.board[1][1] == self.board[2][0]):
            winner = self.board[1][1]
        #if no winner, check for draw, else return None
        if winner == None:
            fullLines = 0
            for row in self.board:
                if " " not in row:
                    fullLines += 1
            if fullLines == 3:
                winner = "D"
                self.running = False
            else:
                return None
        elif winner == "X":
            self.running = False
        elif winner == "O":
            self.running = False

    def mainloop(self):
        pass

ticTacToe()
