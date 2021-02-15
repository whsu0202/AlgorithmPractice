#!/usr/bin/python

import itertools

def next_bigger(n):
    n2str = str(n)
    s_list = list(itertools.permutations(n2str))
    n_list = []
    for num in range(len(s_list)):
        tmp = ""
        for dig in range(len(n2str)):
            tmp+=s_list[num][dig]
        n_list.append(int(tmp))
    
    n_list.sort()
    #for x in range(len(n_list)-1):
    #    for y in range(len(n_list)-1-x):
    #        if n_list[y] > n_list[y+1]:
    #            n_list[y], n_list[y+1] = n_list[y+1], n_list[y]

    # Doing the comparision within a list
    # n_list.index(n)+1 => Find a value's location in a array
    # and then use the next one to do comparision 
    for i in range(n_list.index(n)+1, len(n_list)):
        if n_list[i] > n:
            return n_list[i]
    
    return -1
            

if __name__ == "__main__":
    print(next_bigger(123))
    print(next_bigger(123456))
    print(next_bigger(7654321))
    print(next_bigger(7564321))
