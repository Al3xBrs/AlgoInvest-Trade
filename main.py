from bruteforce import saveCombs, saveBestComb, getCombinations
import time
from conf import actionsList
from optimized import bestComb, saveBestCombOpti

payload = {}


def main_bruteforce(payload):
    """main"""
    print("bruteforce")
    start_time = time.time()

    actions_list = actionsList()
    getCombinations(actions_list, payload)
    saveCombs(payload)
    saveBestComb(payload)
    end_time = time.time()
    print("Total duration : ", round(end_time - start_time, 2), " secondes")


def main_optimized(payload):
    """"""
    print("opti")
    start_time = time.time()
    payload["actions_dict"] = [action.__dict__ for action in actionsList()]
    bestComb(payload)
    saveBestCombOpti(payload)
    end_time = time.time()
    print("Total duration : ", round(end_time - start_time, 2), " secondes")


if __name__ == "__main__":
    if len(actionsList()) <= 20:
        main_bruteforce(payload)
    main_optimized(payload)
