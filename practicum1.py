# 2 of minder scores -> geen resultaten
# 3 -> enkel gemiddelde

# geen input validatie op scores (integers <= 20) en '-1' als sentinel

# geldige score tussen O en 10 (beiden inbegrepen)
# andere ingegeven waardes worden niet meegenomen in berekening

# geen resultaat voor een een eigenschap -> waarde -1

# Voor gemiddelde afronden op 2 cijfers na komma met round() functie

# Bij min en max wordt de hoogste/laagste waarde maar 1 keer geteld

###########################START#####################"

# Initialisation
sum = 0
count = 0
average = -1
lowest = -1
highest = -1
second_lowest = 11
second_highest = -1

## Ask input from user and testing for valid score
# We testen eerst 2 gevallen om highest, second_highest, lowest en second_lowest
# te bepalen en vervolgens voegen we scores in in de while-loop
# Dit alles wordt uitgevoerd tot sentinel '-1' wordt ingevoerd

# Defining highest and lowest, first input score
score = int(input())
while score != -1 and (score < 0 or score > 11):
    score = int(input())

if score != -1:
    highest = score
    lowest = score
    count += 1
    sum += score
    average = round(sum / count, 2)

    # Defining second_highest and second_lowest and
    # redefining highest and lowest, second input score
    score = int(input())
    while (score != -1) and (score < 0 or score > 11):
        score = int(input())
    if score != -1:
        if score > highest:
            second_highest = highest
            highest = score
        elif score != highest:
            second_highest = score
        if score < lowest:
            second_lowest = lowest
            lowest = score
        elif score != lowest:
            second_lowest = score
        count += 1
        sum += score
        average = round(sum / count, 2)

        # While-loop untill sentinel '-1' calculating average, second_highest
        # and second_lowest
        score = int(input())
        while score != -1:
            if 0 <= score <= 10:
                count += 1
                sum += score
                average = round(sum / count, 2)
                if score > highest:
                    second_highest = highest
                    highest = score
                elif score > second_highest and score != highest:
                    second_highest = score
                if score < lowest:
                    second_lowest = lowest
                    lowest = score
                elif score < second_lowest and score != lowest:
                    second_lowest = score

            score = int(input())
# Making sure that second_highest != second_lowest
if second_highest == second_lowest == highest == lowest:
    second_lowest = -1
    second_highest = -1

# Testing if there is a second_lowest value
if second_lowest == 11:
    second_lowest = -1


## Testing if there are enough scores
# Only 2 or less scores
# -> (average, second_lowest, second_highest) = (-1,-1,-1)
if count <= 2:
    average = -1
    second_lowest = -1
    second_highest = -1

# Only 3 scores
# -> (average, second_lowest, second_highest) = ((round(sum/3), 2), -1, -1)
elif count == 3:
    second_lowest = -1
    second_highest = -1

# Print result
print(average,second_lowest,second_highest)



