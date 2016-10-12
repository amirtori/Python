from Start import *
"""
This assignment uses a custom library.
For simplicity's sake we provide you with an interface that hides the complexity of that library.
The header and footer of this file are necessary for the correct execution of the program,
so make sure you don't remove them.

If you try to run this sample without altering it,
a white screen with a black triangle(pen) will be drawn in the middle.
We have provided several instructions for you to use in order to move the pen.
In addition, we have provided a function to change the color with which the pen draws,
and a function to check for input.

(i)    forward(amount)        - 'forward' moves the pen by 'amount' steps.
                                'amount' is of type Integer.

(ii)   turn(amount)           - 'turn' rotates the pen by 'amount' degrees.
                                'amount' is of type Integer.

(iii)  change_color_to(color) - changes the color of the pen into 'color'.
                                The possible colors are: black, green, blue and red
                                'color' is of type string.

(iiii) get()                  - Returns ASCII code of the keyboard input.
                                Check http://wikipedia.org/ASCII for the list of keycodes.
                                Try the following:
                                x = get()
                                print(x)

By combining 'forward' and 'turn'(even inside loops), you can draw lots of nice shapes!
Good luck, and have fun!
"""

def program():
    # Your code here
    x = get()
    if x == 119:
        forward(2)
    elif x == 97:
        turn(-15)
    elif x == 115:
        turn(180)
    elif x == 100:
        turn(15)
    elif x == 114:
        change_color_to("red")
    elif x == 103:
        change_color_to("green")
    elif x == 98:
        change_color_to("blue")
    elif x == 122:
        change_color_to("black")
    elif x == 101:
        exit()
    pass

print("Press the WASD keys to move the turtle"+"\n"+"Press the R,G,B,Z keys to change your color (Red, Green, Blue, Black)" + "\n"+"Press E to exit")
run(program)

from End import *
