import urllib.request
from threading import Timer

coin = input('Digite o nome completo da moeda que deseja acompanhar: ')
coin = (coin.replace(" ", "-")).lower()
min = input('Digite o valor para comparação: ')

print('Loading...')

pastPrice = ''

def getCoinValue():
    page = urllib.request.urlopen('https://coinmarketcap.com/currencies/' + coin + '/')
    page = str(page.read())
    global pastPrice

    firstLocation = page.find('<div class="sc-16r8icm-0 kjciSH priceTitle">')
    finalLocation = page.index('</div>', firstLocation)
    priceLocation = page.index('$', firstLocation)

    if page[priceLocation:finalLocation] != pastPrice:
        print('--------------------')
        print((coin.replace("-", " ")).capitalize())
        print('Valor atual: ' + page[priceLocation:finalLocation])

    Timer(10.0, getCoinValue).start()
    pastPrice = page[priceLocation:finalLocation]


Timer(1, getCoinValue).start()

