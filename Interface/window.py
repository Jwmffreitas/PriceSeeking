from tkinter import *


window = Tk()


window.geometry("1000x600")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    764.0, 155.0,
    image=entry0_img)

coinName = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

coinName.place(
    x=636.0, y=138,
    width=256.0,
    height=32)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    764.0, 230.0,
    image=entry1_img)

coinPrice = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

coinPrice.place(
    x=636.0, y=213,
    width=256.0,
    height=32)

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    #command=btn_clicked,
    relief="flat")

b0.place(
    x=626, y=266,
    width=276,
    height=39)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    500.0, 300.0,
    image=background_img)



window.resizable(False, False)
window.mainloop()
