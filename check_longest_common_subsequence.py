import sys
import longest_common_subsequence as program_file

#####################################################################################################################################
# TODO:
# 1) PUT THIS FILE IN THE SAME FOLDER AS THE PYTHON FILE CONTAINING YOUR SOLUTION                                                   #
# 1b) IF YOUR FILE_NAME IS DIFFERENT FROM longest_common_subsequence2.py THEN CHANGE longest_common_subsequence
#     IN THE SECOND IMPORT STATEMENT TO THE NAME OF YOUR FILE                                                                        #
# 2) RUN THIS FILE                                                                                                                  #
####################################################################################################################################@

# These test cases test whether the algorithm produces the correct output; they do not check whether the function
# is actually recursive!

def runtests():
    runtest('aapje', 'banaan', ['aa'])
    runtest('methodiek', 'katholiek', ['thoiek'])
    runtest('methodiek', 'ochtendgymnastiek', ['ediek', 'etiek', 'hdiek', 'mtiek', 'odiek', 'tdiek'])

def runtest(xstr, ystr, expected):
    # execute 'longest_common_subsequence' with the given input
    ok = True
    try:
        result = program_file.longest_common_subsequence(xstr, ystr)
    except:
        result = "(program crash)"
        ok = False
    
    # check the result
    if ok:
        try:
            # sort the result and compare it with what we expect
            ok = sorted(result) == expected   # this may crash if 'result' is not enumerable, or if it contains uncomparable items
        except:
            ok = False

    if not ok:
        print(f"Error: input '{xstr}' and '{ystr}' returned the wrong result.")
        print(f"Expected: {expected}, received: {result}")
    else:
        print(f"Test case for '{xstr}' and '{ystr}' worked.")
    print() # empty line

if __name__ == "__main__":
    runtests()
