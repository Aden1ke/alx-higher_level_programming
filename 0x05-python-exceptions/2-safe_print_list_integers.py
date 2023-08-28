#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for val in my_list[:x]:
            if isinstance(my_list[val], int):
                count += 1
                print("{:d}".format(my_list[val]), end="")
        print()
        return (count)
    except (IndexError, ValueError, TypeError):
        pass
