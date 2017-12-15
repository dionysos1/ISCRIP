def aantalBuren(generatie: [[]], x: int, y: int) -> int:

    # Berekent het aantal nabijgelegen levende cellen.

    buren = 0
    # Alle posities om een punt.
    modifiers = [[-1, -1], [-1, 0], [-1, 1],
                 [0, -1], [0, 1],
                 [1, -1], [1, 0], [1, 1]]

    for modifier in modifiers:
        posX = x + modifier[1]
        posY = y + modifier[0]

        # Controleer of een positie binnen het veld valt
        if 0 <= posY < len(generatie) and 0 <= posX < len(generatie[0]):
            # Telt de levende cellen
            if generatie[posY][posX] == "X":
                buren += 1

    return buren


def toonGeneratie(generatie: [[]]) -> str:

    # Geeft het veld op een bepaalde manier weer.
    return "\r\n".join([str(" ".join(row)) for row in generatie])


def volgendeGeneratie(generatie: [[]]) -> [[]]:

    # Berekent de volgende generatie

    # Een veld met dode cellen
    nieuwe_generatie = [["O" for o in range(len(generatie[0]))] for i in range(len(generatie))]

    for y, row in enumerate(generatie):
        for x, cell in enumerate(row):
            buren = aantalBuren(generatie, x, y)

            # Alleen als een cel 2 of 3 buren heeft
            if cell == "X" and (buren == 2 or buren == 3):
                # Wordt een levende cel terug gezet op het bord
                nieuwe_generatie[y][x] = "X"

            # Of als er nog geen cel is en er 3 buren zijn
            if cell == "O" and buren == 3:
                # Wordt een levende cel terug gezet op het bord
                nieuwe_generatie[y][x] = "X"

    return nieuwe_generatie

# geef alles weer zoals de voorbeeld uitvoer
generatie = [["X", "O", "O", "O", "O", "O", "O", "O"] for x in range(0, 6)]
print(toonGeneratie(generatie))
print(aantalBuren(generatie, 0, 0))
print(aantalBuren(generatie, 1, 1))
print(aantalBuren(generatie, 2, 2))

for i in range(0, 4):
    print(toonGeneratie(generatie) + "\r\n")
    generatie = volgendeGeneratie(generatie)
