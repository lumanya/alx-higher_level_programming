#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError, ZeroDivisionError) as tpe:
        print("Exception: {}".format(tpe))
        return False
