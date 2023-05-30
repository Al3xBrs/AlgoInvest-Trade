from bruteforce import saveCombs, saveBestComb, getCombinations, actionsList
from datetime import datetime
import time


def main():
    """main"""
    start_time = time.time()
    payload = {}
    actions_list = actionsList()
    getCombinations(actions_list, payload)
    saveCombs(payload)
    saveBestComb(payload)
    end_time = time.time()
    print("Total duration : ", round(end_time - start_time, 2), " secondes")


if __name__ == "__main__":
    main()
