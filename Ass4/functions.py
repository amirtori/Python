def fahrenheit():
    x = int(input("Insert a number to convert Fahrenheit into Celcius:""\n" ))
    celcius = (x  -  32)  *  5/9
    print("%.2f" " Fahrenheit" % celcius,"is" ,x, "Celcius")

def celcius():
    x = int(input("Insert a number to convert Celcius into Kelvin:""\n"))
    kelvin = x + 273
    if kelvin <= 0:
        kelvin = 0
        print (kelvin," kelvin is the absolute zero")
    elif kelvin > 0:
            print(x,"Celcius is", kelvin, "Kelvin")

def absolute():
    x = int(input("enter a number to convert it into an absolute number:""\n"))
    if x < 0:
        x = 0 - x
        print(x, "is the absolute number")
    else:
        print(x, "is the absolute number")

def rpsls():
    from random import randint
    options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    computer = options[randint(0,4)]
    player = True
    pscore = 0
    cscore = 0

    while player == True:
        player = input('\n' + "Rock, Paper, Scissors, Lizard, Spock?" +"\n")
        if player == computer:
            print("Its a tie! "+player+ " equals " +computer, "the score =", "Player",pscore, "-", "Computer", cscore)
        elif player == "Rock":
            if computer == "Paper" or computer == "Spock":
                cscore += 1
                print("You lose!", computer, "beats", player,"the score =", "Player",pscore, "-", "Computer", cscore)
            else:
                pscore += 1
                print("You win!", player, "beats", computer,"the score =", "Player",pscore, "-", "Computer", cscore)
        elif player == "Paper":
            if computer == "Scissors" or computer == "Lizard":
                cscore += 1
                print("You lose!", computer, "beats", player,"the score =", "Player",pscore, "-", "Computer", cscore)
            else:
                pscore += 1
                print("You win!", player, "beats", computer,"the score =", "Player",pscore, "-", "Computer", cscore)
        elif player == "Scissors":
            if computer == "Rock" or computer == "Spock":
                cscore += 1
                print("You lose!", computer, "beats", player,"the score =", "Player",pscore, "-", "Computer", cscore)
            else:
                pscore += 1
                print("You win!", player, "beats", computer,"the score =", "Player",pscore, "-", "Computer", cscore)
        elif player == "Lizard":
            if computer == "Rock" or computer == "Scissors":
                cscore += 1
                print("You lose!", computer, "beats", player,"the score =", "Player",pscore, "-", "Computer", cscore)
            else:
                pscore += 1
                print("You win!", player, "beats", computer,"the score =", "Player",pscore, "-", "Computer", cscore)
        elif player == "Spock":
            if computer == "Paper" or computer == "Lizard":
                cscore += 1
                print("You lose!", computer, "beats", player,"the score =", "Player",pscore, "-", "Computer", cscore)
            else:
                pscore += 1
                print("You win!", player, "beats", computer,"the score =", "Player",pscore, "-", "Computer", cscore)
        elif player =="exit":
            exit()
        else:
            print("You didn't spell it right!")
        player = True
        computer = options[randint(0,4)]
