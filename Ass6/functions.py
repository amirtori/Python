def square():
    x = int(input("Enter a number: \n"))
    for i in range (x):
        text = ""
        for j in range (x):
            text = text +"#"
        print(text)

def hollowsquare():
    x = int(input("Enter a number: \n"))
    i = 0
    text = ""
    while (i < x):
        j = 0
        if(i == 0) or (i == x -1):
            while(j < x):
                text += "*"
                j += 1
        else:
            while(j < x):
                if(j == 0) or (j == x -1):
                    text += "*"
                else:
                    text += " "
                j += 1
        i += 1
        text += "\n"
    print(text)

def halftriangle():
    x = int(input("Enter a number: \n"))
    text = ""
    for i in range(x):
        text += "*"
        print(text)

def otriangle():
    x = int(input("Enter a number: \n"))
    text = 1
    for a in range(x):
        output=""
        space = x - (a+1)
        for i in range(space):
            output += " "
        for j in range(text):
            output += "*"
        print(output)
        text += 2

def circle():
    import math
    d = int(input("Voer een getal in: \n"))
    centerx = d/2
    centery = d/2
    for x in range(d+1):
        output = ""
        for y in range(d+1):
            distance = math.sqrt((centerx-x)**2 + (centery-y)**2)
            distance = math.ceil(distance)
            if(distance <= d/2):
                output += "#"
            else:
                output += " "
        print(output)

def smiley():
    import math
    diameter = int(input("Give me a number: "))
    eyeleft = int(diameter / 3)
    eyeright = int(diameter / 3 * 2)
    nose = int(diameter / 2)
    mouthleft = int(diameter / 3)
    mouthright = int(diameter / 3 * 2)
    locmouth = int(diameter / 3 * 2)
    centerx = diameter / 2
    centery = centerx

    for x in range(diameter + 1):
        output = ""
        for y in range(diameter + 1):
            distance = math.sqrt((centerx - x)**2 + (centery - y)**2)
            distance = math.ceil(distance)
            if distance == math.floor(diameter/2):
                output += "|"
            elif x == eyeleft  and y == eyeleft:
                output += "O"
            elif x == eyeleft and y == eyeright:
                output += "O"
            elif x == nose and y == nose:
                output += "^"
            elif y >= mouthleft and y <= mouthright and x == locmouth:
                output += "_"
            elif y == mouthleft - 1 and x == locmouth:
                output += "\\"
            elif y == mouthright + 1 and x == locmouth:
                output += "/"
            else:
                output += " "
        print(output)
