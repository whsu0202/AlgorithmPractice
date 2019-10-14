#!/usr/bin/python

import json

DEFAULT_BUCKET_NUMBER = 10

def insertion_sort(list_n):
    for elm_idx in range(len(list_n)):
        insertion_idx=elm_idx
        while insertion_idx > 0 and list_n[insertion_idx-1] > list_n[insertion_idx]:
            list_n[insertion_idx-1], list_n[insertion_idx] = list_n[insertion_idx], list_n[insertion_idx-1]
            insertion_idx-=1
    return 


# Sort numbers in a known range (E.g., 1-100, 1-1000)
def bucket_sort(bucket_count=DEFAULT_BUCKET_NUMBER):

    with open("data.json", "r") as source_file:
        json_data = json.load(source_file)

    # Create buckets
    buckets = [[] for _ in range(bucket_count)]

    # Calculate the divider
    max_value, min_value = max(json_data), min(json_data)
    divider = (max_value - min_value) // bucket_count + 1

    # Put the element into buckets.
    # Negative Indexing: -1 refers to the last item, -2 refers to the second last item etc.
    for elm_index in range(len(json_data)): 
        buckets[int(json_data[elm_index]-min_value) // divider].append(json_data[elm_index])

    # Sort the elements in the buckets
    for bukt_idx in range(bucket_count):
        if buckets[bukt_idx]!='':
            insertion_sort(buckets[bukt_idx])

    # Pop up data
    sorted_elms=[]
    for bukt_no in range(bucket_count):
        if buckets[bukt_no]!='':
            for elm_idx in range(len(buckets[bukt_no])):
                # Using append(),extend(), or insert() to add a data into sorted_elms
                # Because it's an empty list, we're attempting to write to element[0] in the first iteration
                # which doesn't exist yet.
                sorted_elms.append(buckets[bukt_no][elm_idx])

    return sorted_elms


if __name__ == '__main__':
    print bucket_sort()
