import csv
import matplotlib.pyplot as plt

with open('rates.csv', 'r') as input_data:
    data = csv.reader(input_data)
    next(data)

    date = []
    rates = []

    for row in data:
        date.append(row[0])
        rate = float(row[1])
        rates.append(rate)

    date = date[::-1]
    rates = rates[::-1]

    plt.plot(date, rates)
    plt.show()
