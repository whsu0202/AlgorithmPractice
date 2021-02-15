#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    m_toys=0
    
    for i in prices:
        if k-i<0:
            break
        else:
            print(i)
            m_toys+=1
            k-=i
            
    return m_toys

if __name__ == '__main__':

    k = 50

    prices = [1,12,5,111,200,1000,10]

    result = maximumToys(prices, k)

    print("===>",result)
