#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
    except IndexError:
        pass
    finally:
        print()
    if x >= i:
        return i + 1
    else:
        return x + 1
