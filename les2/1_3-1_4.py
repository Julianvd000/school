a = 6
b = 7
c = float((a + b)/2)
print(c)


voornaam = 'Julian'
tussenvoegsel = 'van'
achternaam = 'Dijk'
mijnnaam = voornaam + ' ' + tussenvoegsel + ' ' + achternaam
print(mijnnaam)

d = a < 75 < b
print(d)
print(mijnnaam.__len__() == (voornaam.__len__() + tussenvoegsel.__len__() + achternaam.__len__()))
print(mijnnaam.__len__() > 5*tussenvoegsel.__len__())
print(tussenvoegsel in achternaam)