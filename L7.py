import requests
import time
import datetime
import random
import matplotlib.pyplot as plt
import numpy
import statistics

def data(crypto):
    day = int(input("Podaj dzień:"))
    month = int(input("Podaj miesiąc:"))
    year = int(input("Podaj rok:"))
    today = str(datetime.date.today())
    past = str(datetime.date(year, month, day))
    date_timestamp_today = time.mktime(datetime.datetime.strptime(today, "%Y-%m-%d").timetuple())
    date_timestamp_past = time.mktime(datetime.datetime.strptime(past, "%Y-%m-%d").timetuple())
    crypto = requests.get(
        "https://poloniex.com/public?command=returnChartData&currencyPair=BTC_{}&start={}&end={}&period=86400".format(crypto, date_timestamp_past, date_timestamp_today))
    return crypto.json()

def prediction(crypto):
    volumen = []

    for i in crypto:
        volumen.append(i['volume'])

    del volumen[0]

    lower_volumen = 0
    higher_volumen = 0
    positive_difference = []
    negative_difference = []

    for i in range(len(volumen)-1):
        if volumen[i] >= volumen[i+1]:
            lower_volumen += 1
            negative = (volumen[i] - volumen[i+1])/(volumen[i])
            negative_difference.append(negative)
        elif volumen[i] < volumen[i+1]:
            higher_volumen += 1
            positive = (volumen[i+1] - volumen[i]) / (volumen[i])
            positive_difference.append(positive)

    result = [0] * (len(volumen))
    result100 = [0] * (len(volumen))
    number2 = higher_volumen

    for j in range(100):
        for i in range(len(volumen)):
            number1 = random.randint(1,lower_volumen + higher_volumen)

            if number1 >= 1 and number1 <= number2:
                result[i] = numpy.mean(volumen) + (numpy.mean(volumen) * random.choice(positive_difference))

            elif number1 > number2 and number1 <= (lower_volumen + higher_volumen):
                result[i] = numpy.mean(volumen) - (numpy.mean(volumen) * random.choice(negative_difference))

        for k in range(len(result)):
            result100[k] += result[k]

    for h in range(len(result)):
        result100[h] = result100[h]/100

    result_mean = numpy.mean(result)
    result_median = statistics.median(result)
    result_stdev = statistics.stdev(result)

    result100_mean = numpy.mean(result100)
    result100_median = statistics.median(result100)
    result100_stdev = statistics.stdev(result100)

    today = datetime.datetime.now()
    future = []
    past = []

    for i in range(len(result)):
        next_day = today + datetime.timedelta(i+1)
        future.append(next_day)

    for i in range(len(volumen)):
        yesterday = today - datetime.timedelta(i)
        past.append(yesterday)

    plt.plot(future,result)
    plt.plot(past,volumen)
    plt.plot(future,result100)
    plt.title("Zielony to średnia z przeprowadzonych 100 symulacji, niebieski to przeprowadzona 1 symulacja, pomarańczowy to dane historyczne")
    plt.show()

    return result_mean, result_median, result_stdev, result100_mean, result100_median, result100_stdev

name = input("Podaj nazwę ETC lub LTC lub XRP:")
crypto=data(name)
mean,median,stdev,mean100,median100,stdev100 = prediction(crypto)
print(mean,median,stdev)
print(mean100,median100,stdev100)