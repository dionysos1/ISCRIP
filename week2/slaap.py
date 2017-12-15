from datetime import datetime, timedelta

# gebruiker voer uur en minuut in waarin hij naar bed gaat.
invoerUur = input("Voer het huidige uur in:")
invoerMinuut = input("voer de huidige minuut in: ")

# gebruiker voert uur en minuut in waarin hij uit zijn bed wil.
invoerUurEruit = input("Voer wakker wordt uur in: ")
invoerMinuutEruit = input("Voer wakker wordt minuut in: ")

# zet de invoer om in 1 string die de datetime functie kan gebruiken.
erIn = datetime.strptime(invoerUur + ":" + invoerMinuut, '%H:%M')

# zet de invoer om in 1 string die de datetime functie kan gebruiken en voeg toe dat hij overweg kan met extra dagen na 24 uur.
erUit = (datetime.strptime(invoerUurEruit + ":" + invoerMinuutEruit, '%H:%M') + timedelta(days=1))

# vergelijk de 2 strings van tijden met elkaar.
# ga je later uit bed dan dat je erin gaat. Dus de volgende dag. Dan telt hij daar iig 90 minuten bij op.
# dit doet hij tot je over je ingevoerde tijd heengaat dat je eruit wilde gaan.
while True:
    if erUit < erIn:
        print("het beste tijdstip dat je wakker kan worden is: " + datetime.strftime(erIn, '%H:%M'))
        break

    erIn += timedelta(minutes=90)
