def cats_heats(numb_cat, rounds):
    cats = {}
    result = []

    for n in range(numb_cat):
        cats[n] = 0

    steps = list(cats.keys())

    for i in range(rounds):
        if i >= 1:
            list_cats = steps[i::i]
            for k in cats.keys():
                if k in list_cats:
                    if cats[k] == 0:
                        cats[k] = 1
                    else:
                        cats[k] = 0

    [result.append(k) for k, v in cats.items() if v == 1]

    return result


rounds = int(input('Enter a number of rounds: ')) + 1
numb_cat = int(input('Enter a number of cats: ')) + 1

final = cats_heats(numb_cat, rounds)

print(f"Cats # {', '.join(map(str, final))} have hats at the end")
