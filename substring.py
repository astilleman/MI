def find_string(main_string, sub_string):
    for position in range(len(main_string) - len(sub_string) + 1):
        slice = main_string[position:position + len(sub_string)]
        if slice == sub_string:
            return position
    return None

assert find_string("Some Text", "Some") == 0
assert find_string("Some text", "other") is None
assert find_string("Some text", "text") == 5