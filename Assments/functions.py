from tkinter import *
root = Tk()
TopFrame = Frame(root)
TopFrame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

def set_first_screen():
    button1 = Button(TopFrame, text='Kluis openen')
    button1.pack(side=LEFT, pady=10)

    button2 = Button(TopFrame, text='Welke kluizen zijn vrij?')
    button2.pack(side=LEFT, pady=10)

    button3 = Button(TopFrame, text='Kluis terug geven')
    button3.pack(side=LEFT, pady=10)

    button4 = Button(TopFrame, text='Nieuwe kluis aanvragen')
    button4.pack(side=LEFT, pady=10)

def toon_aantal_kluizen_vrij():
    lijst = []
    result = []
    kluizen = open('kluizen.txt')
    reader = kluizen.readlines()

    for x in reader:
        if x != '\n':
            lijst.append(x.strip().split(';'))

    vrij = 12 - len(lijst)

    result.append('Er zijn ' + str(vrij) + ' kluizen vrij.')

    bezetteKluizen = []
    bezetteKluisnummer = []

    for x in lijst:
        bezetteKluisnummer.append((int(x[0])))
    for x in bezetteKluisnummer:
        if x in bezetteKluisnummer:
            bezetteKluizen.append(x)

    result.append("De kluisjes " + str(bezetteKluizen).strip("[").strip("]") + " zijn bezet.\n")
    return result
