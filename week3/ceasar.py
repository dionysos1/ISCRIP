from string import ascii_lowercase, ascii_uppercase


def rotVerschuiving(letter: str, shift: int) -> str:

    # check de ingevoerde letter en geef het verschoven nummer terug
    if letter in ascii_uppercase:
        return ascii_uppercase[((ascii_uppercase.index(letter) + shift) % 26)]
    elif letter in ascii_lowercase:
        return ascii_lowercase[((ascii_lowercase.index(letter) + shift) % 26)]
    else:
        return letter


def decode(invoer: str, shift: int) -> str:

    # ga alle letters langs en decodeer ze door de verschuiving.
    uitvoer = ''
    for nummer in invoer:
        uitvoer += uitvoer.join(rotVerschuiving(nummer, shift * -1))

    return uitvoer

# gebruiker voert zijn bericht in en hoeveel letters hij wil verschuiven.
message = input("Bericht: ")
verschuiving = int(input("Shift: "))

# print het gecodeerde bericht
print(decode(message, verschuiving))
