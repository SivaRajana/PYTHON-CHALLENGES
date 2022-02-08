password = input()
upperCaseTest = (password != password.lower())
lowerCaseTest = (password != password.upper())
digitTest = False
for i in password:
    if (i.isdigit()):
        digitTest = True
        break
if (upperCaseTest and lowerCaseTest and digitTest):
    print ("Valid Password")
else:
    print ("Invalid Password")
