"""
Insertion Sort voegt iteratief elementen toe aan een reeds
gesorteerde . Het toevoegen gebeurt vaak door lineair
te zoeken. Het is efficiënter om hiervoor Binary Search te
gebruiken. Schrijf een functie die een  sorteert met
behulp Insertion Sort en Binary Search. (Hint: schrijf een
aparte functie om de index te zoeken met behulp van Binary
Search)
"""

def efficient_insertion_sort(lijst, nieuw):
        i = 0
        for i in range(1, len(nieuw)):
            index_element = binary_search(lijst, nieuw[i], 0, len(lijst))
            if index_element != -1:
                lijst.insert(index_element, nieuw[i])
            else:
                j = i
                if lijst[i - 1] > lijst[i]:
                    lijst[j - 1], lijst[j] = lijst[j], lijst[j - 1]
                    j -= 1
            i += 1
        return lijst
        print(lijst)
    

def binary_search(lijst, target, start, end):
    if start >= end: #lege lijst dan zeker dat element niet vookomt #BASECASE
        return -1
    mid = (start+end)//2
    if lijst[mid] == target:
        return mid
    elif lijst[mid] < target:
        # mid zelf niet meer beschouwen, want sws verschillend van target
        return binary_search(lijst, target, mid+1, end)
    else: #lijst[mid] > target
        # hier niet mid-1 schrijven, want end was exclusief
        return binary_search(lijst, target, start, mid)

lijst = list(range(0, 10))
nieuw = [20, 18, 10, 6, 15, 3, 9, 7, 11, 20, 9, 5, 12, 8, 17]
efficient_insertion_sort(lijst, nieuw)
print("Gesorteerde : ", )
