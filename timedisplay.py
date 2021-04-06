"""
Write a program that reads a number of seconds, and displays it as a number of
hours, a number of minutes and a number of seconds.
* Input will not be negative
* Output is of the format: hours:minutes:seconds
* Output hours will range between 0 and 23
Some example outputs for given inputs:
12457   	3 : 27 : 37
0           0 : 0 : 0
86399   	23 : 59 : 59
86400   	24 : 0 : 0
"""
# Commentaar bij meerdere lijnen met 2x driedubbele aanhalingstekens


total_seconds = int(input("Enter number of seconds: "))
def function(total_seconds):
# There are 60*60 seconds in an hour (volgorde bewerkingen dus haakjes)
    hours = total_seconds // (60 * 60)

# subtract the hours from the total amount of seconds
    total_seconds = total_seconds - hours * 60 * 60

# Calculate number of minutes
    minutes = total_seconds // 60

# Calculate number of remaining seconds
    seconds = total_seconds - minutes * 60

# print result (2de zelf, is niet helemaal correct, want spatie te veel dus daarom concatenatie(+) gebruiken)
    mes = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    return mes

print(function(total_seconds))
#print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
#print(hours, ":", minutes, ":", seconds)



assert function(12457) == "3:27:37"
assert function(86399) == "23:59:59"
assert function(4655456) == "1293:10:56"
assert function(86400) == "24:0:0"
'''
if total_seconds == 0:
    assert mes == "0:0:0"
if total_seconds == 86399:
    assert mes == "23:59:59"
if total_seconds == 4655456:
    assert mes == "1293:10:56"
if total_seconds == 86400:
    assert mes == "24:0:0"
'''

#(assert zelf :))