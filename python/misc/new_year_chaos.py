#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q_len=len(q)
    m_c=0
    str_a="Too chaotic"

    for x in range(q_len-1,-1,-1):
        if (q[x]-(x+1))>2:
            print(str_a)
            return

    for x in range(q_len-1,-1,-1):
        for y in range(0,x):
            print(y,x)
            if q[y] > q[x]:
                m_c+=1
    print(m_c)
            
        
if __name__ == '__main__':

    qa=[5,1,2,3,7,8,6,4]
    qb=[1,2,5,3,7,8,6,4]

    minimumBribes(qa)
    print("===================")
    minimumBribes(qb)

