#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
   i = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
    except IndexError:
        pass
    finally:
        print()
    if x >= i:
        return i + 1
    elif i == 0:
        return i
    else:
        return x + 1
