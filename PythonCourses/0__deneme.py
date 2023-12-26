def askInput():
    userInput = 0
    while True:
        try:
            userInput = int(input("Enter a number between 1 and 3"))
        except ValueError:
            print("Not an integer!")
            continue
        else:
            break
    return userInput


print(askInput())
