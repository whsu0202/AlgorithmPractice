#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/minimum-swaps-2/problem
# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos

    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
            print(arr)
    return swaps


if __name__ == '__main__':

    arr =[4,3,1,2]

    res = minimumSwaps(arr)
    print(res)
