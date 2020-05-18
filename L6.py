import requests
import csv

all_crypto = ['BTC','ETH','XRP','LTC','BCC']

def data():
    BTC = requests.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")
    ETH = requests.get("https://bitbay.net/API/Public/ETHUSD/ticker.json")
    XRP = requests.get("https://bitbay.net/API/Public/XRPUSD/ticker.json")
    LTC = requests.get("https://bitbay.net/API/Public/LTCUSD/ticker.json")
    BCC = requests.get("https://bitbay.net/API/Public/BCCUSD/ticker.json")

    return BTC.json(),ETH.json(),XRP.json(),LTC.json(),BCC.json()

def wallet():

    crypto_name = your_crypto()
    crypto_value = []
    crypto_price = []

    for i in range(len(crypto_name)):
        print("Ile posiadasz",crypto_name[i],"?")
        crypto_value.append(float(input()))
        while crypto_value[i] < 0:
            print("Wprowadzono niepoprawne dane, ile posiadasz",crypto_name[i],"?")
            x = (float(input()))
            crypto_value[i] = x
        print("Po jakiej cenie kupiłeś/aś",crypto_name[i],"? (USD)")
        crypto_price.append(float(input()))

    save_data(crypto_name,crypto_value)

    return crypto_name,crypto_value,crypto_price

def your_crypto():
    crypto_name = ''
    your_wallet = []
    i=0
    while i < 5:
        print('Wybierz swoją kryptowalute (BTC/ETH/XRP/LTC/BCC), jeśli chcesz zakończyć wciśnij q:')
        crypto_name = str(input())
        if crypto_name == 'q' or crypto_name == 'Q':
            break
        elif crypto_name.upper() not in ['BTC','ETH','XRP','LTC','BCC']:
            print('Niepoprawne dane. Wpisz BTC lub ETH lub XRP lub LTC lub BCC.')
        elif crypto_name.upper() in ['BTC','ETH','XRP','LTC','BCC']:
            your_wallet.append(crypto_name.upper())
    return your_wallet

def open_wallet():
    with open('wallet.csv') as csvfile:
        reader = csv.reader(csvfile,delimiter = ',')
        for row in reader:
            print(row[0],row[1])

