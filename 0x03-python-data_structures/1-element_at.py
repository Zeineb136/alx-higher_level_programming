#!/usr/bin/python3
def element_at(my_list, idx):
    max_idx = len(my_list) - 1
    if idx < 0:
        return(0)
    elif idx > max_idx:
        return(0)
    else:
        return(my_list[idx])
