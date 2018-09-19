def new_password(newpassword, oldpassword ):
    if(newpassword == oldpassword ):
        return False

    if(len(newpassword) > 6):
        for x in newpassword:
            if(x in '1234567890'):
                return True
            else:
                return 'Je hebt de juiste lengte maar je wachtwoord bevat geen cijfer van 0-9'
    else:
        return False

print(new_password('markteds', 'markteds'))
print(new_password('markteds1', 'markteds'))
