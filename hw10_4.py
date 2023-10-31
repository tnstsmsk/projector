import csv

players = ['Josh', 'Kate', 'Anna', 'Mary', 'Mark']

with open('result.csv', 'r') as input_data, open('high_scores.csv', 'w') as output_data:

    next(input_data)
    data = csv.reader(input_data)

    rows = [[row[0], int(row[1])] for row in data]

    summary = {}

    for player in players:
        summary[player] = 0

    for k, v in summary.items():
        for row in rows:
            if row[0] == k:
                if row[1] > v:
                    summary[k] = row[1]

    result = dict(sorted(summary.items(), key=lambda item: item[1], reverse=True))

    writer = csv.writer(output_data)
    writer.writerow(['Player name', 'Highest score'])

    for key, value in result.items():
        writer.writerow([key, value])
