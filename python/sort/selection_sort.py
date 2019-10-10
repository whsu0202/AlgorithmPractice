#!/usr/bin/python

import json

def selection_sort():

    with open("data.json", "r") as source_file:
        json_data = json.load(source_file)

    length = len(json_data)
    for index in range(length - 1):
        mini_value_index = index
        for inner_index in range(index, length):
            if json_data[inner_index] < json_data[mini_value_index]:
                mini_value_index = inner_index
        json_data[index], json_data[mini_value_index] = json_data[mini_value_index], json_data[index]

    return json_data

if __name__ == '__main__':
    print selection_sort()
