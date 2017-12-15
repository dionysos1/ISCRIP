import math

# vraag de gebruiker om invoer.
naam = input("Ronde land: ")
afstand = float(input("Afstand: "))
gemtijd = float(input("Gemiddelde tijd: "))

# aantal rondes is de maximale 120 minuten gedeeld door de gemidelde tijd in minuten.
rondes = math.ceil(120.0 / gemtijd)

# als de maximale rondes 305 km / de afstand overscheiden wil je dit veranderen naar het echt gereden rondes in km.
if rondes > (305 / afstand):
    rondes = math.ceil(305 / afstand)

# voor de uitzondering van monaco zetten we het aantal ronden automatisch op 78.
if naam.lower() == "monaco":
    rondes = 78

# print alles in het aangegeven formaat. Om het totaal aantal kilometers te krijgen doe je het aantal ronde keer de afstand.
print("De grote prijs van {0} wordt verreden over {1} ronden ({2} km)".format(naam, rondes, round(rondes * afstand, 3)))
