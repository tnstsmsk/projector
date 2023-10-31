import string, random

for c in string.ascii_uppercase:

    with open(f'{c}.txt', 'w') as file:
        number = str(random.randint(1, 100))
        file.write(number)

    with open(f'{c}.txt', 'r') as input_file, open('summary.txt', 'a') as summary:
        data = input_file.read()
        summary.write(f'{c}.txt: {str(data)} \n')
