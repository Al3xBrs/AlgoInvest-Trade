from conf import WALLET, DATA_FILE
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
            actions_list.append(Action(name, price, profitPerCent))

    return actions_list


actions_list = actionsList()


def checkWallet(full_price):
    """Check the wallet if it's still ok

    Args:
        full_price (int): Full price of an actions list

    Returns:
        Boolean: True if Wallet still ok
                 False if wallet can't
    """
    if WALLET > full_price:
        return True
    else:
        return False


def saveData(payload):
    i = 1

    getCombinations(actions_list, payload)
    combinations = payload["combinations"]
    fullprices = payload["fullprices"]
    pnls = payload["pnl"]
    with open("./Results/combinations.csv", "w") as f:
        f.write("Num,Combinations,Price,PNL")
        f.write("\n")
        for j in range(0, len(combinations)):
            pnl = str(pnls[j]).replace(",", " ").replace("[", "").replace("]", "")
            fp = str(fullprices[j]).replace(",", " ").replace("[", "").replace("]", "")
            comb = (
                str(combinations[j]).replace(",", " ").replace("[", "").replace("]", "")
            )
            f.write(f"{i}, {comb}, {fp}, {pnl}")
            f.write("\n")
            i += 1


def getCombinations(actions_list, payload):
    combs = []
    fullprices = []
    pnl = []
    payload["combinations"] = combs
    payload["fullprices"] = fullprices
    payload["pnl"] = pnl

    for k in range(1, len(actions_list)):
        testing_list = combinations(actions_list, k)

        for comb in list(testing_list):
            portfolio = Portfolio(comb)
            if checkWallet(portfolio.getFullActionsPrice) is True:
                combs.append([action.name for action in portfolio.actions_list])
                fullprices.append(portfolio.getFullActionsPrice)
                pnl.append(portfolio.getPNL)
                continue

    return payload
