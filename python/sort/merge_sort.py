#!/usr/bin/python

import json

def merge_sort(json_data):
    if len(json_data) != 1:
        mid_value = len(json_data) // 2
        L_list, R_list = json_data[:mid_value], json_data[mid_value:]
        merge_sort(L_list)
        merge_sort(R_list)

        i=j=k= 0
        while i<len(L_list) and j<len(R_list):
            if L_list[i] < R_list[j]:
                json_data[k] = L_list[i]
                i+=1
            else:
                json_data[k] = R_list[j]
                j+=1
            k+=1
        # Pop the remaining elements of L_list to overwrite the existing elements in the array
        #                                                           E.g., [4,0,2] >> [4][0,2]
        # After finishing the comparison, the new values in the array are [0,2,"2"].
        # It needs to pop "4"(The last element in the L_list) to overwrite the old element - "2"
        while i<len(L_list):
            json_data[k] = L_list[i]
            i+=1
            k+=1

        # Pop the remaining elements of R_list to overwrite the existing elements in the array
        while j<len(R_list):
            json_data[k] = R_list[j]
            j+=1
            k+=1

    return json_data

if __name__ == '__main__':
    # Load the data
    with open("data.json","r") as source_file:
        json_data = json.load(source_file)
    print merge_sort(json_data)
