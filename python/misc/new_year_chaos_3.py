#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/new-year-chaos/problem
# Complete the minimumBribes function below.
def minimumBribes(q):
    q_len = len(q)
    swaps = 0
    swaped = False
    
    # check if the queue is too chaotic
    for i, v in enumerate(q):
        if (v - 1) - i > 2:
            print("Too chaotic")
            return
    # bubble sorting to find the answer
    for i in range(q_len):
        for j in range(q_len-i-1):
            if q[j] > q[j+1]:
                q[j],q[j+1]=q[j+1],q[j]
                swaps += 1
                swaped = True
        
        if swaped:
            swaped = False
        else:
            break

    print(swaps)   
        
if __name__ == '__main__':

    qa=[5,1,2,3,7,8,6,4]
    qb=[1,2,5,3,7,8,6,4]

    minimumBribes(qa)
    print("===================")
    minimumBribes(qb)