def save_data(a,b):
    with open('wallet.csv', 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([a,b])
    print("Dane zapisane")

def all_crypto_money_percentage_and_USD(crypto_name,crypto_value,crypto_price):

    data_BTC, data_ETH, data_XRP, data_LTC, data_BCC = data()

    bid_BTC = float(data_BTC['bid'])
    bid_ETH = float(data_ETH['bid'])
    bid_XRP = float(data_XRP['bid'])
    bid_LTC = float(data_LTC['bid'])
    bid_BCC = float(data_BCC['bid'])

    max_BTC = float(data_BTC['max'])
    max_ETH = float(data_ETH['max'])
    max_XRP = float(data_XRP['max'])
    max_LTC = float(data_LTC['max'])
    max_BCC = float(data_BCC['max'])

    min_BTC = float(data_BTC['min'])
    min_ETH = float(data_ETH['min'])
    min_XRP = float(data_XRP['min'])
    min_LTC = float(data_LTC['min'])
    min_BCC = float(data_BCC['min'])

    crypto_bid = [bid_BTC, bid_ETH, bid_XRP, bid_LTC, bid_BCC]
    crypto_max = [max_BTC, max_ETH, max_XRP, max_LTC, max_BCC]
    crypto_min = [min_BTC, min_ETH, min_XRP, min_LTC, min_BCC]

    USD_all_crypto = []

    for i in range(len(crypto_name)):
        if crypto_name[i] == all_crypto[0]:
            percentage_change = ((crypto_max[0]/crypto_min[0])-1)*100
            if percentage_change > 0:
                print("Zysk na", crypto_name[i], "w ciągu 24h wynosi", percentage_change, "%")
            elif percentage_change < 0:
                print("Spadek na", crypto_name[i], "w ciągu 24h wynosi", percentage_change, "%")
            else:
                print("Nie odnotowano wzrostu ani spadku", crypto_name[i], "w ciągu 24h.")

            USD_change = crypto_bid[0] - crypto_price[i]
            USD_all_crypto.append(USD_change)
            if USD_change > 0:
                print("Potencjalny zysk na", crypto_name[i], "od ostatniego kupna wynosi", USD_change, "USD")
            elif USD_change < 0:
                print("Potencjalny spadek na", crypto_name[i], "od ostatniego kupna wynosi", USD_change, "USD")
            else:
                print("Cena bez zmian na", crypto_name[i])
        elif crypto_name[i] == all_crypto[1]:
            percentage_change = ((crypto_max[1] / crypto_min[1]) - 1) * 100
            if percentage_change > 0:
                print("Zysk na", crypto_name[i], "w ciągu 24h wynosi", percentage_change, "%")
            elif percentage_change < 0:
                print("Spadek na", crypto_name[i], "w ciągu 24h wynosi", percentage_change, "%")
            else:
                print("Nie odnotowano wzrostu ani spadku", crypto_name[i], "w ciągu 24h.")

            USD_change = crypto_bid[1] - crypto_price[i]
            USD_all_crypto.append(USD_change)
            if USD_change > 0:
                print("Potencjalny zysk na", crypto_name[i], "od ostatniego kupna wynosi", USD_change, "USD")
            elif USD_change < 0:
                print("Potencjalny spadek na", crypto_name[i], "od ostatniego kupna wynosi", USD_change, "USD")
            else:
                print("Cena bez zmian na", crypto_name[i])
        elif crypto_name[i] == all_crypto[2]:
            percentage_change = ((crypto_max[2] / crypto_min[2]) - 1) * 100
            if percentage_change > 0:
                print("Zysk na", crypto_name[i], "w ciągu 24h wynosi", percentage_change, "%")
            elif percentage_change < 0:
                print("Spadek na", crypto_name[i], "w ciągu 24h wynosi", percentage_change, "%")
            else:
                print("Nie odnotowano wzrostu ani spadku", crypto_name[i], "w ciągu 24h.")

            USD_change = crypto_bid[2] - crypto_price[i]
            USD_all_crypto.append(USD_change)
            if USD_change > 0:
                print("Potencjalny zysk na", crypto_name[i], "od ostatniego kupna wynosi", USD_change, "USD")
            elif USD_change < 0:
                print("Potencjalny spadek na", crypto_name[i], "od ostatniego kupna wynosi", USD_change, "USD")
            else:
                print("Cena bez zmian na", crypto_name[i])
        elif crypto_name[i] == all_crypto[3]:
            percentage_change = ((crypto_max[3] / crypto_min[3]) - 1) * 100
            if percentage_change > 0:
                print("Zysk na", crypto_name[i], "w ciągu 24h wynosi", percentage_change, "%")
            elif percentage_change < 0:
                print("Spadek na", crypto_name[i], "w ciągu 24h wynosi", percentage_change, "%")
            else:
                print("Nie odnotowano wzrostu ani spadku", crypto_name[i], "w ciągu 24h.")

            USD_change = crypto_bid[3] - crypto_price[i]
            USD_all_crypto.append(USD_change)
            if USD_change > 0:
                print("Potencjalny zysk na", crypto_name[i], "od ostatniego kupna wynosi", USD_change, "USD")
            elif USD_change < 0:
                print("Potencjalny spadek na", crypto_name[i], "od ostatniego kupna wynosi", USD_change, "USD")
            else:
                print("Cena bez zmian na", crypto_name[i])
        elif crypto_name[i] == all_crypto[4]:
            percentage_change = ((crypto_max[4] / crypto_min[4]) - 1) * 100
            if percentage_change > 0:
                print("Zysk na", crypto_name[i], "w ciągu 24h wynosi", percentage_change, "%")
            elif percentage_change < 0:
                print("Spadek na", crypto_name[i], "w ciągu 24h wynosi", percentage_change, "%")
            else:
                print("Nie odnotowano wzrostu ani spadku", crypto_name[i], "w ciągu 24h.")

            USD_change = crypto_bid[4] - crypto_price[i]
            USD_all_crypto.append(USD_change)
            if USD_change > 0:
                print("Potencjalny zysk na", crypto_name[i], "od ostatniego kupna wynosi", USD_change, "USD")
            elif USD_change < 0:
                print("Potencjalny spadek na", crypto_name[i], "od ostatniego kupna wynosi", USD_change, "USD")
            else:
                print("Cena bez zmian na", crypto_name[i])

    x = sum(USD_all_crypto)
    if x > 0:
        print("Potencjalny wzrost ilości zasobów w portfelu o",x,"USD.")
    elif x < 0:
        print("Potencjalny spadek ilości zasobów w portfelu o",x,"USD.")
    else:
        print("Nie odnotowano wzrostu ani spadku ilości zasobów w portfelu.")

while True:
    print("Witamy:\n 1) Otwórz portfel \n 2) Zapisz zmiany w portfelu \n 3) Zmiany w zasobach portfela \n 4) Sprawdź zawartość portfela  \n 5) Wyjście z programu")

    number = int(input("Wybierz opcję:"))

    if number == 1:
        crypto_name, crypto_value, crypto_price = wallet()
    elif number == 2:
        save_data(crypto_name,crypto_value)
    elif number == 3:
        all_crypto_money_percentage_and_USD(crypto_name,crypto_value,crypto_price)
    elif number == 4:
        open_wallet()
    elif number == 5:
        exit("Dziękujemy za skorzystanie z naszej aplikacji.")