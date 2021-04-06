"""
 In een bevraging moeten voetbalfans hun 3 
 favoriete voetbalteams kiezen (volgorde speelt geen rol). 
 De mogelijkheden zijn: "Bel", "Eng",“Ger", “Fra", 
 “Ita", “Spa" and “Cam". De resultaten zijn opgeslagen 
 in het bestand survey.txt. Zoek het antwoord op de 
 volgende vragen:
1. print de teams die door geen enkele fan gekozen zijn.
2. print het totaal aantal fans van wie zowel "Bel" als "
   Ger" een favoriet is.
3. maak een dictionary waarin je kan opzoeken 
   hoeveel fans voor elke combinatie van drie 
   teams hebben gekozen.
Hint: Je kan de volgende code gebruiken voor het lezen van informatie uit het bestand:
file=open("survey.txt","r") #hiermee open je het bestand enkel om het te lezen
for line in file.readlines(): # hiermee lees je het bestand lijn per lijn
	line=line.strip() # hiermee verwijder je het newline character	
	#hier kan je de lijn gebruiken in een functie
file.close() # sluit de file
"""
teamset_te_kiezen = {"Bel", "Eng", "Ger", "Fra", "Ita", "Spa", "Cam"}
teamset_gekozen = set()
aantal_Bel_en_Ger = 0
teamdictionary = {}

file=open("survey.txt","r") #hiermee open je het bestand enkel om het te lezen
for line in file.readlines(): # hiermee lees je het bestand lijn per lijn
	line=line.strip() # hiermee verwijder je het newline character
	#hier kan je de lijn gebruiken in een functie

	if line not in teamdictionary:
		teamdictionary[line] = 1
	else:
		teamdictionary[line] += 1

	teams = line.split(" ")
	if "Bel" in teams and "Ger" in teams:
		aantal_Bel_en_Ger += 1
	for team in teams:
		teamset_gekozen.add(team)

	niet_gekozen_teams = teamset_te_kiezen.difference(teamset_gekozen)

file.close() # sluit de file

print(niet_gekozen_teams)
print(aantal_Bel_en_Ger)
print(teamdictionary)