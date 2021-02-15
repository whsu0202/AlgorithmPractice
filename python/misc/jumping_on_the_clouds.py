#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    list_len=len(c)
    jumps=0
    position=0
    while list_len-position>1:
        if (list_len-position)==2 and c[position+1]==1:
            break
        elif c[position+1]==1 and c[position+2]==0:
            position+=2
            jumps+=1
            print(position)
        elif c[position+1]==0 and (list_len-position)==2:
            position+=1
            jumps+=1
            print(position)
        elif c[position+1]==0 and c[position+2]==0:
            position+=2
            jumps+=1
            print(position)
        elif c[position+1]==0 and c[position+2]==1:
            position+=1
            jumps+=1
            print(position)

    return jumps

if __name__ == '__main__':

    c=[0,0,0,1,0,1]
    result = jumpingOnClouds(c)
    print("================================")
    print(result)
