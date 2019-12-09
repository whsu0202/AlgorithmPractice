#!/usr/bin/python

import datetime

def date_validation(input_string):

    try:
        datetime.datetime.strptime(input_string, '%Y-%m-%d')
        print ("It's a correct date format")
    except ValueError:
        raise ValueError('Incorrect date format!!!!')


if __name__ == "__main__":
    # In order to handle dash(-) symbol, using "raw_input()" instead of "input()".
    user_input = raw_input('Enter 3 numbers separated by a dash (-), e.g., 2018-99-88:\n')
    date_validation(user_input)
