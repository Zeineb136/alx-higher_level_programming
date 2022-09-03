#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
<<<<<<< HEAD
	for key, value in sorted(a_dictionary.keys()):
	   print ("{}: {}".format(key, value))
=======
    for key, value in sorted(a_dictionary.items()):
        print ("{:}: {:}".format(key, value))
>>>>>>> 9bf3b505666e8400e40765657455afd848de4254
