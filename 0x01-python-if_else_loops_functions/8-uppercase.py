#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        upper = ord(str[i])
        if 97 <= upper <= 122:
             upper = upper - 32
        print("{:c}".format(upper), end='')
    print("")
