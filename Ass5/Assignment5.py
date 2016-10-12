from functions import *
comments = """
Press 1 for the option reverse:
Press 2 for the option password:
Press 3 for the option cryptography:"""
print (comments)
userinput = input()
loop = True
while loop == True:
    if userinput == "1":
        reverse()
    elif userinput == "2":
        password()
    elif userinput == "3":
        cryptography()
    print(comments)
    userinput = input()
