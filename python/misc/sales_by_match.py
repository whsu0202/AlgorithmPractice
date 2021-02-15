import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
# https://www.hackerrank.com/challenges/sock-merchant/problem
def sockMerchant(n, ar):
    pairs=0
    dedupe_list = list(dict.fromkeys(ar))
    print(dedupe_list)
    for x in dedupe_list:
        same_sock_count = ar.count(x)
        print (same_sock_count)
        pairs = pairs+math.floor(same_sock_count/2)
        print (pairs)
        print (ar)
        print("--------------")

    return pairs

if __name__ == '__main__':

    n = 9
    ar = [10,20,20,10,10,30,50,10,20] 

    result = sockMerchant(n, ar)
