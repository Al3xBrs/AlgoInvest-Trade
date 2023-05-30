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


def saveCombs(payload):
    i = 1

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


def saveBestComb(payload):
    best_comb = [*payload["best_comb"][0]]
    best_portfolio = Portfolio(best_comb)

    price_best_comb = best_portfolio.getFullActionsPrice
    best_pnl = best_portfolio.getPNL
    action_best_comb = [action.name for action in best_portfolio.actions_list]
    act_csv = str(action_best_comb).replace(",", " ").replace("[", "").replace("]", "")

    with open("./Results/best_comb.csv", "w") as f:
        f.write("Num,Combinations,Price,PNL")
        f.write("\n")
        f.write(f"1,{act_csv},{price_best_comb},{best_pnl}")


def getCombinations(actions_list, payload):
    former_profit = 0
    best_comb = []
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

                new_best_comb, former_profit = getBestComb(
                    portfolio, best_comb, former_profit
                )
                best_comb = new_best_comb

    payload["best_comb"] = best_comb
    return payload


def getProfitFullActions(portfolio):
    if portfolio.getFullActionsPrice == 0:
        profit = 0
    else:
        profit = round((portfolio.getPNL * 100) / portfolio.getFullActionsPrice, 2)

    return float(profit)


def getBestComb(portfolio, best_comb, former_profit):
    new_profit = getProfitFullActions(portfolio)

    if len(best_comb) == 0:
        best_comb.append(portfolio.actions_list)

    elif len(best_comb) == 1 and new_profit > former_profit:
        ac_list = [*best_comb[0]]
        former_list = [action for action in ac_list]
        last_portfolio = Portfolio(former_list)
        former_profit = getProfitFullActions(last_portfolio)
        best_comb.clear()
        best_comb.append(portfolio.actions_list)
    return best_comb, former_profit
