# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# def capital1and4(arg):
#     result = ""
#     for x, y in enumerate(arg):
#         if x == 0:
#             result += y.upper()
#         elif x == 3:
#             result += y.upper()
#         else:
#             result+=y
#     return result

# -------------------------------------------------------------

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'

# def reverseString(arg):
#     list1 = arg.split(" ")
#     list1.reverse()
#     result = " ".join(list1)
#     return result
#
# print(reverseString("I am home"))

# -------------------------------------------------------------


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

# def in_between(num):
#     if 89 < num < 111:
#         return True
#     elif 189 < num < 211:
#         return True
#     else:
#         return False
#
# print(in_between(90))
# print(in_between(104))
# print(in_between(150))
# print(in_between(209))


# -------------------------------------------------------------

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

# def check_double3(list):
#     is_double = False
#     num = 0
#
#     for x in range(len(list)-1):
#             if list[x] == list[x+1] ==3:
#                is_double = True
#             else:
#                 pass
#     return is_double
#
#
# print(check_double3([1, 3, 3]))
# print(check_double3([1, 3, 1, 3]))
# print(check_double3([3, 1, 3]))


# -------------------------------------------------------------

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

# def paper_doll(str):
#     list = [x for x in str]
#     print(list)
#     tripledStr = ""
#     for x in range(len(list)):
#         list[x] = "" + list[x] + list[x] + list[x]
#         tripledStr += list[x]
#     return tripledStr
#
#
# print(paper_doll("hello"))


# -------------------------------------------------------------

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

# def black_jack(a,b,c):
#     total = a+b+c
#     list = [a,b,c]
#     if a and b and c in range(1,12):
#         if total <= 21:
#             return total
#         elif total > 21 and list.__contains__(11):
#             total-=10
#             if total >21:
#                 return "BUST"
#             else:
#                 return total
#         elif total > 21:
#             return "BUST"
#
#     else:
#         print("The numbers you provided is not in range between 1 and 11")
#
#
# print(black_jack(5, 6, 7))
# print(black_jack(9, 9, 9))
# print(black_jack(9, 9, 11))

# -------------------------------------------------------------

# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


# def summer_of_69(list=[]):
#     sumOfList = 0
#     for x in list:
#         sumOfList += x
#
#     totalSum = 0
#
#     if not list:
#         return 0
#     elif list.__contains__(6) and list.__contains__(9):
#         indxOf6 = list.index(6)
#         indxof9 = list.index(9)
#         if indxOf6 < indxof9:
#             for x in range(indxOf6, indxof9 + 1):
#                 totalSum += list[x]
#         return sumOfList - totalSum
#     else:
#         return sumOfList
#
# #test the function for 2,1,6,9 should be 14
# print(summer_of_69([2, 1, 6,9, 11]))

# ----------------CHALLENGING PROBLEMS---------------------------------------------

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

# def spy_game(list):
#     code = [0, 0, 7, "x"]
#
#     for x in list:
#         if x == code[0]:
#             code.pop(0)
#     return len(code) == 1
#
#
# print(spy_game(([1, 2, 4, 0, 0, 7, 5])))
# print(spy_game(([1, 0, 2, 4, 0, 5, 7])))
# print(spy_game(([1, 7, 2, 0, 4, 5, 0])))
# print(spy_game(([1, 1, 2, 0, 7, 0, 4, 5, 0])))

# -------------------------------------------------------------

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25

# By convention, 0 and 1 are not prime.






# -------------------------------------------------------------




























































