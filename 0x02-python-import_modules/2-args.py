#!/usr/bin/python3
import sys
if __name__ == '__main__':
    num = len(sys.argv) - 1
    print(num, " arguments")
    for i in range(1, num + 1):
        print("{} : {}".format(i, sys.argv[i]))
