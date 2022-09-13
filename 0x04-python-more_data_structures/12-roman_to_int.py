#!/usr/bin/python3
def roman_to_int(roman_string):
    new = roman_string[:]
    num = 0;
    for i in range(len(new)):
            num += 1 + i
    return (num)
