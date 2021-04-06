'''

Implementeer de functies hieronder. Vervang daardoor 'pass' door gepaste Python-code

Merk op!!
    Het bestand dat je uiteindelijk inzendt mag GEEN syntax-fouten meer bevatten!
    Inzendingen met syntaxfouten geven een 0-score, ook als die syntax-fouten in slechts 1
    functie voorkomen!
    Lukt het je niet om voor een bepaalde functie een oplossing te vinden? Zet dan (evt. een deel)
    van je code dat syntax-fouten kan bevatten in commentaar!

'''


#########################################################################################################

# Deze functie gaat na of een 2-dimensionale data-structuur leeg is of niet
# @param m  - de 2-dimensionale data-structuur
#           - de functie mag ervan uitgaan dat m verwijst naar een geldige (lege of niet-lege) 2-dim data-structuur
# @return   - True als m een lege lijst is (dus: [ ]), of slechts 1 element bevat dat op zich een lege lijst
#               is dus: [ [ ] ] );  anders False
def is_lege_matrix(m):
    boolean = False
    if len(m) == 0:
        boolean = True
    elif len(m) == 1 and len(m[0]) == 0:
        boolean = True
    return boolean

#########################################################################################################

# Deze functie gaat na of de 2-dimensionale data-structuur een matrix is of niet
# @param m  - de 2-dimensionale data-structuur
#           - de functie mag ervan uitgaan dat m verwijst naar een geldige (lege of niet-lege) 2-dim data-structuur;
#             dit betekent dat als m niet leeg is, alle elementen van m een lijst zullen zijn
# @return   - True als alle 'rijen' van de data-structuur evenveel elementen bevatten, anders False
#           - bemerk: de return-value van een lege structuur (zoals hierboven gedefinieerd in de functie
#               is_lege_matrix) is True
def is_matrix (m):
    if is_lege_matrix(m) or len(m) == 1:
        return True
    aantal_rijen = len(m)
    i = 0
    #aantal_elementen_in_rij = len(m[i])
    #volgend_aantal_elementen_in_rij = len(m[i+1])
    while i < (aantal_rijen-1) and len(m[i]) == len(m[i+1]):
        i += 1
    if i == (aantal_rijen-1):
        return True
    else:
        return False




#########################################################################################################


# Deze functie gaat na of alle elementen op de rand van een matrix gelijk zijn
# @param m  - de matrix
#           - de functie mag ervan uitgaan dat m verwijst naar een geldige (lege of niet-lege) matrix, zoals
#             hierboven gedefinieerd
# @return   - True als alle elementen op de rand van m gelijk zijn, anders False
#           - bemerk: de return-value van een lege matrix is True
def gelijke_rand_matrix (m):
    if is_lege_matrix(m):
        return True
    lijst_randelementen = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i == 0 or j == 0:
                lijst_randelementen.append(m[i][j])
            elif i == len(m)-1 or j == len(m)-1:
                lijst_randelementen.append(m[i][j])
    randelement = lijst_randelementen[0]
    i = 1
    while i < len(lijst_randelementen) and lijst_randelementen[i] == randelement:
        i += 1
    if i == len(lijst_randelementen):
        return True
    else:
        return False



#########################################################################################################

# Deze functie maakt een nieuwe matrix met alle elementen van een oorspronkelijke matrix zonder de rand
# @param m  - de oorspronkelijke matrix
#           - de functie mag ervan uitgaan dat m verwijst naar een geldige, niet-lege matrix, zoals
#             hierboven gedefinieerd
# @return   - een matrix die alle elementen van m bevat zonder de rand-elementen
#           - bemerk: zie evt. de voorbeelden in de main-functie
def strip_matrix (m):
    nieuwe_rij = []
    nieuwe_matrix = []
    for i in range(1, len(m)-1):
        nieuwe_matrix.append(nieuwe_rij)
        for j in range(1, len(m[0])-1):
            nieuwe_rij.append(m[i][j])
        nieuwe_rij = []
    return nieuwe_matrix




#########################################################################################################


# In deze functie worden de functies al voor enkele voorbeelden getest.
# Pas deze functie aan om eventueel zelf andere tests te definiëren.

def main ():
    print("-- is_lege_matrix --")

    assert is_lege_matrix([]) == True
    assert is_lege_matrix( [ [ ] ] ) == True
    assert is_lege_matrix( [ [1, 1] ] ) == False
    assert is_lege_matrix( [ [1, 2] ] ) == False

    print("-- is_matrix --")

    assert is_matrix( [ ] ) == True
    assert is_matrix( [ [ ] ] ) == True
    assert is_matrix( [ [1] ] ) == True
    assert is_matrix( [ [1, 'a'] ] ) == True
    assert is_matrix( [ [1, 'a'], [True, 1.2] ] ) == True
    assert is_matrix( [ [1, 'a'], [True, 1.2] , [ "hello"] ] ) == False

    print("-- gelijke_rand_matrix --")

    assert gelijke_rand_matrix( [ ] ) == True
    assert gelijke_rand_matrix( [[1, 'a'], [True, 1.2]]) == False
    assert gelijke_rand_matrix( [[1,   1,    1,  1 ],
                                [1, 1.2, True,  1 ],
                                [1,   1,    2,  1 ]]) == False
    assert gelijke_rand_matrix( [[1,   1,    1,  1 ],
                                [1, 1.2, True,  1 ],
                                [1,   1,    1,  1 ]]) == True
    assert gelijke_rand_matrix([ ['a',   'a',  'a',   'a' ],
                                ['a',   1.2, True,   'a' ],
                                ['a',     1,    1,   'a' ],
                                ['a',   'a',   'a',  'a']]) == True
    assert gelijke_rand_matrix( [['a',   'a',  'a',   'a' ],
                                ['a',   1.2, True,   'a' ],
                                ['a',     1,    1,   'a' ],
                                ['a',   'b',   'a',  'a']]) == False

    print("-- strip_matrix --")

    assert strip_matrix       ([['a',   'a',  'a',   'a' ],
                               ['a',   1.2, True,   'a' ],
                               ['a',     1,    1,   'a' ],
                               ['a',   'b',   'a',  'a']]) == [ [1.2, True], [1, 1] ]
    assert strip_matrix       ([['a',   'a',  'a',   'a' ],
                               ['a',   1.2, True,   'a' ],
                               ['a',   'b',   'a',  'a']]) ==  [ [1.2, True] ]
    assert is_lege_matrix(
            strip_matrix ([[1,   1,    1,  1 ]]) )
    assert is_lege_matrix(
                strip_matrix  ([['a', 'a', 'a', 'a'],
                               ['a', 'b', 'a', 'a']])
            )

#########################################################################################################

# VERANDER NIETS AAN DE LIJN HIERONDER, EN PLAATS ENKEL OPDRACHTEN BINNEN DE FUNCTIES HIERBOVEN
if __name__ == "__main__":
    main()