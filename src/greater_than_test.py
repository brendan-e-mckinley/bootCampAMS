from greater import greater_than

def test_greater_than():
    """Verify that the function works as expected."""
    arg_1 = 100
    arg_2 = 200

    # false case
    assert greater_than(arg_1, arg_2) is False

    # true case
    assert greater_than(arg_2, arg_1) is True

if __name__ == "__main__":
    test_greater_than()