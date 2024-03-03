#!/usr/bin/python3
""" making change using dynamic approach """


def makeChange(coins, total):
    if total <= 0:
        return 0

    sorted_array = sorted(coins, reverse=True)
    rem = total
    ind = 0
    change = 0
    n = len(coins) - 1
    while (rem > 0):
        if ind > n:
            return -1
        if rem - sorted_array[ind] >= 0:
            change = change + 1
            rem = rem - sorted_array[ind]
        else:
            ind = ind + 1
    return change
