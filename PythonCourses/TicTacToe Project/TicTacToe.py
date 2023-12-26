import logging


def get_user_input(var, current_player):
    print(f"{current_player}, your turn !")
    while True:
        response = input(f"Please Enter {var} between 1 and 3: ")

        if response.isdigit():
            if var == "row":
                if int(response) in range(1, 4):
                    return int(response), True
                else:
                    print(f"The input you entered '{response}' is not in between 1 and 3")
            else:
                if int(response) in range(1, 4):
                    return int(response) - 1, True
                else:
                    print(f"The input you entered '{response}' is not in between 1 and 3")

        else:
            print(f"Wrong type entered:  '{response}' is not an integer")
            return False


def get_input_value():
    while True:
        inputValue = input("Please select a value you want to pass in, X or O only: ")

        if inputValue.lower() not in ["x", "o"]:
            print(f"Wrong input selection '{inputValue}', please try again with only X or O ")
        else:
            print("You selection is: " + inputValue.upper())
            return inputValue.upper(), True


r1 = ['_', '_', '_']
r2 = ['_', '_', '_']
r3 = ['_', '_', '_']

previousSelections = []

board = [r1, r2, r3]


def tictactoe_table(row, column, usrInput):
    if checkBlank(row, column):
        previousSelections.append((row, column))
        if row == 1:
            r1[column] = usrInput
        if row == 2:
            r2[column] = usrInput
        if row == 3:
            r3[column] = usrInput
        for row in board:
            print(" ".join(row))
        return True
    else:
        logging.error(f"Error ! Row: {row} and Column: {column}, This spot has already been filled")
        return False


def askUser():
    current_player = ""
    indx = 0
    while not checkFinished(current_player):

        if indx % 2 == 0:
            current_player = "Player 1"
        else:
            current_player = "Player 2"

        row, booleanAnswer1 = get_user_input("row", current_player)
        col, booleanAnswer2 = get_user_input("column", current_player)
        value, booleanAnswer3 = get_input_value()
        booleanAnswerTictac = tictactoe_table(row, col, value)

        if booleanAnswer2 and booleanAnswer3 and booleanAnswer1 and booleanAnswerTictac:
            indx = indx + 1


def checkBlank(a, b):
    return (a, b) not in previousSelections


def checkFinished(player):

    for row in board:

        rows = all(element == row[0] for element in row)
        rowNotBlank = all(element != "_" for element in row)

    for x in range(len(board[0])):
        columns = all(row[x] == board[0][x] for row in board)
        colNotBlank = all(row[x] != "_" for element in row)

    for col in range(len(board[0])):
        diagonals = all(row[col] == board[0][col] for row in board)
        diagNotBlank = all(row[col] != "_" for element in row)

    if (rows and rowNotBlank) or (columns and colNotBlank) or (diagonals and diagNotBlank):
        print(f"{player} wins !")




askUser()
