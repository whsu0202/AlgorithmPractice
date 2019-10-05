#!/usr/bin/python

import json

def insertion_sort():

    with open("data.json", "r") as source_file:
        json_data = json.load(source_file)

    for index in range(1 , len(json_data)):
        insertion_index = index
        print json_data
        print "#######################"
        while insertion_index > 0 and json_data[insertion_index - 1] > json_data[insertion_index]:
            json_data[insertion_index-1], json_data[insertion_index] = json_data[insertion_index], json_data[insertion_index-1]
            print "------------------------------"
            print json_data
            print "------------------------------"
            insertion_index -= 1
 

    return json_data


if __name__ == "__main__":
    print insertion_sort()
