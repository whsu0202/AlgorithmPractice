#!/usr/bin/python

import json

def bubble_sort():

    with open("data.json", "r") as source_file:
        json_data = json.load(source_file)

    length = len(json_data)
    for index_i in range(length-1):
        for index_j in range(length-1-index_i):
            if json_data[index_j] > json_data[index_j+1]:
                json_data[index_j], json_data[index_j+1] = json_data[index_j+1], json_data[index_j]
    return json_data

if __name__ == '__main__':
    print bubble_sort()

