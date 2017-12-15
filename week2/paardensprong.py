def coordinates(positie: str)->tuple:

    # positie komt binnen als een positie op het schaakbord als een letter en een cijfer bijv. D6
    # het cijfer hoeft niets meer mee te gebeuren.
    x = int(positie[1])

    # van de letter maak ik ook een cijfer vanuit de ascii tabel
    y = ord(positie[0]) + 1

    # return dit als een tuple om er later los mee te kunnen rekenen.
    return x, y


def checker(begin: tuple, eind: tuple)->bool:
    # return een boolean of de L vorm gemaakt kan worden of niet. Richting maakt daarvoor niet uit.
    return (abs(begin[0] - eind[0]) == 2 and abs(begin[1] - eind[1]) == 1) or (abs(begin[0] - eind[0]) == 1 and abs(begin[1] - eind[1]) == 2)

# print een intro met uitleg
print("Voer eerst de beginpositie in en daarna de eindpositie van het schaakstuk.\nDeze invoer moet wel op het veld bestaan.\nGebruik dus A t/m H en 1 t/m 6")

# vraag de gebruiker om de posities
beginPos = input("De startpositie: ")
eindPos = input("De eindpositie: ")

# zet de posities om in ints om later te gebruiken in de methode checker.
begin = coordinates(beginPos.lower())
eind = coordinates(eindPos.lower())

#print de uitslag. Hierin wordt de ckeck functie aangeroepen om te kijken of de beweging wel valide is of niet.
print("De sprong kan {0}gemaakt worden van {1} naar {2}".format(["niet ", ""][checker(begin, eind)], beginPos, eindPos))
