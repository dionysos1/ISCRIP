def naarT9(char: str):

    # beschrijf alle opties op het GSM toetsenbord
    if char in "ABC":
        return 2
    if char in "DEF":
        return 3
    if char in "GHI":
        return 4
    if char in "JKL":
        return 5
    if char in "MNO":
        return 6
    if char in "PQRS":
        return 7
    if char in "TUV":
        return 8
    if char in "WXYZ":
        return 9
    return 0


def invoerT9(invoer: str):
    uitvoer = ''
    invoer = invoer.upper()

    # ga langs alle letters en vraag het nummer er van op
    for nummer in invoer:
        uitvoer += uitvoer.join(str(naarT9(nummer)))

    return uitvoer


def GSMoniem(invoer1: str, invoer2: str)->bool:
    return invoerT9(invoer1) == invoerT9(invoer2)

# gebruiker kiest wat hij wil doen
gebrInvoer = int(input("wilt u de t9 invoer weten (1) of 2 teksten vergelijken (2)\r\n"))
if gebrInvoer == 1:
    print(invoerT9(input("Voer uw tekst in: ")))
if gebrInvoer == 2:
    print(GSMoniem(input("woord 1: "), input("woord 2: ")))

