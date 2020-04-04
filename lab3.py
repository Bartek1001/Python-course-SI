import requests
import json
import numpy


x = "https://bitbay.net/API/Public/BTCUSD/orderbook.json"

def print_bid_ask(x):
    response = requests.get(x)
    data = response.json()

    print('BIDS OFFERS','\n')

    for i in range(100):
        print(data['bids'][i])

    print('\n','ASKS OFFERS','\n')

    for i in range(100):
        print(data['asks'][i])

    return

print_bid_ask(x)




#bid - najwyższa oferta kupna.
#ask - najniższa oferta sprzedaży.

response1 = requests.get("https://api.bitfinex.com/v1/pubticker/btcusd")
response2 = requests.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")
data1 = response1.json()
data2 = response2.json()
bid_2 = float(data2['bid'])
ask_2 = float(data2['ask'])
bid_1 = float(data1['bid'])
ask_1 = float(data1['ask'])

def best_bid():
    if bid_1 > bid_2:
        result = 'bitbay.net'
    elif bid_1 < bid_2:
        result = 'bitfinex.com'
    elif bid_1 == bid_2:
        result = 'both bitbay.net and bitfinex.com'
    return result

def best_ask():
    if bid_1 > bid_2:
        result = 'bitfinex.com'
    elif bid_1 < bid_2:
        result = 'bitbay.net'
    elif bid_1 == bid_2:
        result = 'both bitbay.net and bitfinex.com'
    return result

print("Bitbay","Bid:",bid_2,"Ask:",ask_2)
print("Bitfinex","Bid:",bid_1,"Ask:",ask_1)
print("Currently the", best_bid(), "exchange market is better for buying whilst", best_ask(),"is better for selling")