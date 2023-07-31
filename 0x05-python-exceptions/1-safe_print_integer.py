#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format().
    Args:
        value (int): The integer to be printed.
    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(int(value)))
        return (True)
    except (ValueError, TypeError):
        return (False)
