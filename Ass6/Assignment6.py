from functions import *
comments = """
Press 1 for the option Square:
Press 2 for the option HollowSquare:
Press 3 for the option HalfTriangle:
Press 4 for the option Osciles Triangle:
Press 5 for the option Circle:
Press 6 for the option Smiley:"""
print (comments)
userinput = input()
loop = True
while loop == True:
    if userinput == "1":
        square()
    elif userinput == "2":
        hollowsquare()
    elif userinput == "3":
        halftriangle()
    elif userinput == "4":
        otriangle()
    elif userinput == "5":
        circle()
    elif userinput == "6":
        smiley()
    print(comments)
    userinput = input()
