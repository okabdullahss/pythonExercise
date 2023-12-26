import string


def display(r1, r2, r3):
    print(r1)
    print(r2)
    print(r3)


def askInput():
    userInput = 0
    within_range = range(1, 4)
    while True or userInput not in within_range:
        try:
            userInput = int(input("Enter a number between 1 and 3"))
        except ValueError:
            print("Not an integer!")
            continue
        else:
            break
    return userInput


def quit():
    selection = input("Please press 5 to quit, to continue press something else")
    return selection == "5"


def tictactoe():
    print("Welcome to Tick Tack Toe Game")

    row1 = ["_", "_", "_"]
    row2 = ["_", "_", "_"]
    row3 = ["_", "_", "_"]
    print("Heres the game board")
    display(row1, row2, row3)

    while True:

        if quit():
            break
        row = askInput()
        column = askInput()



        if 4 > int(row) > 0 and 4 > int(column) > 0:
            print(f'Heres the new board with selected row:{row} and column:{column}')
            if row == 1:
                row1[int(column) - 1] = "X"
            elif row == 2:
                row2[int(column) - 1] = "X"
            elif row == 3:
                row3[int(column) - 1] = "X"
            # if row1[0] == row1[1] == row1[2] == "X":
            #     row1 = ["--", "--", "--"]
            # elif row2[0] == row2[1] == row2[2] == "X":
            #     row2 = ["--", "--", "--"]
            # elif row3[0] == row3[1] == row3[2] == "X":
            #     row3 = ["--", "--", "--"]
            # elif row1[0] == row2[1] == row3[2] == "X":
            #     row1[0] = row2[1] = row3[2] = "--"
            # elif row1[2] == row2[1] == row3[0] == "X":
            #     row1[2] = row2[1] = row3[0] = "--"
            display(row1, row2, row3)


        else:
            print("Wrong numbers selected, please select within the given range of 1 & 3")


tictactoe()
