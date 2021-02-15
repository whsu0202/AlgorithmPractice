#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
# https://www.hackerrank.com/challenges/2d-array/problem
def hourglassSum(arr):

    r_arr=[]
    a_count=0
    r_count=0
    max_v=0

    for p_x in range(0,4):
        for p_y in range(0,4):
            for i in range(0,3):
                for j in range(0,3):
                    a_count+=arr[i+p_x][j+p_y]
                    print("---",i+p_x,j+p_y,"=",a_count,"---")

            r_count=a_count-arr[1+p_x][p_y]-arr[1+p_x][2+p_y]
            print("=== r_count",r_count,"===")
            r_arr.append(r_count)
            a_count=0
            print(r_arr)

    max_v=max(r_arr)
    return max_v

if __name__ == '__main__':

    arr = [[1,2,3,4,5,6],
           [1,2,3,4,5,6],
           [1,2,3,4,5,6],
           [1,2,3,4,5,6],
           [1,2,3,4,5,6],
           [1,2,3,4,5,6]]

    result = hourglassSum(arr)

    print(result)
