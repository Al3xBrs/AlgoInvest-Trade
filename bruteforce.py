import csv

DATA_FILE = "src/data.csv"


def getData(DATA_FILE):
    actionsList = []
    with open(DATA_FILE, "r") as f:
        obj = csv.reader(f, delimiter=";")

        for name, price, profit in obj:
            actionsList.append({name: {"price": int(price), "profit": int(profit)}})

        return actionsList


print(getData(DATA_FILE))
