import urllib.request

page = urllib.request.urlopen('https://coinmarketcap.com/currencies/electric-vehicle-direct-currency/')
page = str(page.read())

firstLocation = page.find('<div class="sc-16r8icm-0 kjciSH priceTitle">')
finalLocation = page.index('</div>', firstLocation)
priceLocation = page.index('$', firstLocation)

print(page[priceLocation:finalLocation])

