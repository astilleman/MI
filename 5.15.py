def reverse(string):
    if len(string) == 0 or len(string) == 1:
        return string
    else:
        return reverse(string[1:]) + string[0]

assert reverse("flow") == "wolf"
assert reverse("mama") == "amam"
