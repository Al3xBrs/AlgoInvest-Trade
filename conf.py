import csv
from models.action import Action

DATA_FILE = "data/dataset2_Python+P7.csv"
WALLET = 500 * 100


def actionsList():
    """Get data from .csv file"""

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
