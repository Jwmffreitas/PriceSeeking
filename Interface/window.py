from tkinter import *
import urllib.request
from threading import Timer
import winsound
from datetime import datetime

window = Tk()


def btn_clicked():
    Timer(1, getCoinValue).start()
    b0["state"] = "disabled"


def clearCanvas():
    canvas2.delete('all')


def getCoinValue():
    min = coinPrice.get()
    coin = coinName.get()
    coin = (coin.replace(" ", "-")).lower()
    page = urllib.request.urlopen('https://coinmarketcap.com/currencies/' + coin + '/')
    page = str(page.read())

    clearCanvas()

    smallLocation1 = page.find('<small>')
    smallLocation2 = page.index('</small>', smallLocation1)
    smallLocation3 = page.index('(', smallLocation1)

    small = page[smallLocation3 + 9:smallLocation2 - 9]


    firstLocation = page.find('<div class="sc-16r8icm-0 kjciSH priceTitle">')
    finalLocation = page.index('</div>', firstLocation)
    priceLocation = page.index('$', firstLocation)

    price = page[priceLocation + 1:finalLocation]

    lastRefresh = datetime.now()

    canvas2.create_text(
    360, 15,
    text="Última atualização: " + lastRefresh.strftime("%d/%m/%Y, %H:%M:%S"),
    fill="#000000",
    font=("None", int(10.0)))

    canvas2.create_text(
        80, 50,
        text=small.upper(),
        fill="#000000",
        font=("None", int(34.0)))

    canvas2.create_text(
        180, 119,
        text="Valor atual: ",
        fill="#000000",
        font=("None", int(18.0)))

    if price.replace(",", "") <= min:
        winsound.PlaySound("../lightsaber.wav", winsound.SND_ASYNC)
        canvas2.create_text(
            325, 118,
            text=page[priceLocation:finalLocation],
            fill="green",
            font=("None", int(22.0)))
    else:
        canvas2.create_text(
            325, 118,
            text=page[priceLocation:finalLocation],
            fill="#000000",
            font=("None", int(22.0)))

    canvas2.create_text(
        100, 200,
        text="Desejado:",
        fill="#000000",
        font=("None", int(14.0)))

    canvas2.create_text(
        215, 200,
        text="$" + min,
        fill="#000000",
        font=("None", int(20.0)))

    Timer(10.0, getCoinValue).start()


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

canvas2 = Canvas(
    window,
    bg="#ffffff",
    height=236,
    width=492,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas2.place(x=508, y=364)


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
    command=btn_clicked,
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
