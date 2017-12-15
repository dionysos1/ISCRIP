def rooster(getal: int, spoor: str):

    # check of de opgegeven string correct is
    # maak het rooster aan
    if len(spoor) % getal == 0:
        t = 0
        lijst2 = []
        for x in range(getal):
            lijst = []
            for y in range(getal):
                lijst.append(spoor[t])
                t += 1
            lijst2.append(lijst)
            x += 1
        return lijst2
    # vang de Assertion Error af
    else:
        raise AssertionError("ongeldige argumenten")
        # return print("Assertion Error: ongeldige argumenten")


def tekst(lijst: [[]]) -> str:
    # zet de lijst om naar tekst om te laten zien op meerdere regels
    output = ""
    for row in lijst:
        for cell in row:
            output += cell + " "
        output += "\n"
    return output


def stap(lijst: [[]], coordinaat: tuple):

    coX = coordinaat[0]
    coY = coordinaat[1]
    lijstX = lijst[coordinaat[0]]
    tekentje = lijstX[coordinaat[1]]
    array = ['v', '<', '^', '>']
    index = 0
    for x in range(len(array)):
        if tekentje == array[x]:
            index = x
    newCoordinaat = (0, 0)

    # ga 1 stap verder
    # en verander icoontje 90 graden met klok mee
    if tekentje == 'v' and coX < len(lijst)-1:
        newCoordinaat = (coX + 1, coY)
        lijstX[coordinaat[1]] = '<'
    elif tekentje == '^'and coX > 0:
        newCoordinaat = (coX - 1, coY)
        lijstX[coordinaat[1]] = '>'
    elif tekentje == '>' and coY < len(lijst)-1:
        newCoordinaat = (coX, coY + 1)
        lijstX[coordinaat[1]] = 'v'
    elif tekentje == '<' and coY > 0:
        newCoordinaat = (coX, coY - 1)
        lijstX[coordinaat[1]] = '^'
    # als hij out of bounds wil gaan blijf op dezelfde plek
    else:
        newCoordinaat = (coX, coY)
        if index < 3:
            lijstX[coordinaat[1]] = array[index + 1]
        else:
            lijstX[coordinaat[1]] = array[0]

    return newCoordinaat


def stappen(lijst: [[]]):
    # probeer naar het nest op 0,3 te komen.
    coordinaat = stap(lijst, (3, 0))
    stappenlijst = [(3, 0)]
    while coordinaat != (0, 3):
        stappenlijst.append(coordinaat)
        coordinaat = stap(lijst, coordinaat)
    stappenlijst.append(coordinaat)
    return stappenlijst


def main() -> None:
    # zoals het voorbeeld
    vierkant = rooster(4, '>>>>^<^v^v^^>>v>')
    print(tekst(vierkant))
    print(stap(vierkant, (3, 0)))
    print(tekst(vierkant))
    print(stap(vierkant, (3, 1)))
    print(tekst(vierkant))

    vierkant = rooster(4, '>>>>^<^v^v^^>>v>')
    print(tekst(vierkant))
    print(stappen(vierkant))
    print(tekst(vierkant))

    rooster(4, '>>>>^<^v^v^>>v>')

try:
    main()
except AssertionError:
    print("Assertion Error: Ongeldige argumenten")
