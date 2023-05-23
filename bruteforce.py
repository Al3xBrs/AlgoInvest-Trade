from conf import WALLET, DATA_FILE
import csv
from models.action import Action
import itertools


def actionsList():
    """Get data from .csv file

    Args:
        DATA_FILE: .csv file with data

    Returns:
        list : actions dicts list
    """

    actionsList = []
    with open(DATA_FILE, "r") as f:
        obj = csv.reader(f, delimiter=";")
        for name, price, profitPerCent in obj:
            actionsList.append(Action(name, price, profitPerCent))

    return actionsList


actions = actionsList()

print("nb actions", len(actions))
combinations = []
for i in range(1, len(actions) + 1):
    print("i = ", i)
    for j in range(len(actions) - i + 1):
        combination = actions[j : j + i]

        combinations.append(combination)
        print("j = ", j)
        print("combs = ", combination)

print("combs tot = ", combinations)
print("nb combs tot = ", len(combinations))

# i[0] + i[1], i[0] + i [2], i[0] + i[n] = i[0] + len(comb)+1

# for i in range 1, len(comb) + 1

# Formule combinaison : C(n,r) = n! / (r!(n-r)!)


def factorial(n):
    if n == 0:
        return 1
    else:
        F = 1
        for k in range(2, n + 1):
            F = F * k

        return F


def combForm(n, r):
    nbCombinations = factorial(n) / (factorial(r) * factorial(n - r))
    return nbCombinations


nbTotComb = 0
for i in actions:
    nbTotComb = nbTotComb + combForm(len(actions), i)

print(nbTotComb)
