from conf import WALLET
from models.portfolio import Portfolio
from itertools import combinations


def checkWallet(full_price):
    """Return True if the portfolio is available"""
    if WALLET > full_price:
        return True
    else:
        return False


def saveCombs(payload):
    """Save all the possibles combs in .csv"""
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
            f.write(f"{i}, {comb}, {float(fp)/100}, {float(pnl)/100}")
            f.write("\n")
            i += 1


def saveBestComb(payload):
    """Save the only best comb in .csv"""
    best_comb = [*payload["best_comb"][0]]
    best_portfolio = Portfolio(best_comb)

    price_best_comb = best_portfolio.getFullActionsPrice
    best_pnl = best_portfolio.getPNL
    action_best_comb = [action.name for action in best_portfolio.actions_list]
    act_csv = str(action_best_comb).replace(",", " ").replace("[", "").replace("]", "")

    with open("./Results/best_comb.csv", "w") as f:
        f.write("Num,Combinations,Price,PNL")
        f.write("\n")
        f.write(f"1,{act_csv},{float(price_best_comb)/100},{float(best_pnl)/100}")


def getCombinations(actions_list, payload):
    """Load all the possible combinations"""
    former_price = 0
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

                new_best_comb, former_price = getBestComb(
                    portfolio, best_comb, former_price
                )
                best_comb = new_best_comb

    payload["best_comb"] = best_comb
    return payload


def getBestComb(portfolio, best_comb, former_price):
    """Find the best combination"""

    # new_price = round((100 * portfolio.getPNL) / portfolio.getFullActionsPrice, 2)

    new_price = portfolio.getPNL

    if len(best_comb) == 0:
        best_comb.append(portfolio.actions_list)

    elif len(best_comb) == 1 and new_price > former_price:
        ac_list = [*best_comb[0]]
        last_portfolio = Portfolio(ac_list)
        # former_price = round(
        #     (last_portfolio.getPNL * 100) / last_portfolio.getFullActionsPrice, 2
        # )
        former_price = last_portfolio.getPNL
        best_comb.clear()
        best_comb.append(portfolio.actions_list)
    return best_comb, former_price
