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
best_actions_list = sorted_list[0:20]


def isAdmissible(portfolio):
    if portfolio.getFullActionsPrice < WALLET:
        return True
    else:
        return False


def getCombinations(best_actions_list):
    combs = []
    admissible_portfolio = []
    for i in range(1, len(best_actions_list)):
        combs.append(list(combinations(best_actions_list, i)))

    for comb in combs:
        for portfolio in comb:
            portfolio_testing = Portfolio(portfolio)

            if isAdmissible(portfolio_testing):
                admissible_portfolio.append(portfolio_testing)

    return admissible_portfolio


def getBestComb(admissible_portfolio):
    sorted_portfolio = sorted(
        admissible_portfolio, key=lambda x: x.getPNL, reverse=True
    )
    return (
        sorted_portfolio[0].getFullActionsPrice,
        sorted_portfolio[0].getPNL,
        sorted_portfolio[0].actions_list,
    )


admissible_portfolio = getCombinations(best_actions_list)
best_portfolio = getBestComb(admissible_portfolio)
print(best_portfolio)
