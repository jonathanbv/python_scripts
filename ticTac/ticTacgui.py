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
        self.mainframe.rowconfigure(4,pad=5)
        self.mainframe.rowconfigure(0,pad=5)
        self.build()

    def build(self):
        #create instructions at top
        self.instruction = ttk.Label(self.mainframe, text="Click an empty box to place an 'x'", anchor="center")
        self.instruction.grid(column=0,row=0, columnspan=3, sticky=(W,E))

        #create 2d list that holds 3 rows of 3 boxes
        #Next step: this needs to be a list of tuples to make it easier
        #to pass index information to the logic portion of game
        self.gameBoxes = []
        for i in range(0,3):
            self.gameBoxes.append([Canvas(self.mainframe, width=75, height=75, bg="white")
            for j in range(0,3)])

        #place the boxes
        for rowDex, row in enumerate(self.gameBoxes):
            for colDex, box in enumerate(row):
                box.grid(column=colDex, row=rowDex + 1, padx=5, pady=5)
                box.bind("<Button-1>", self.fillBox)

        #create a button to reset game
        self.gameButton = ttk.Button(self.mainframe, text="Reset",command=self.reset)
        self.gameButton.grid(column=0,row=4,columnspan=3, sticky=(W,E), ipadx=2)
        self.root.mainloop()

    def fillBox(self, event):
        parent = event.widget
        parent.create_line(0, 0, 75, 75, width=5)
        parent.create_line(75, 0, 0, 75, width=5)
        print(self.gameBoxes[0].index(parent))

    def reset(self, event):
        print("OMG! Someone called the reset method")

#x = ticTacGui(None)
