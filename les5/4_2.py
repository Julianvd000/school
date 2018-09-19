def allowedToVote():
    leeftijd = int(input('Enter age:'))
    print('Do you have password \n')
    pasport = bool(input('yes or no'))

    if(leeftijd >= 18 and pasport == True):
        print('je mag stemmen')
    else:
        print('je mag niet stemmen')

allowedToVote()