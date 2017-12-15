def levensverwachting(geslacht: str, roker: bool, sport: int, alcohol: int, fastfood: bool)->float:

    verwachteLeeftijd = 70

    # bij vrouwen wordt er vier jaar bijgeteld
    if geslacht == "vrouw":
        verwachteLeeftijd += 4

    # bij rokers wordt er vijf jaar afgetrokken en bij niet-rokers wordt er vijf jaar bijgeteld
    if roker:
        verwachteLeeftijd -= 5
    else:
        verwachteLeeftijd += 5

    # trek drie jaar af voor personen die nooit sporten en tel één jaar bij voor elk uur dat iemand wekelijks aan sport doet
    if sport == 0:
        verwachteLeeftijd -= 3
    else:
        verwachteLeeftijd += sport

    # trek een half jaar af voor elk geconsumeerd glas alcohol boven de zeven dat iemand per week drinkt
    # (bij iemand die elf glazen alcohol per week drinkt worden dus twee jaren afgetrokken);
    # bij geheelonthouders wordt er twee jaar bijgeteld

    if alcohol == 0:
        verwachteLeeftijd += 2
    if alcohol > 7:
        alcohol -= 7
        verwachteLeeftijd -= (alcohol * 0.5)

    # bij een persoon die niet vaak fastfood eet wordt 3 jaar bijgeteld.
    if not fastfood:
        verwachteLeeftijd += 3

    return verwachteLeeftijd


# print de verschillende invoer uit het voorbeeld.
print("De uitvoer uit het voorbeeld:")
print(levensverwachting(geslacht='man', roker=True, sport=2, alcohol=10, fastfood=True))
print(levensverwachting(geslacht='man', roker=True, sport=5, alcohol=5, fastfood=True))
print(levensverwachting(geslacht='vrouw', roker=False, sport=5, alcohol=0, fastfood=False))
print(levensverwachting(geslacht='vrouw', roker=False, sport=3, alcohol=14, fastfood=True))
print(levensverwachting(geslacht='man', roker=False, sport=4, alcohol=4, fastfood=False))

print(input("Wilt u zelf nog wat testen ? Druk dan op enter"))
print(levensverwachting(str(input("geslacht (man of vrouw): ")), bool(input("roker 1 of 0: ")), int(input("sport uren in de week: ")), int(input("alcohol glazen per week: ")), bool(input("fastfood eten 1 of 0: "))))


