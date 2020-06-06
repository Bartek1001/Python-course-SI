import requests
import time
import datetime
import random
import matplotlib.pyplot as plt
import numpy
import statistics

def data(crypto):
    crypto1 = crypto

    stop_day = str(datetime.date(2020,5,1))
    start_day = str(datetime.date(2020,4,1))
    date_timestamp_start_day = time.mktime(datetime.datetime.strptime(start_day, "%Y-%m-%d").timetuple())
    date_timestamp_stop_day = time.mktime(datetime.datetime.strptime(stop_day, "%Y-%m-%d").timetuple())
    crypto = requests.get(
        "https://poloniex.com/public?command=returnChartData&currencyPair=BTC_{}&start={}&end={}&period=86400".format(crypto, date_timestamp_start_day, date_timestamp_stop_day))

    stop_day2 = str(datetime.date(2020, 5, 31))
    start_day2 = str(datetime.date(2020, 5, 1))
    date_timestamp_start_day2 = time.mktime(datetime.datetime.strptime(start_day2, "%Y-%m-%d").timetuple())
    date_timestamp_stop_day2 = time.mktime(datetime.datetime.strptime(stop_day2, "%Y-%m-%d").timetuple())
    crypto1 = requests.get(
        "https://poloniex.com/public?command=returnChartData&currencyPair=BTC_{}&start={}&end={}&period=86400".format(crypto1, date_timestamp_start_day2, date_timestamp_stop_day2))
    return crypto.json(),crypto1.json()

def prediction(crypto,crypto1):
    volumen = []

    for i in crypto:
        volumen.append(i['volume'])

    del volumen[0]


    volumen1 = []

    for i in crypto1:
        volumen1.append(i['volume'])

    del volumen1[0]

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
            number1 = random.randint(1, lower_volumen + higher_volumen)

            if number1 >= 1 and number1 <= number2:
                result[i] = numpy.mean(volumen) + (numpy.mean(volumen) * random.choice(positive_difference))

            elif number1 > number2 and number1 <= (lower_volumen + higher_volumen):
                result[i] = numpy.mean(volumen) - (numpy.mean(volumen) * random.choice(negative_difference))

        for k in range(len(result)):
            result100[k] += result[k]

    for h in range(len(result)):
        result100[h] = result100[h] / 100

    result_mean = numpy.mean(result)
    result_median = statistics.median(result)
    result_stdev = statistics.stdev(result)

    result100_mean = numpy.mean(result100)
    result100_median = statistics.median(result100)
    result100_stdev = statistics.stdev(result100)

    volumen1_mean = numpy.mean(volumen1)
    volumen1_median = statistics.median(volumen1)
    volumen1_stdev = statistics.stdev(volumen1)

    start1 = datetime.datetime.strptime("1-04-2020", "%d-%m-%Y")
    end1 = datetime.datetime.strptime("1-05-2020", "%d-%m-%Y")
    date_generated1 = [start1 + datetime.timedelta(days=x) for x in range(0, (end1 - start1).days)]

    start2 = datetime.datetime.strptime("1-05-2020", "%d-%m-%Y")
    end2 = datetime.datetime.strptime("31-05-2020", "%d-%m-%Y")
    date_generated2 = [start2 + datetime.timedelta(days=x) for x in range(0, (end2 - start2).days)]

    plt.plot(date_generated2, result)
    plt.plot(date_generated1, volumen)
    plt.plot(date_generated2, result100)
    plt.plot(date_generated2,volumen1)
    plt.title(
        "Zielony to średnia ze 100 symulacji, niebieski to przeprowadzona 1 symulacja, pomarańczowy(kwiecień) i czerowny(maj) to wolumen danego waloru z giełdy")
    plt.show()

    return result_mean, result_median, result_stdev, result100_mean, result100_median, result100_stdev, volumen1_mean, volumen1_median, volumen1_stdev

name = input("Podaj nazwę ETC lub LTC lub XRP:")
crypto,crypto1 = data(name)
mean, median, stdev, mean100, median100, stdev100, mean_volumen1, median_volumen1, stdev_volumen1 = prediction(crypto,crypto1)
print(stdev,stdev100,stdev_volumen1)
