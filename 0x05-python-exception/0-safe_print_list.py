#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for x in my_list:
            print(x, end='')
            i += 1
    except IndexError:
        break
    print('')
    return(i)
