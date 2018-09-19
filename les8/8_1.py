def seizoen(maand):
    if (maand == 3 or maand == 4 or maand == 5 ):
        return 'lente'
    elif (maand == 6 or maand == 7 or maand == 8):
        return 'zomer'
    elif (maand == 9 or maand == 10 or maand == 11):
        return 'herfst'
    elif (maand == 12 or maand == 1 or maand == 2):
        return 'winter'

maand = int(input("geef maand nummer: "))

print(seizoen(maand))