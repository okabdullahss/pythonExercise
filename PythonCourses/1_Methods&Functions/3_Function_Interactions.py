# create a simple game where user tries to guess the location of O
from random import shuffle

global guessedNumber
myList = [" ", "O", " "]


def user_guess():
    guess = ""
    while guess not in ["0", "1", "2"]:
        guess = input("Please provide a number 0, 1 or 2 ")
    return int(guess)

def shuffle_list(list):
    shuffle(list)
    return list


def guess_game(list):
    list = shuffle_list(list)
    userGuess = user_guess()
    if list[userGuess] == "O":
        print("Correct !")
        print(list)
    else:
        print("Wrong...")
        print(list)


guess_game(myList)
