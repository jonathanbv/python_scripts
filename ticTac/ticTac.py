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
        if self.board[move[0]][move[1]] == " ":
            self.board[move[0]][move[1]] = "X"
            self.interf.drawPlayer(move)
            print("In getplayermove, currents status of checkBoard is :",self.checkBoard())
            if self.checkBoard() == None:
                self.botMove()

    def botMove(self):
        #have the computer make a valid move
        #then draw it
        validGuess = False
        while validGuess == False and not self.checkBoard():
            time.sleep(0.25)
            print("New while iteration")
            row = rnd.randint(0,2)
            col = rnd.randint(0,2)
            print("Bot guess is: row:{} column{}".format(row,col))
            if self.board[row][col] == " ":
                validGuess = True
                print("Bot made a valid guess. Printing...")
                self.board[row][col] = "O"
                self.interf.drawBot((row,col))
            else:
                print("Botguess was occupied, continuing.")
                continue
        print("Hello from outside the while loop.")

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
            return(winner)
    def resetBoard(self):
        for list in self.board:
            list = [" "," "," "]
        print(self.board)
        self.running = True
        print(self.running)

x = ticTacToe()
