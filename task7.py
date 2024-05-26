import random
from collections import defaultdict

from tabulate import tabulate


def dices_probabilities(num_experiments):
    res = defaultdict(int)

    for _ in range(num_experiments):
        dice_1, dice_2 = int(random.randint(1, 6)), int(random.randint(1, 6))
        res[sum((dice_1, dice_2))] += 1

    probs = {s: f'{o / num_experiments * 100}% ({o}/{num_experiments})' for s, o in res.items()}
    probs = dict(sorted(probs.items()))
    return probs


probabilities = dices_probabilities(100000)

print(tabulate(probabilities.items(), headers=['Сума', 'Імовірність']))

#  Сума  Імовірність
# -----  ----------------------------------
#     2  2.758% (2758/100000)
#     3  5.694% (5694/100000)
#     4  8.3% (8300/100000)
#     5  11.087% (11087/100000)
#     6  13.729% (13729/100000)
#     7  16.649% (16649/100000)
#     8  13.875000000000002% (13875/100000)
#     9  11.134% (11134/100000)
#    10  8.278% (8278/100000)
#    11  5.683% (5683/100000)
#    12  2.8129999999999997% (2813/100000)
