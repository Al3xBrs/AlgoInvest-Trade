import csv

DATA_FILE = "src/data.csv"

def getData(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        obj = csv.reader(f)

        for ligne in f :
            print(ligne)
            

getData(DATA_FILE)