from conf import DATA_FILE, WALLET
import csv
from models.action import Action
import time


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
            if float(price) > 0:
                actions_list.append(
                    Action(
                        name,
                        int(float(price) * 100),
                        round((float(profitPerCent) / 100) * (float(price) * 100), 2),
                    )
                )

    return actions_list


actions_dict = [action.__dict__ for action in actionsList()]


def bestComb(WALLET, actions_dict):
    matrice = [[0 for x in range(WALLET + 1)] for x in range(len(actions_dict) + 1)]
    for i in range(1, len(actions_dict) + 1):
        for j in range(1, WALLET + 1):
            if actions_dict[i - 1]["price"] <= j:
                matrice[i][j] = max(
                    actions_dict[i - 1]["profitEuro"]
                    + matrice[i - 1][j - actions_dict[i - 1]["price"]],
                    matrice[i - 1][j],
                )
            else:
                matrice[i][j] = matrice[i - 1][j]

    best_comb = []
    n = len(actions_dict)
    w = WALLET
    while w > 0 and n > 0:
        action = actions_dict[n - 1]
        if matrice[n][w] == matrice[n - 1][w - action["price"]] + action["profitEuro"]:
            best_comb.append(action)
            w -= action["price"]

        n -= 1

    a = [action["name"] for action in best_comb]
    tot = sum([action["price"] for action in best_comb])
    return round(matrice[-1][-1] / 100, 2), a, round(tot / 100, 2)


start_time = time.time()
print(bestComb(WALLET, actions_dict))
end_time = time.time()
print("durée total : ", round(end_time - start_time, 2), "s")
