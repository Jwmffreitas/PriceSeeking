import urllib.request
from threading import Timer
import winsound
import os
from datetime import datetime

coin = input('Digite o nome completo da moeda que deseja acompanhar: ')
coin = (coin.replace(" ", "-")).lower()
min = input('Digite o valor desejado para compra: ')

print('Loading...')

pastPrice = ''


def getCoinValue():
    global pastPrice
    page = urllib.request.urlopen('https://coinmarketcap.com/currencies/' + coin + '/')
    page = str(page.read())

    firstLocation = page.find('<div class="sc-16r8icm-0 kjciSH priceTitle">')
    finalLocation = page.index('</div>', firstLocation)
    priceLocation = page.index('$', firstLocation)

    price = page[priceLocation + 1:finalLocation]

    lastRefresh = datetime.now()

    os.system("cls")
    print('--------------------')
    print((coin.replace("-", " ")).capitalize())
    print('Valor desejado: $' + min)
    print('Valor atual: ' + page[priceLocation:finalLocation])
    print(lastRefresh.strftime("%d/%m/%Y, %H:%M:%S"))
    print('--------------------')
    if price <= min:
        winsound.PlaySound("lightsaber.wav", winsound.SND_ASYNC)
        print("COMPRA LIBERADA!")
    Timer(10.0, getCoinValue).start()
    pastPrice = price


Timer(1, getCoinValue).start()

