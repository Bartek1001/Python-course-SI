import requests
import time

while(True):
    USD_wallet = [20000,20000,20000,20000]     #Bitfinex,Bitbay,Bitstamp,Blockchain
    BTC_wallet = [2.5,2.5,2.5,2.5]             #Bitfinex,Bitbay,Bitstamp,Blockchain

    exchange_market = ["Bitfinex","Bitbay","Bitstamp","Blockchain"]

    def bid_ask():
        bitfinex = requests.get("https://api.bitfinex.com/v1/pubticker/btcusd")
        bitbay = requests.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")
        bitstamp = requests.get('https://www.bitstamp.net/api/ticker')
        blockchain = requests.get("https://blockchain.info/ticker")

        data1 = bitfinex.json()
        data2 = bitbay.json()
        data3 = bitstamp.json()
        data4 = blockchain.json()

        bid_1 = float(data1['bid'])
        ask_1 = float(data1['ask'])
        bid_2 = float(data2['bid'])
        ask_2 = float(data2['ask'])
        bid_3 = float(data3['bid'])
        ask_3 = float(data3['ask'])
        bid_4 = float(data4["USD"]["buy"])
        ask_4 = float(data4["USD"]["sell"])

        bid_list = [bid_1,bid_2,bid_3,bid_4]
        ask_list = [ask_1,ask_2,ask_3,ask_4]

        return bid_list,ask_list

    taker = [0.002,0.0025,0.0025,0.0024]

    bid_list,ask_list = bid_ask()

    maximum_bid = max(bid_list)
    minimum_ask = min(ask_list)

    a=0
    for i in range(len(bid_list)):
        if maximum_bid == bid_list[i]:
            a=i

    b=0
    for i in range(len(ask_list)):
        if minimum_ask == ask_list[i]:
            b=i

    BTC = 0.1

    buy = BTC * maximum_bid * (1+taker[a])
    sell = BTC * minimum_ask * (1+taker[b])
    profit = sell - buy

    if profit>0:
        if BTC_wallet[a] >= BTC and USD_wallet[b] >= sell:
            USD_wallet[a] += buy
            BTC_wallet[a] -= BTC
            USD_wallet[b] -= sell
            BTC_wallet[b] += BTC
            print("Na giełdzie",exchange_market[a],"można kupić 0.1 BTC za USD po kursie",maximum_bid,"i sprzedać na giełdzie",exchange_market[b],"po kursie",minimum_ask,", zyskując",profit,"USD.")
        else:
            print("Nie masz wystarczająco środków na giełdzie")
    elif profit<=0:
        print("Arbitraż nie przyniesie zysku")

    time.sleep(5)