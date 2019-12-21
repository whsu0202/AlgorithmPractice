#!/usr/bin/python

def next_bigger(n):

    if type(n) is str or n == "" or n < 10:
        return -1
        
    n2str = str(n)
    str_list = list(n2str)
    sub_list = []
    pivot, sub, index_pivot, nb_num = "", "", 0, ""
    
    for i in range(len(n2str)-1, 0, -1):
        sub_list.append(str_list[i])
        if str_list[i-1] < str_list[i]:
            pivot = str_list[i-1]
            index_pivot = i-1
            break
        elif i==1:
            return -1


    sub_list.sort()
    for x, y in enumerate(sub_list):
        if y > pivot:
            sub = y
            sub_list[x] = pivot
            break
    
    nb_list = str_list[:index_pivot]
    nb_list.append(sub)
    nb_list += sub_list
    
    for x in nb_list:
        nb_num += x
    
    return int(nb_num)

if __name__ == "__main__":
    print next_bigger(123)
    print next_bigger(123456)
    print next_bigger(7654321)
    print next_bigger(7564321)
