#a simple tictactoe game
#that draws a board on the terminal
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
        self.board = [ #maybe need self.board
        [" "," "," "],
        [" "," "," "],
        [" "," "," "],
        ]
        self.running = True
        gui.ticTacGui(self)
        self.mainloop()

    def printBoard(self):
        pass
    #     dex = 1
    #     print()
    #     for row in self.board:
    #         print("{:}: {:^5}|{:^5}|{:^5}".format(dex,*row))
    #         if dex == 3: #if we're printing row 3, skip the next step
    #             continue
    #         dex += 1
    #         print(" "*3 + "-"*17)
    #     print(" " * 20)
    #     print("   {:^5} {:^5} {:^5}".format("A","B","C"))

    def getUserInput(self):
        #return true or false depending on whether guess was valid?
        #either keep that in this function or make that part of the
        #main logic
        validGuess = False
        while validGuess == False:
            userInput = input("Enter column and row (ex. 'C1'):")
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

    def botChoice(self):
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
        #print an appropriate message
        if winner == None:
            fullLines = 0
            for row in self.board:
                if " " not in row:
                    fullLines += 1
            if fullLines == 3:
                winner = "D"
                self.running = False
                print("It's a draw.")
            else:
                return None
        elif winner == "X":
            print("Congratulations, player. You win")
            self.running = False
        elif winner == "O":
            print("You lost to a really, really dumb robot.")
            self.running = False

    def mainloop(self):
        self.printBoard()
        while self.running == True:
            self.getUserInput()
            if not self.running: break
            self.botChoice()

ticTacToe()
