import random, csv

players = ['Josh', 'Kate', 'Anna', 'Mary', 'Mark']
result = {}

for player in players:
    result[player] = 0

    for numb in range(100):
        score = random.randint(0, 10)
        result[player] += score

summary = [[key, value] for key, value in result.items()]

with open('result.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Score'])

    for players in summary:
        writer.writerow(players)
