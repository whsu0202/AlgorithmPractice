#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/repeated-string/problem
# Complete the repeatedString function below.
def repeatedString(s, n):
    s_len=len(s)
    rt=math.floor(n/s_len)
    remainder=n%s_len
    r_s=s[:remainder]
    a_count=s.count("a")*rt+r_s.count("a")
    print(rt, remainder, r_s, a_count)
    
    return a_count

if __name__ == '__main__':

    result = repeatedString("abababc", 10)

    print("==========", result, "===========")

