#!/usr/bin/python3
def no_c(my_string):
    my_string = my_string.translate({ord(c): None for c in 'c' and 'C'})
    return (my_string)   
