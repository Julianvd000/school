input = eval(input("Geef lijst met minimaal 10 strings: "))
output = []
if(len(input) >= 10):
    for i in input:
        if(len(i) == 4):
            output.append(i)
    print('De nieuw-gemaakte lijst met alle vier-letter strings is:')
    print(output)
