uren = int(input('Het aantal gewerkte uren: '))
uurloon = float(input('uurloon: '))

total = uren * uurloon

print(
    'Wat verdien je per uur:'+ str(uurloon) + '\n' + 'Hoeveel uur heb je gewerkt: '  + str(uren) + '\n' + str(uren) +  'uur werken levert ' + str(total) + ' Euro op'
    )