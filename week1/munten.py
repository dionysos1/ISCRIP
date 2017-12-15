aantal = 0
totaal = 0.0
muntArray = [1, 2, 5, 10, 20, 50, 100, 200]

for waarde in muntArray:
    invoer = int(input("Aantal munten met waarde {0} ct: ".format(waarde)))
    aantal += invoer
    totaal += (waarde * invoer) / 100

print("Totaal aantal munten: {0}\r\nTotale waarde van {1} euro".format(aantal, round(totaal, 2)))