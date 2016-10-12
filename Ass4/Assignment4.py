from functions import *
comments = """
Press 1 to convert fahrenheit into celcius:
Press 2 to convert celcius into kelvin:
Press 3 to calculate the absolute value of a number:
Press 4 to play RPSLS:"""
print (comments)
userinput = input()
loop = True
while loop == True:
    if userinput == "1":
        fahrenheit()
    elif userinput == "2":
        celcius()
    elif userinput == "3":
        absolute()
    elif userinput == "4":
        rpsls()
    print(comments)
    userinput = input()
