
if __name__ == '__main__':
    myString = "abcdefghijk"

    print("index2 is: "+ myString[2]) # print the value on index2

    print("reverse index3 is: "+ myString[-3]) #prints the value of index starting from last value being -1

    print("substring starting from index2 inluding is: "+myString[2:])  #prints the value of substring starting from index2(included) and the rest

    print("substring starting from 0 up to the index4 excluded is: "+ myString[:4])

    print("substring starting from index2 inlcluded and index 5 excluded, with step size of 2 is: "+myString[2:5:2])

    print("REVERSE OF STRING IS: "+ myString[::-1])

# -----------------------------immutableitiy and concatination------------------------------------------------------------------------


    letter = "z"

    newLetter = letter*10
    print("new letter is = "+newLetter)


    x = "Hello World"

    print(x.upper()) #REMEMBER THIS DOES NOT REASSING THE x . IF YOU WANT X TO BE PERMENANTLY UPPERCASE YOU HAVE TO x = x.upper()
    print(x.lower())
    print(x.capitalize())
    print(x.endswith("ld"))
    print(x.startswith("Hel"))
    print(x.isnumeric())

    myList = x.split("l")
    print(myList)

    # -----------------------------String Formatting------------------------------------------------------------------------

    str1 = "Fox is quick {}".format("INSERTED")
    print(str1)

    str2 = "Fox is {} {} {}".format("helpful", "orange", "fast")
    print(str2)
    str2 = "Fox is {2} {1} {0}".format("first","second","third")
    print(str2)


    results = 100/777
    print("Results was {0:1.4f}".format(results))

    name = "Jose"

    print("His name is {}".format(name))
    print(f"his name is {name}")



















