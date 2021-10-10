#a simple tictactoe game
#that draws a board on the terminal
import random as rnd
board = [
[" "," "," "],
[" "," "," "],
[" "," "," "],
]
validCol = {
'a': 0, 'A': 0,
'b': 1, 'B': 1,
'c': 2, 'C': 2
}
validRow = [1,2,3]
running = True
#draw the board
def printBoard():
    dex = 1
    print()
    for row in board:
        print("{:}: {:^5}|{:^5}|{:^5}".format(dex,*row))
        if dex == 3: #if we're printing row 3, skip the next step
            continue
        dex += 1
        print(" "*3 + "-"*17)
    print(" " * 20)
    print("   {:^5} {:^5} {:^5}".format("A","B","C"))

def getUserInput():
    #return true or false depending on whether guess was valid?
    #either keep that in this function or make that part of the
    #main logic
    validGuess = False
    while validGuess == False:
        userInput = input("Enter column and row (ex. 'C1'):")
        if (len(userInput) > 0
        and userInput[0] in validCol
        and int(userInput[1]) in validRow):
            column = validCol[userInput[0]]
            row = int(userInput[1]) - 1
            if board[row][column] != " ":
                print("Space already full. Try again")
            else:
                validGuess = True
                board[row][column] = "X"
                printBoard()
        else:
            print("Invalid input. Try again")
    checkBoard()

def botChoice():
    validGuess = False
    print("Beep boop...bot is making a decision.")
    while validGuess == False:
        col = rnd.randint(0,2)
        row = rnd.randint(0,2)
        if board[row][col] != " ": #infinite loop possible
            #add: check for gameover condition
            continue
        else:
            validGuess = True
            board[row][col] = "O"
            printBoard()
    checkBoard()
def checkBoard():    #check for gameOver condition
    global running
    winner = None
    #is there a vertical win?
    for pair in enumerate(board[0]):
        if pair[1] == board[1][pair[0]] == board[2][pair[0]]:
            winner = pair[1]
            break
    #is there a horizontal win?
    for list in board:
        if list.count("X") == 3 or list.count("O") == 3:
            winner = list[0]
            break
    #is there a diagonal win?
    if (board[0][0] == board[1][1] == board[2][2]
    or board[0][2] == board[1][1] == board[2][0]):
        winner = board[1][1]
    #if no winner, check for draw, else return None
    #print an appropriate message
    if winner == None:
        fullLines = 0
        for row in board:
            if " " not in row:
                fullLines += 1
        if fullLines == 3:
            winner = "D"
            running = False
            print("It's a draw.")
        else:
            return None
    elif winner == "X":
        print("Congratulations, player. You win")
        running = False
    elif winner == "O":
        print("You lost to a really, really dumb robot.")
        running = False

def mainloop():
    printBoard()
    while running == True:
        getUserInput()
        if not running: break
        botChoice()

mainloop()
