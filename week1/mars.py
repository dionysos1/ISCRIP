import math

#gebruiker voert het aantal sol dagen in die hij wil weten in mars dagen
input = int(input("aantal hele dagen in sol: "))

# zet het aantal sol om in mars seconden

# methode 1
# seconds = (input * 35.244) + (input * 60 * 39) + (input * 60 * 60 * 24)

# methode 2
seconds = (input * 86400) * 1.02749125170

# kijk hoe vaak dagen in het aantal seconden passen en het daarna van het geheel aftrekken.
days = math.floor(seconds / (60*60*24))
seconds -= (60*60*24) * days

# kijk hoe vaak uren in het overig aantal seconden passen en het daarna van het geheel aftrekken.
hrs = math.floor(seconds / (60*60))
seconds -= 3600 * hrs

# kijk hoe vaak minuten in het overig aantal seconden passen en het daarna van het geheel aftrekken.
mins = math.floor(seconds / 60)
seconds -= 60 * mins

print("{0} sol = {1} dagen {2} uren {3} minuten {4} seconden".format(input, days, hrs, mins, round(seconds)))