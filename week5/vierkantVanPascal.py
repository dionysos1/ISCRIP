def vierkant (rijgrootte, getal=1) -> [[]]:
    # maak lijstjes aan om het viekant in op te slaan
    alles = []
    lijst = []

    # vul de eerste rij met het getal
    for y in range(rijgrootte):
        lijst.append(getal)

    # vul rij 2 met telkens het getal van links en boven in het grid
    # en voeg daarna de lijst toe aan de grote lijst met alle lijsten.
    for z in range(rijgrootte):
        newlijst = [getal]

        for x in range(rijgrootte-1):
            newlijst.append(lijst[x+1] + newlijst[x])
        alles.append(lijst)
        lijst = newlijst
    return alles


def paden(rijgrootte, getal=1) -> str:
    # haal de tekst op uit de vierkant functie
    tekst = ''
    vierkantje = vierkant(rijgrootte, getal)
    # haal op hoe lang het laatste getal is
    laatsteInLijst = vierkantje[rijgrootte - 1]
    p = len(str(laatsteInLijst[rijgrootte - 1])) + 1
    # loop door alle getallen heen en zet het allemaal op 1 grote regel,
    # gescheiden door de lengte +1 van het laatste getal p
    for x in vierkantje:
        for y in x:
            tekst += '{:{align}{width}}'.format(str(y), align='>', width=p)
        tekst += '\n'
    return tekst

# print de voorbeelden
vierkant(3, 100)
vierkant(4)

print(paden(3))
print(paden(3, 100))
print(paden(4))
print(paden(6))
print(paden(8))
print(paden(10))
