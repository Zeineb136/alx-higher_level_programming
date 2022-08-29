#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_list2 = my_list[:]
    for i in range(0, len(my_list2)):
       if my_list2[i] % 2 == 0:
          my_list2[i] = True
       else:
          my_list2[i] = False
    return(my_list2)
