import math


#write a functin that calculates the volume of a sphere
import string


def vol(r):
    return 4/3*(math.pi)*math.pow(r,3)

print(vol(2))

#write a function that returns whether the given number is within the provided range(all inclusive)

def is_range(num,low,high):
    if num in range(low,high+1):
        return print(f'{num} is in range between {low} and {high}')
    else:
        return print(f'{num} is in NOT range between {low} and {high}')

print(is_range(2,1,4))
print("------")
#write a function that takes a string param and calcualtes the number of upper and lower case letters

def numOfUpAndLow(str):
    uppersList = []
    lowersList = []

    # str  = str.replace(" ","")
    for x in str:
        if x.islower():
         lowersList.append(x)
        elif x.isupper():
            uppersList.append(x)
    print(f'lowerlist: {lowersList} and upperList: {uppersList}')
    return print(f'the number of lower letters is {len(lowersList)} and upper letters is {len(uppersList)}')

numOfUpAndLow("Hi my name is")
print("-----")
#Write a palindrome check function

def is_palindrome(str):
    asdf = ""
    list1 = [x for x in str if x !=" "]
    list1.reverse()
    for x in list1:
        asdf+=x
    return asdf == str.replace(" ","")


print(is_palindrome("nurses run"))
print(is_palindrome("helleh"))

print("-----")
#write a fucn that return if the given str includes all the words in the alphabet (PANGRAM)

alphbet = string.ascii_lowercase

#1st solution / REMOVING existing elements and verifying empty list
def is_pangram(str):
    list1 = [x.lower() for x in str if x!=" "]
    set2 = set(list1)
    set3 = set(set2)
    for x in set3:
        if x in alphbet:
          set2.remove(x)

    return not set2

print(is_pangram("The quick brown fox jumps over the lazy dog"))

#2nd solution adding existing elements to the new list and verifying the length of new list is equal to alphabet lenght = 26
# def is_pangram(str):
#     list1 = [x for x in str if x!=" "]
#     list2 = []
#     for x in set(list1):
#         if x in alphbet:
#             list2.append(x)
#     return len(list2) == 26
#
# print(is_pangram("The quick brown fox jumps over the lazy dog"))