from string import punctuation


def password_strength(password: str)->int:

    score = 0

    # het wachtwoord is minstens 8 karakters lang
    if len(password) >= 8:
        score += 1

    # het wachtwoord bevat minstens één hoofdletter,
    if len([x for x in password if x == x.upper()]) > 0:
        score += 1

    # het wachtwoord bevat minstens één kleine letter,
    if len([x for x in password if x == x.lower()]) > 0:
        score += 1

    # het wachtwoord bevat minstens één cijfer,
    if len([x for x in password if x.isdigit()]) > 0:
        score += 1

    # het wachtwoord bevat minstens één speciaal karakter dat geen letter of cijfer is.
    if len([x for x in password if x in punctuation]) > 0:
        score += 1

    return score


number = int(input("Aantal te testen wachtwoorden: "))
passwords = []

for i in range(0, number):
    passwords.append(input("Wachtwoord {0} ".format(i + 1)))

for password in passwords:
    print("Wachtwoord - {0} - is {1} met een score van {2}".format(password, ["zwak", "zwak", "zwak", "matig", "matig", "sterk", "sterk"][password_strength(password)], password_strength(password)))

