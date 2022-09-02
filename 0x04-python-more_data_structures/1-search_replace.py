#!/usr/bin/python3
def search_replace(my_list, search, replace):
	new_list = my_list[:]
	for item in my_list:
		if (item == search):
			item = replace	
	return (new_list)
