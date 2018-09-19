cijferICOR = input()
cijferPROG = input()
cijferCSN = input()
gemiddelde = int



def gemiddelde():
    total = cijferCSN + cijferICOR + cijferPROG
    gemiddelde = total / 3

def saldo():
    gemiddelde()
    print( 'Mijn cijfers (gemiddeld een '
        + gemiddelde +
        ') leveren een beloning van € '
        + gemiddelde*30 + ' op!'
    )


saldo()