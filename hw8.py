def cats_heats(numb_cat, rounds):
    cats = {}
    result = []

    for n in range(numb_cat):
        cats[n] = 0

    steps = list(cats.keys())

    for i in range(rounds):
        list_cats = steps[::i + 1]
        for k in cats.keys():
            if k in list_cats:
                if cats[k] == 0:
                    cats[k] = 1
                else:
                    cats[k] = 0

    [result.append(k + 1) for k, v in cats.items() if v == 1]

    return result


rounds = int(input('Enter a number of rounds: '))
numb_cat = int(input('Enter a number of cats: '))

final = cats_heats(rounds, numb_cat)

print(f"Cats # {', '.join(map(str, final))} have hats at the end")
