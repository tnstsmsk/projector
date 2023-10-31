import csv

players = ['Josh', 'Kate', 'Anna', 'Mary', 'Mark']

with open('result.csv', 'r') as input_data, open('high_scores.csv', 'w') as output_data:

    next(input_data)
    data = csv.reader(input_data)

    rows = [[row[0], int(row[1])] for row in data if row]


print(rows)