from tkinter import *

root = Tk()

root.geometry("600x300")

# Variables
coin = ''
min = ''


# Creating a texts
title = Label(root, text="PriceSeeking")
title.config(font=("Arial", 40))
question1 = Label(root, text="Digite o nome completo da moeda: ")
question1.config(font=20)
question2 = Label(root, text="Digite o valor desejado para compra: ")
question2.config(font=20)

# Creating some inputs
coinName = Entry(root, width=50, borderwidth=2)
textMinValue = Entry(root, width=50, borderwidth=2)

# Show all in the screen
title.grid(row=0, column=1, pady=10)
question1.grid(row=1, column=0, padx=5, pady=1)
coinName.grid(row=1, column=1)
question2.grid(row=2, column=0, padx=5, pady=0)
textMinValue.grid(row=2, column=1)



# Creating a Button
myButton = Button(root, text="Acompanhar", padx=113, fg="white", bg="black")

# Shoving it onto the screen
myButton.grid(row=3, column=1)

root.mainloop()
