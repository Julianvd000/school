def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


def table(celsius):
    print('{:>6}'.format('F') + '{:>12}'.format('C'))
    for i in range(8):
        fahrenheit = convert(celsius)
        print('{:>6}'.format(fahrenheit) + '{:>12}'.format(float(celsius)))
        celsius += 10

celsius = -30
table(celsius)
