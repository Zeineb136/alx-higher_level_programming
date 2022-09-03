#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = a_dictionary
    for i in a_dictionary:
        d[i] = 2 * d[i]
    return (d)
