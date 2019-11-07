# A Dynamic Programming (Tabulation method) based solution for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity C

from random import randint


def knapSack(C, wt, val, n):
    # L is a list of n+1 number of items, where each item is a list itself containing C+1 number of items.
    L = [[0 for x in range(C+1)] for x in range(n+1)]

    # Build a table K[n+1][C+1] in bottom up manner, each K[][] cell in the table holds a total value.
    # We're building a [n+1][C+1] table instead of [n][C] to include the cases where either C or w is zero
    # 0 <= i <= n
    for i in range(n+1):
        # 0 <= w <= C
        for w in range(C+1):
            # If either n or C is 0, then the max value = 0
            if i == 0 or w == 0:
                L[i][w] = 0
            # If the weight of an item is greater than the knapsack capacity, its not included
            elif wt[i-1] > w:
                L[i][w] = L[i-1][w]
            # If the weight of an item is equal to or lower than the knapsack capacity,
            # then choose the maximum of 2 cases where one includes the ith item and the other doesn't
            else:
                L[i][w] = max(L[i-1][w], val[i-1] + L[i-1][w-wt[i-1]])

    copyN = n
    copyC = C
    # Setting the weights and values of items not included in the knapsack to 0
    while copyN >= 0 and copyC >= 0:
        # Starting from the bottom-right (L[copyN][copyC]) value, check if the value above it is equal to it
        if L[copyN][copyC] == L[copyN-1][copyC]:
            # If equal, then item at index copyN-1 is not included in the chosen subset.
            wt[copyN-1] = 0
            val[copyN-1] = 0
            # move up 1 row
            copyN = copyN-1
        else:
            # If not equal, then item at index copyN-1 is included in the chosen subset
            # Thus, the next value to check is at 1 row up and column index is copyC - wt[copyN-1]
            copyC = copyC - wt[copyN-1]
            copyN = copyN-1

    print(f'Included item weights are non-zero: {wt}')
    print(f'Included item values are non-zero: {val}')

    return L[n][C]

    # Generating the input randomly
C = randint(20, 30)
n = randint(5, 10)
print('\nInput:\n')
print(f'Knapsack capacity: {C}')
print(f'Number of items: {n}')

wt, val = [], []

for _ in range(n):
    weight = randint(1, 15)
    value = randint(5, 50)
    wt.append(weight)
    val.append(value)

print(f'Weight of items: {wt}')
print(f'Value of items: {val}')

# Calling the knapSack function inside a print()
print('\nOutput:\n')
print(f'\nMaximum possible value = {knapSack(C, wt, val, n)}')
