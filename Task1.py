import requests

def price(symb,compar_symb=["USD"],exchange=""):
    url="https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}"\
.format(symb.upper(), ','.join(compar_symb).upper())
    if exchange:
        url += '&e={}'.format(exchange)
        getRequest=requests.get(url)
        data=getRequest.json()
        return data

a=price("ETH",exchange="Coinbase")
print(a)