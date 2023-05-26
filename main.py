from bruteforce import saveCombs, saveBestComb, getCombinations, actionsList


def main():
    payload = {}
    actions_list = actionsList()
    getCombinations(actions_list, payload)
    saveCombs(payload)
    saveBestComb(payload)


if __name__ == "__main__":
    main()
