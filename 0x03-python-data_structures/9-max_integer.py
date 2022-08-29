#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max1 = my_list[0]
        for i in range(0, len(my_list)):
            a = my_list[i]
            if a > max1:
                max1 = a
        return(max1)
