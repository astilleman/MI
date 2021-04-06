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
    if len(xstr) == 0 or len(ystr) == 0:
        return [""]
    uitvoerlijst = []
    substring_set_xstr = all_substrings(xstr)
    substring_set_ystr = all_substrings(ystr)
    gemeenschappelijke_substrings = substring_set_xstr.intersection(substring_set_ystr)
    gemeenschappelijke_substrings_lijst = list(gemeenschappelijke_substrings)
    for element in gemeenschappelijke_substrings_lijst:
        if len(element) == lengte_langste_substring(gemeenschappelijke_substrings):
            uitvoerlijst.append(element)
    return uitvoerlijst


    pass


def all_substrings(word):
    substringset = set()
    for substr_len in range(1, len(word) + 1):
        for start_pos in range(len(word) - substr_len + 1):
            substringset.add(word[start_pos: start_pos + substr_len])
    return substringset
print(all_substrings('aapje'))

def lengte_langste_substring(setje):
    lijst = list(setje)
    maximale_lengte = len(lijst[0])
    for element in lijst:
        if len(element) > maximale_lengte:
            maximale_lengte = len(element)
    return maximale_lengte





'''
    if len(xstr) == 0 or len(ystr) == 0:
        return [""]
    if xstr[0] in ystr:
        longest_common_subsequence2(xstr, ystr)
    else:
        longest_common_subsequence(xstr[1:], ystr)

    return lijstenfunctie

def longest_common_subsequence2(xstr, ystr):
    substring = ""
    i = 0
    while xstr[i] == ystr[ystr.index(xstr[0])+i]:
        substring += xstr[i]
        i += 1
    lijstenfunctie(substring)


def lijstenfunctie(substring, lijst = []):
    lijst.append(substring)









    substring = ""
    if len(xstr) == 0 or len(ystr) == 0:
        return lijst
    else:
        if xstr[0] in ystr:
            substring += xstr[0]
        else:
            lijst.append(substring)
        return longest_common_subsequence(xstr[1:], ystr)'''








#
# DO NOT CHANGE ANYTHING BELOW THIS LINE !!!
#

def main():
    data = ("aapje", "banaan", ["aa"])
    result = longest_common_subsequence(data[0], data[1]);
    print(f"Testing with input '{data[0]}' and '{data[1]}'.")
    print(f"Received result: {result}")

    if result == data[2]:
        print("Looking good! Now try to run the test suite to see if your solution works with other examples as well.")

if __name__ == "__main__":
    main()
