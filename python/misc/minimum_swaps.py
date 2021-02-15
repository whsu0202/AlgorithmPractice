#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem
def minimumSwaps(arr):
    s_c=0
    a_len=len(arr)
    m_index=0
    b_arr=arr
    
    for x in range(a_len):
        if arr==sorted(b_arr):
            break
        else:
            m_index=x
            for y in range(x,a_len):
                if arr[y]<arr[m_index]:
                    m_index=y
            if m_index!=x:
                print(x,y,arr,m_index)
                arr[x],arr[m_index]=arr[m_index],arr[x]
                print(arr)
                print("----------------------")
                s_c+=1
                
    return s_c

if __name__ == '__main__':

    arr =[4,3,1,2]

    res = minimumSwaps(arr)
    print(res)
