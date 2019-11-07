# A Dynamic Programming (Tabulation method) based solution for 0-1 Knapsack problem

from random import randint

# Declaring variables
n = 0
C = 0
wt = []
val = []
L = []


# Function for generating the inputs randomly


def generateInputs():
    global n, C
    C = randint(20, 30)
    n = randint(5, 10)
    print('\nInput:\n')
    print(f'Knapsack capacity: {C}')
    print(f'Number of items: {n}')

    for _ in range(n):
        weight = randint(1, 15)
        value = randint(5, 50)
        global wt
        wt.append(weight)
        global val
        val.append(value)

    print(f'Weight of items: {wt} = ' + str(sum(wt)))
    print(f'Value of items: {val} = ' + str(sum(val)))

# Returns the maximum value that can be put in a knapsack of capacity C


def knapSack():
    # L is a list of n+1 number of items, where each item is a list itself containing C+1 number of items.
    global L
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
    return L[n][C]

# Function for setting the excluded items to 0 and print the optimal subset


def printOptimalSubset():
    global n, C, L
    while n >= 0 and C >= 0:
        # Starting from the bottom-right (L[n][C]) value, check if the value above it is equal to it
        if L[n][C] == L[n-1][C]:
            # If equal, then item at index n-1 is not included in the chosen subset.
            wt[n-1] = 0
            val[n-1] = 0
            # move up 1 row
            n = n-1
        else:
            # If not equal, then item at index n-1 is included in the chosen subset
            # Thus, the next value to check is at 1 row up and column index is C - wt[n-1]
            C = C - wt[n-1]
            n = n-1

    print(f'Included item weights are non-zero: {wt} = ' + str(sum(wt)))
    print(f'Included item values are non-zero: {val} = ' + str(sum(val)))


# Program starting point
generateInputs()
print('\nOutput:')
print(f'\nMaximum possible value = {knapSack()}')
printOptimalSubset()
