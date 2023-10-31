import random, csv

players = ['Josh', 'Kate', 'Anna', 'Mary', 'Mark']
result = []

for player in players:

    for numb in range(100):
        score = random.randint(0, 1000)
        result.append([player, score])

with open('result.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Score'])

    for players in result:
        writer.writerow(players)
