#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_nums = list(set(my_list))
    result = 0
    for num in uniq_nums:
        result += num
    return result
