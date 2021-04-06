"""
Given two strings, write a method 'longest_common_subsequence' that finds the list of longest common
subsequences (the longest group of characters that occur in both strings, in the same order).
For example, the list of longest common subsequences of 'methodiek' and 'katholiek' is ['thoiek']

Note that two strings can have multiple common subsequences. For instance, the longest common subsequences of
'methodiek' and 'ochtendgymnastiek' are ['ediek', 'etiek', 'hdiek', 'mtiek', 'odiek', 'tdiek']

If the strings do not have matching characters, the longest common subsequence is an empty string

Write this function as a RECURSIVE function. This is not enforced by the tests, but you should
implement it like this anyway. On the real exam, someone will actually look at your implementation
to manually verify that it is indeed written recursively.

If you upload your solution before the deadline, your implementation will be graded by us. This grade
is a direct (and automatically calculated) result of the output of the test cases in this file and an
additional set of test cases. Make sure you think about special and edge cases.
"""
def longest_common_subsequence(xstr, ystr): # do not change the signature of this method (i.e. do not change its name, add/remove parameters, ...)
    """
    Given two strings, this function returns the list of longest common subsequences of both strings
    """
    lijstje = []
    tuple_substrings = longest_common_subsequence2(xstr, ystr)
    for element in tuple_substrings:
        if element != '':
            lijstje.append(element)
    return lijstje


def longest_common_subsequence2(xstr, ystr, substring="", tupletje=()):
    # if len(xstr) == 0 or len(ystr) == 0:
    if len(xstr) == 0:
        return tupletje
    elif xstr[0] in ystr:
        substring += xstr[0]
        return longest_common_subsequence2(xstr[1:], ystr[ystr.index(xstr[0]) + 1:], substring, tupletje)
    else:
        tupletje += (substring,)
        substring = ""
        return longest_common_subsequence2(xstr[1:], ystr, substring, tupletje)



#
# DO NOT CHANGE ANYTHING BELOW THIS LINE !!!
#

def main():
    data = ("boek", "", ["k"])
    result = longest_common_subsequence(data[0], data[1]);
    print(f"Testing with input '{data[0]}' and '{data[1]}'.")
    print(f"Received result: {result}")

    if result == data[2]:
        print("Looking good! Now try to run the test suite to see if your solution works with other examples as well.")

if __name__ == "__main__":
    main()
