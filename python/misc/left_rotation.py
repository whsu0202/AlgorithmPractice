#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the rotLeft function below.
def rotLeft(a, d):
    a_list=collections.deque(a)
    a_list.rotate(-d)# "-" means left rotations
    return list(a_list)

if __name__ == '__main__':

    d = 3
    a = [1,2,3,4,5,6,7]

    result = rotLeft(a, d)
    print(result)
