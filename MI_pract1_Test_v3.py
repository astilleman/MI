from subprocess import Popen, PIPE
import sys

######################################################################################################################
# TODO:                                                                                                              #
# 1) PUT THIS FILE IN THE SAME FOLDER AS THE PYTHON FILE CONTAINING YOUR SOLUTION                                    #
# 2) CHANGE THE NAME 'MY_FILE_NAME.py' BELOW THIS BOX TO THE NAME OF YOUR PYTHON FILE                                #
# 3) RUN THIS FILE                                                                                                   #
######################################################################################################################


YOUR_SOLUTION_FILE_NAME = "practicum1.py"


######################################################################################################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE                                                                             #
######################################################################################################################


# parse the given output string
def parse_output(full_output_string):
    try:
        splitted = full_output_string.split(' ')
        uitvoer = (float(splitted[0]), int(splitted[1]), int(splitted[2]))
    except (Exception):
        uitvoer = -1
    return uitvoer


# Run one test case with given input and output, return True when test succeeds, False when test fails
def run_one_test_case(inp, verwachte_uitvoer, st):
    print(st)
    process = Popen([sys.executable, YOUR_SOLUTION_FILE_NAME], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    (output, err) = process.communicate(inp)
    output = output.decode('utf-8').strip()
    #print ('out', output)
    if len(str(err)) > 3:
        print('Your program threw an ERROR')
        return False
    exit_code = process.wait()
    uitvoer = parse_output(output)
    print("received output: ", output)
    if uitvoer == -1:
        print('Check your output format: print exactly three numeric values separated by a comma (no text). Example: print(val1,val2,val3)')
        return False
    return uitvoer == verwachte_uitvoer


# Retrieve a list containing all test_cases
def get_test_cases():
    all_test_cases = []
    # IN: 8 6 4 2 -1 OUT: 5.0 4 6
    st = "IN: 8 6 4 2 -1    EXPECTED OUT: 5.0 4 6"
    all_test_cases.append((b'8\n6\n4\n2\n-1\n',(5.0,4,6), st))

    # IN: 6 4 0 10 8 4 2 -1 OUT: 5.25 2 8
    st = "IN: 6 10 2 0 10 8 4 2 -1    EXPECTED OUT: 5.25 2 8"
    all_test_cases.append((b'6\n10\n2\n0\n10\n8\n4\n2\n-1\n', (5.25,2,8), st))

    # IN: 4 3 5 -1 OUT: 4.0 -1 -1
    st = "IN: 4 3 5 -1    EXPECTED OUT: 4.0 -1 -1"
    all_test_cases.append((b'4\n3\n5\n-1\n', (4.0,-1,-1), st))

    # IN: 12 10 8 9 17 4 2 1 -1 OUT: 5.67 2 9
    st = "IN: 12 10 8 9 17 4 2 1 -1    EXPECTED OUT: 5.67 2 9"
    all_test_cases.append((b'12\n10\n8\n9\n17\n4\n2\n1\n-1\n', (5.67, 2, 9),st))

    # IN: 10 5 -1 OUT: -1 -1 -1
    st = "IN: 10 5 -1    EXPECTED OUT: -1 -1 -1"
    all_test_cases.append((b'10\n5\n-1\n', (-1, -1, -1),st))

    # IN: 5 5 5 -1 OUT: 5.0, -1, -1
    st= "IN: 5 5 5 -1    EXPECTED OUT: 5.0 -1 -1"
    all_test_cases.append((b'5\n5\n5\n-1\n', (5.0, -1, -1),st))

        # IN: 5 5 5 -1 OUT: 5.0, -1, -1
    st= "IN: 5 5 5 5 -1    EXPECTED OUT: 5.0 -1 -1"
    all_test_cases.append((b'5\n5\n5\n5\n-1\n', (5.0, -1, -1),st))

    return all_test_cases


# Run all given test_cases
def run_test_cases(all_tests):
    for test_nb in range(len(all_tests)):
        (inp, outp, st) = all_tests[test_nb]
        test_result = run_one_test_case(inp, outp, st)
        if test_result:
            print('Test ' + str(test_nb + 1) + ': Succeeded')
        else:
            print('Test ' + str(test_nb + 1) + ': Failed')
        print("")


# load all test cases and test them on given solution
all_tests = get_test_cases()
run_test_cases(all_tests)



