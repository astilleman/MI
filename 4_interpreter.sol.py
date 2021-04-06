"""
Schrijf een functie die eenvoudige commando's inleest en uitvoert. 
Er zijn twee soorten commando's:

    - "add x y"       : tel x en y op, met x en y floating point getallen.
    - "subtract x y"  : trek y af van x, met x en y floating point getallen.
    
De functie moet altijd een floating point getal teruggeven.


Onderaan de file staan enkele 'assert' statements.
Wanneer je deze file runt, zullen die ook uitgevoerd worden 
en weet je of jeimplementatie al dan niet correct is.
"""

def interpret(command):
    command = command.split(" ")
    command[1] = float(command[1])
    command[2] = float(command[2])
    if(command[0] == "add"):
        return command[1] + command[2]
    elif(command[0] == "subtract"):
        return command[1] - command[2]
    
# TESTS
assert interpret("add 5.7 6.3") == 12.0
assert interpret("add -5 10") == 5
assert interpret("add 10 -5") == interpret("add -5 10")
assert interpret("subtract -55.5 55.2") == -110.7
assert interpret("subtract 10 5") == 5
assert interpret("subtract 5 10") == -interpret("subtract 10 5")