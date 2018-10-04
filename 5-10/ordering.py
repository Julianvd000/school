invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

lst = invoer.split('-')
lst.sort()
lst = list(map(int, lst))

print("Gesorteerde list van ints: {}".format(lst))
print("Grootste getal: {} en Kleinste getal: {}".format(max(lst), min(lst)))

print("Aantal getallen: {} en Som van de getallen: {}".format(len(lst), sum(lst)))
print("Gemiddelde: {}".format(sum(lst) / len(lst)))
