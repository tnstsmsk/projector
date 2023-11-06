import csv

with open('ex_rates.csv', 'r') as input_data:
    data = csv.reader(input_data)
    next(data)

    rates = {}

    for row in data:
        rates[row[0]] = row[1]


def currency_converter(ammount, currency1, currency2):
    rate1 = float(rates[currency1])
    rate2 = float(rates[currency2])

    return rate2/rate1 * ammount
