with open('kaartnummers.txt', 'r') as f:
    line = []
    for l in f:
        line.append(l.split(','))

    for l in line:
        l[1] = l[1].replace('\n', '')
        print("{} heeft kaartnummer: {}".format(l[1], l[0]))
    f.close()
