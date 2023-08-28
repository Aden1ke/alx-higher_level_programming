#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return (True)
    except (TypeError, ValueError):
        import sys
        print("Exception:", sys.exc_info()[1], file=sys.stderr)
        return (False)
