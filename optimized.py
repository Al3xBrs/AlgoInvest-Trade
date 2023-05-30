from conf import DATA_FILE, WALLET
import csv
from models.action import Action
from models.portfolio import Portfolio
from itertools import combinations


def actionsList():
    """Get data from .csv file

    Args:
        DATA_FILE: .csv file with data

    Returns:
        list : actions dicts list
    """

    actions_list = []
    with open(DATA_FILE, "r") as f:
        obj = csv.reader(f, delimiter=",")
        for name, price, profitPerCent in obj:
            if 1 < float(price) < WALLET and float(profitPerCent) > 1:
                actions_list.append(
                    Action(
                        name,
                        float(price),
                        float(profitPerCent),
                        round((float(profitPerCent) / 100) * float(price), 2),
                    )
                )

    return actions_list


actions_list = actionsList()
sorted_list = sorted(actions_list, key=lambda x: x.profitE, reverse=True)


def isAdmissible(portfolio):
    if portfolio.getFullActionsPrice > WALLET:
        return False
    else:
        return True


def getCombinations(sorted_list):
    combs = []

    for i in range(1, len(sorted_list)):
        testing_list = combinations(sorted_list, i)
        for comb in testing_list:
            portfolio = Portfolio(comb)
            if isAdmissible(portfolio):
                combs.append(comb[0:-1])

            else:
                break

    return combs


combs = getCombinations(sorted_list)
print(combs)
