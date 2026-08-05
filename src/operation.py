"""
Performs the specified operation on the two provided integers.

Usage:
    python operation.py <operation_keyword> <int_1> <int_2>
"""

import sys

if __name__ == "__main__":
    operation_keyword = sys.argv[1]
    arg_1 = int(sys.argv[2])
    arg_2 = int(sys.argv[3])

    if operation_keyword == "MULTIPLY":
        res = arg_1 * arg_2
    elif operation_keyword == "ADD":
        res = arg_1 + arg_2

    print(f"result: {res}")