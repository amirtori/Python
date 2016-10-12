def reverse():
    reverse = ""
    text = input("Enter String: ")
    for i in range(len(text), 0, -1):
        reverse += text[i-1]
    print (reverse)

def password():
    userinput = input("type your password: ")
    inputlength = len(userinput)
    weak = ("your password is weak")
    average = ("your password is average")
    strong = ("your password is strong")
    score           = 0
    kleineletter    = True
    hoofdletter     = True
    special         = True
    nummer          = True

    if inputlength > 7:
        score += 2
    elif inputlength < 8:
        score += 1

    for i in userinput:
        a = ord(i)
        if a >= 97 and a <= 122 and kleineletter == True:
            score += 1
            kleineletter = False
        elif a >= 65 and a <= 90 and hoofdletter == True:
            score += 1
            hoofdletter = False
        elif a >= 33 and a <= 47 and special == True:
            score += 1
            speciaal = False

        elif a >= 48 and a <= 57 and nummer == True:
            score += 1
            nummer = False

    if score < 4:
        print(weak)
    elif score == 4 or score == 5:
        print(average)
    elif score >= 6:
        print(strong)

def cryptography():
    x  = input("Enter a word: ")
    begin = 97
    end = 122
    n = int(input("Enter a number between 1 and 52: "))
    for i in (x):
        a = ord(i)
        total = a + n
        if (97 <= total < 122 or 65 <= total < 90) and n >= 0 and n <= 52:
            a = a + (n % 26)
            print(chr(a), end="")
        elif n > 52:
            print("please enter a number between 1 and 52""\n")
            break
        else:
            a = a + (n % -26)
            print(chr(a), end="")
