import csv

rates = [
    ['USD', 1.0702],
    ['EUR', 1],
    ['BGN', 1.9558],
    ['CZK', 24.414],
    ['GBP', 0.86983],
    ['HUF', 380.38],
    ['PLN', 4.4500],
    ['CHF', 0.9625],
]

with open('ex_rates.csv', 'w') as input_data:
    data = csv.writer(input_data)
    data.writerow(['Currency', 'Rate'])
    for currency in rates:
        data.writerow(currency)
