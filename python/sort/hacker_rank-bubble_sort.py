#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
# Complete the countSwaps function below.
def countSwaps(a):
    a_len=len(a)
    num_swaps=0
    for x in range(a_len-1):
        for y in range(a_len-x-1):
            if a[y]>a[y+1]:
                num_swaps+=1
                a[y],a[y+1]=a[y+1],a[y]
    
    print("Array is sorted in",num_swaps,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

