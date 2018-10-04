with open('kaartnummer.txt', 'r') as f:
    line = []
    for l in f:
        line.append(l.split(','))

    print('Deze file telt {} regels'.format(len(line)))
    max = max(line)

    i = 1
    for l in line:
        if(max == l):
            print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(l[0], i))
        i += 1
