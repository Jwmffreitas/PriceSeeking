from tkinter import *

root = Tk()


def myClick():
    myLabel2 = Label(root, text="My name is  John!")
    myLabel2.grid(row=1, column=0)


# Creating a Label Widget
myLabel = Label(root, text="Hello World!")

# Creating a Button
myButton = Button(root, text="Click Me!", padx=50, command=myClick, fg="white", bg="black")

# Shoving it onto the screen
myLabel.grid(row=0, column=0)
myButton.grid(row=2, column=0)

root.mainloop()
