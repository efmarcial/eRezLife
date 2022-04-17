#!/usr/bin/env python3

import re

# test raw strings
string = '<html><body><div><a></a></div></body></html>'
string2 = '<html><body><div></a></body></html>'
string3 = '<html><body><div><a></div></a>'

def format_html(string):

    # Remove all '<' '>' and '/' from raw string and into a list
    arr = re.split('[</>]', string)

    # Remove all whitespaces if any in the list arra
    arr = [i for i in arr if i]

    n = len(arr)
    low = 0
    tab = 0
    high = n
    mid = n // 2

    # Travers through array
    for item in range(n):

        # While travesing array check for matching tabs
        # by checking the start and end index of the array
        if arr[item] == arr[-item-1]:

            # start formating low side of array element and adding spaces until it reached mid of the array
            if low < mid:
                print("  "*(tab), "<{}>".format(arr[item]))
                low += 1
                tab += 1

            # start formatting high side of array and removing spaces until loop ends
            elif  high > mid:
                print("  "*(tab-1), "</{}>".format(arr[item]))
                high -= 1
                tab -= 1

        # If no matching tag then stop for loop
        else:
            # If missing tag or not matched then print error and return 1
            print("Error Found. Missing or Mismatched tag.")
            return 1
            break

    # If no erros then return 0
    return 0

# Run the function
if __name__ == '__main__':
    format_html(string)
