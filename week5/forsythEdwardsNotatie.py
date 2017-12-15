def fen2grid(fen: str, emptysign='*') -> str:
    # je krijgt een string binnen die een 8x8 grid voor moet stellen
    string = ''
    rows = fen.split('/')
    expectedRows = 0
    # loop door elke letter heen
    for x in rows:
        for y in x:
            if y.isdigit():
                # is het een nummer? zet er het tekentje neer van emptysign keer het aantal dat er staat.
                string += (emptysign * int(y))

            else:
                string += y
        expectedRows += 1
        # zodra je de 8 hebt berijkt zet een enter neer.
        if expectedRows != len(rows):
            string += '\n'
    return string


def grid2fen(grid: str, emptysign='*') -> str:
    # je krijgt een grid binnen met enters erin.
    string = ''
    teller = 0
    # splits het grid op bij elke enter
    rows = grid.split('\n')
    expectedRows = 0
    # loop door de rijen heen en zet het netjes achter elkaar.
    for x in rows:
        for y in x:
            # als er een emptysign tekentje staat zet een teller omhoog.
            if y == emptysign:
                teller += 1

            if not y == emptysign:
                if teller != 0:
                    # zet het nummer van de teller neer in de string
                    string += str(teller)
                string += y
                teller = 0
        # als na de loop de teller geen 0 is. zet hem achter de string en reset hem.
        if teller != 0:
            string += str(teller)
        teller = 0
        expectedRows += 1
        if expectedRows != len(rows):
            string += '/'
    return string

# laat het voorbeeld zien.
print(fen2grid('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR') + '\n')
print(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR', '.') + '\n')
print(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '+') + '\n')

rooster = '''rnbqkbnr
pppppppp
********
********
********
********
PPPPPPPP
RNBQKBNR'''
print(grid2fen(rooster))

print(grid2fen(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR')))
print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR', '.'), '.'))
print(grid2fen(fen2grid('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R', '+'), '+'))
