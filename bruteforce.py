from conf import WALLET, DATA_FILE
import csv
from models.action import Action
from models.portfolio import Portfolio


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


def incrementCombination(actions_list, payload):
    fullprice = []
    combinations = []
    pnl = []
    payload["combinations"] = combinations
    payload["fullprices"] = fullprice
    payload["pnl"] = pnl

    for j in range(0, len(actions_list) + 1):
        for i in range(j + 1, len(actions_list) + 1):
            testing_list = actions_list[j:i]
            portfolio = Portfolio(testing_list)

            if checkWallet(portfolio.getFullActionsPrice) is True:
                combinations.append([action.name for action in portfolio.actions_list])
                fullprice.append(portfolio.getFullActionsPrice)
                pnl.append(portfolio.getPNL)
                continue

            else:
                break

    return payload


def saveData(payload):
    i = 1
    incrementCombination(actions_list, payload)
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


actions_list = actionsList()
