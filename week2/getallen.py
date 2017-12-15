# bereken de som van de cijfers in een getal
def somGetal(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


# Check de oplossing tegen somGetal(n) == n
def sum(n, y):

    testgeval = n

    # loop door de mogelijk heden heen. maar stop bij 10000
    while testgeval <= y:
        temp = testgeval

        if somGetal(temp) == n:
            return testgeval

        testgeval += n

    return "geen uitkomst gevonden"

# vraag de gebruiker om input.
nummers = []
print("Voer getallen in onder de 100 en maximaal 50 getallen.")
aantalGetallen = int(input("hoeveel getallen wilt u zien: "))

# check of er niet meer dan 50 getallen ingevoerd gaan worden.
if aantalGetallen > 50:
    print("foutieve invoer")
    exit(-1)

# Gebruiker voert zijn getallen in.
while len(nummers) < aantalGetallen:
    x = input("uw nummer: ")
    # als de gebruiker niets invult. stop de loop en begin met rekenen.
    if x == "":
        break

    # als er een verkeerd getal wordt ingevoerd meld dit aan de gebruiker en sluit de invoer.
    if 0 > int(x) > 100:
        print("Foutieve invoer")
        exit(-1)

    nummers.append(int(x))

# loop door alle nummers heen en check wat hun antwoord is.
for num in nummers:
    print(sum(num, 10000))
