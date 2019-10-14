#!/usr/bin/python

import json

def merge_sort(json_data):
    if len(json_data) != 1:
        mid_value = len(json_data) // 2
        L_list, R_list = json_data[:mid_value], json_data[mid_value:]
        print L_list, R_list
 


if __name__ == '__main__':
    # Load the data
    with open("data.json","r") as source_file:
        json_data = json.load(source_file)
    merge_sort(json_data)
