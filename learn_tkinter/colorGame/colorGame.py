import tkinter as tk
import random

#potential improvements:
#allow restarting
#high score

#list of colors
colors = ["Red", "Blue", "Green", "Pink", "Black",
           "Yellow", "Orange", "White", "Purple", "Brown"]
score = 0
timeLeft = 30

#fxn to start game
def startGame(event):
    if timeLeft == 30:
        countdown()

    nextColor()

#Function to display and choose next color
def nextColor():

    global colors
    global score

    #if game in progress
    if timeLeft > 0:

        #make text entry box active
        e.focus_set()

        #if color typed equals
        #text colors
        if e.get().lower() == colors[1].lower():

            score += 1

        #clear entry box
        e.delete(0, tk.END)

        random.shuffle(colors)

        #change the color by randomizing
        label.config(fg = str(colors[1]), text = str(colors[0]))

        #update score
        scoreLabel.config(text = "Score: " + str(score))

#countdown timer function
def countdown():

    global timeLeft

    #if game is in play
    if timeLeft > 0:
        #decrement timer
        timeLeft -= 1
        #update the time label
        timeLabel.config(text = "Time left: "
                                + str(timeLeft))
        #run the function again after 1 second
        timeLabel.after(1000, countdown) #why call it on timeLabel?

#Driver Code
#create a GUI window
root = tk.Tk()
root.title("COLOR LORDS")
root.geometry("375x200")

#add instructions label
instructions = tk.Label(root, text = "Type in the color"
                            " of the words, and not the word text!",
                                            font = ('Helvetica', 12))
instructions.pack()
scoreLabel = tk.Label(root, text = "Press enter to start",
                                    font = ('Helvetica', 12))
scoreLabel.pack()
timeLabel = tk.Label(root, text = "Time left: " +
                            str(timeLeft), font = ('Helvetica', 12))
timeLabel.pack()
label = tk.Label(root, font = ('Helvetica', 60))
label.pack()

e = tk.Entry(root)
#start game when enter is pressed
root.bind('<Return>', startGame)
e.pack()

#set focus on the entry box
e.focus_set()

#start the gui
root.mainloop()
