"""
Compares two numbers using the greater_than function.
"""

def greater_than(arg_1, arg_2):
    if arg_1 > arg_2:
        return True
    else:
        return False

if __name__ == "__main__":
    arg_1 = 10
    arg_2 = 1

    result = greater_than(10, 1)
    result_string = f"{'is' if result else 'is not'}"

    print(f'Result: {arg_1} ' + result_string + f' greater than {arg_2}.')