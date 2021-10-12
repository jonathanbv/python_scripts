#script to run in interactive mode for testing
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("~Test and Debugging~")
mainframe = ttk.Frame(root, padding=10) #need to define the size of it
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
