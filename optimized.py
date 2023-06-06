from conf import WALLET


def bestComb(payload):
    actions_dict = payload["actions_dict"]
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

    payload["total_price_opti"] = round(
        (sum([action["price"] for action in best_comb])) / 100, 2
    )
    payload["actions_name_opti"] = [action["name"] for action in best_comb]
    payload["best_pnl_opti"] = round(matrice[-1][-1] / 100, 2)
    return payload


def saveBestCombOpti(payload):
    """"""

    action_best_comb = payload["actions_name_opti"]
    act_csv = str(action_best_comb).replace(",", " ").replace("[", "").replace("]", "")

    price_best_comb = payload["total_price_opti"]

    best_pnl = payload["best_pnl_opti"]

    with open("./Results/best_comb_opti.csv", "w") as f:
        f.write("Num,Combinations,Price,PNL")
        f.write("\n")
        f.write(f"1,{act_csv},{float(price_best_comb)},{float(best_pnl)}")
