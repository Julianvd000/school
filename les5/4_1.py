

def graduate():
    score = int(input('geef je score:'))
    if(score > 15):
        print(
            "Gefeliciteerd!\nMet een score van "
            + str(score) + " ben je geslaagd!"
        )
    else:
        print(
            "Helaas \n Met een score van "
            + str(score) + " ben je gezakt!"
        )

graduate()