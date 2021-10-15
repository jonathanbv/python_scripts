#a simple tictactoe game
#sends information to ticTacgui
import random as rnd
import ticTacgui as gui
import time

class ticTacToe:
    #constructor
    def __init__(self):
        self.board = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "],
        ]
        self.running = True
        self.interf = gui.ticTacGui(self)

    def getPlayerMove(self, move):
        #guess is a tuple in the form (row, col)
        if self.checkBoard() == None:
            if self.board[move[0]][move[1]] == " ":
                self.board[move[0]][move[1]] = "X"
                self.interf.drawPlayer(move)
                if self.checkBoard() == None:
                    self.botMove()

    def botMove(self):
        #more efficient bot moves could come from iterating through board
        #random causes computer to make a bunch of invalid guesses
        #have the computer make a valid move
        #then draw it
        validGuess = False
        for rowDex, row in enumerate(self.board,0):
            print("in bot outer for loop")
            if "O" in row and " " in row and "X" not in row: #go for a horizontal win
                col = row.index(" ") #will always fill the leftmost blank...
                self.board[rowDex][col] = "O"
                validGuess = True
                self.interf.drawBot((rowDex,col))
                break
            elif rowDex == 0: #check for good moves based on row 0 values
                print("checking rowDex == 0...")
                for colDex, space in enumerate(row,0):
                    if (space == "O" and self.board[rowDex+1][colDex] == "O"
                    or self.board[rowDex+1][colDex] == " " and self.board[rowDex+2][colDex] == "0"
                    or self.board[rowDex+2][colDex] == " "):
                        if self.board[rowDex+2][colDex] == " ":
                            self.board[rowDex+2][colDex] = "O"
                            validGuess = True
                            self.interf.drawBot((rowDex+2, colDex))
                            break
                break
            elif rowDex == 1:
                pass
            elif rowDex == 2:
                pass
        #when all else fails, just pick something random
        while validGuess == False and not self.checkBoard():
            print("in bot while loop")
            row = rnd.randint(0,2)
            col = rnd.randint(0,2)
            if self.board[row][col] == " ":
                validGuess = True
                self.board[row][col] = "O"
                self.interf.drawBot((row,col))

        if validGuess: self.checkBoard()

    def checkBoard(self):
        #check for gameOver condition
        #Return None, "X", "O", or "D"
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

        if winner == " ":
            return None
        else:
            self.running = False
            if winner == "X":
                self.interf.instruction["text"] = "You won!"
            elif winner == "O":
                self.interf.instruction["text"] = "You lost to a really dumb robot."
            elif winner == "D":
                self.interf.instruction["text"] = "It's a draw. Wow."
            return(winner)
    def resetBoard(self):
        clearRow = [" ", " ", " "]
        self.interf.instruction["text"] = "Click an empty box to place an 'x'"
        for list in self.board:
            list.clear()
            for item in clearRow:
                list.append(item)
        self.running = True

x = ticTacToe()
x.interf.root.mainloop()
