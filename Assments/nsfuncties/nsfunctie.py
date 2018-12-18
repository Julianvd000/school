volwassenweekendprijs = 0.65
volwassennoweekendprijs = 0.7
novolwassenweekendprijs = 0.60

minimaleleeftijd = 12
maximaleleeftijd = 65

def standaardtarief(afstandKM):
    if (afstandKM < 0):
        afstandKM = 0
    if (afstandKM > 50):
        return 15 + (afstandKM * 0.60)
    return afstandKM * 0.80

#2
def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardprijs = standaardtarief(afstandKM)
    if (leeftijd < minimaleleeftijd) | (leeftijd >= maximaleleeftijd):
        if (weekendrit):
            standaardprijs = standaardprijs * volwassenweekendprijs
        else:
            standaardprijs = standaardprijs * volwassennoweekendprijs
    else:
        if (weekendrit):
            standaardprijs = standaardprijs * novolwassenweekendprijs
    return standaardprijs

#3
for age in [11, 12, 64, 65]:
    print('leeftijd: ' + str(age))
    print('het is weekend en 30km reizen ' + str(ritprijs(age, True, 30)))
    print('het is geen weekend en 30km reizen ' + str(ritprijs(age, False, 30)))
    print('het is weekend en 70km reizen ' + str(ritprijs(age, True, 70)))
    print('het is geen weekend en 70km reizen ' + str(ritprijs(age, False, 70)))
    print('het is weekend en -3km reizen ' + str(ritprijs(age, True, -3)))
    print('het is geen weekend en -3km reizen ' + str(ritprijs(age, False, -3)))
    print(' ----- ')
