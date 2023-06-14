#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_ord = list(a_dictionary.keys())
    sort_ord.sort()

    for i in sort_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
