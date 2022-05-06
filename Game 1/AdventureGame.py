# TODO
# Make a proper movement system
# Make it not return "None" in addition to the actual response

# Intro section ig
from os import close

running = True
print("Welcome to the Forest!")
userinput = input("Press Enter to Begin!\n")
level1map = print("LEVEL 1"
                  "\nWWWWWWWWWWWWWWWWW"
                  "\nW  X            W"
                  "\nW               W"
                  "\nW               W"
                  "\nW     0         W"
                  "\nW          X    W"
                  "\nW   X           W"
                  "\nWWWWWWWWWWWWWWWWW")


def loss():
    print("You somehow Lost!")


# Movement Stuff
def move_up():
    print("Die W")


def move_left():
    print("Die A")


def move_down():
    print("Die S")


def move_right():
    print("Die D")


# Map Stuff
def level1(lvl1input):
    print(level1map)
    if lvl1input == "w":
        return move_up()
    if lvl1input == "a":
        return move_left()
    if lvl1input == "s":
        return move_down()
    if lvl1input == "d":
        return move_right()
    if lvl1input == "q":
        loss()
        return close()


def getinput():
    return input("Enter W, A, S, or D to move and Q to quit: ")


while running == True:
    lvlinput = getinput().lower()
    level1(lvlinput)
