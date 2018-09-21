cijferICOR = int(input("vul cijfer van icor in: "))
cijferPROG = int(input("vul cijfer van prog in: "))
cijferCSN = int(input("vul cijfer van csn in"))
gemiddelde = 0



def gemiddelde():
    total = cijferCSN + cijferICOR + cijferPROG
    gemiddelde = total / 3

def saldo():
    gemiddelde()
    print( 'Mijn cijfers (gemiddeld een '
        + str(gemiddelde) +
        ') leveren een beloning van € '
        + str(gemiddelde*30) + ' op!'
    )


saldo()
