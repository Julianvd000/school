def standaardtarief(afstandKM):
    if (afstandKM < 0):
        afstandKM = 0
    if (afstandKM > 50):
        return 15 + (afstandKM * 0.60)
    return afstandKM * 0.80

#2
def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardprijs = standaardtarief(afstandKM)
    if (leeftijd < 12) | (leeftijd >= 65):
        if (weekendrit):
            standaardprijs = standaardprijs * 0.65
        else:
            standaardprijs = standaardprijs * 0.7
    else:
        if (weekendrit):
            standaardprijs = standaardprijs * 0.60
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