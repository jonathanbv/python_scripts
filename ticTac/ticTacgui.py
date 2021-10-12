from tkinter import *
from tkinter import ttk

class ticTacGui:

    def __init__(self, ticTac):
        self.logic = ticTac
        self.root = Tk()
        self.root.title("Tic Tac Teaux")
        self.mainframe = ttk.Frame(self.root, padding=10) #need to define the size of it
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        #self.mainframe.columnconfigure(1,pad=100)
        self.build()

    def build(self):
        #create instructions at top
        self.instruction = ttk.Label(self.mainframe, text="Click a blank square to place an 'X'")
        self.instruction.grid(column=1,row=0, sticky=(W,E))

        #create 9 boxes for Xs and Os
        gameBoxes = [
        Canvas(self.mainframe, width=50, height=50, bg="white")
        for i in range(1,10)]
        #place the boxes
        bxCol = 0
        bxRow = 1
        for box in gameBoxes:
            print(bxCol,bxRow)
            box.grid(column=bxCol, row=bxRow)
            box.bind("<Button-1>", self.fillBox("X"))
            if bxCol < 2:
                bxCol += 1
            else:
                bxCol = 0
                bxRow += 1

        #create a button to reset game
        self.gameButton = ttk.Button(self.mainframe, text="Reset",command=self.reset)
        self.gameButton.grid(column=1,row=4, ipadx=2)
        self.root.mainloop()

    def fillBox(self,char):
        pass
    def reset(self):
        pass

ticTacGui(None)
