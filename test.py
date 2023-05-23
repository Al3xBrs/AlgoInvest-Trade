# import itertools

actions = "ABCD"
# combinations = []


# for i in range(1, len(sequence) + 1):
#     for j in range(len(sequence) - i + 1):
#         combination = sequence[j : j + i]
#         combinations.append(combination)

# print(combinations)
# # print(getCombinations())
# # print(len(getCombinations()))


def factorial(n):
    if n == 0:
        return 1
    else:
        F = 1
        for k in range(2, n + 1):
            F = F * k
        print("F = ", F)
        return F


def combForm(n, r):
    nf = factorial(n)
    rf = factorial(r)
    n_r = n - r
    n_rf = factorial(n - r)

    nbCombinations = nf / (rf * n_rf)
    print(nbCombinations)
    return nbCombinations


nbTotComb = 0
for i in range(1, len(actions)):
    nbTotComb = nbTotComb + combForm(len(actions), i)

print(nbTotComb)
