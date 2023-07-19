#!/usr/bin/python3
def uniq_add(my_list = []):
    uniq_set = set()
    for element in my_list:
    if type (element) is int:
        uniq_set.add (element)
return sum(uniq_set)
