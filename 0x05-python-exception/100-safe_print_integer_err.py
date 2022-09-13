#!/usr/bin/python3i
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end ="\n")
        return(True)
    except (ValueError, TypeError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return(False)
