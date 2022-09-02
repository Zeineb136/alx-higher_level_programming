#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    sum_all = 0
    for item in (my_list):
        if item not in uniq_list:
            uniq_list.append(item)
    for n in uniq_list:
        sum_all = sum_all + n
    return (sum_all)
