myString = "hello"

myList = []

for item in myString:
    myList.append(item)

print(myList)
# EASIER WAY TO DO THIS VIA ListComprehension

list2 = [item for item in myString]
print(list2)

myList = [x for x in "welcome to africa"]  # IT CAN ONLY BE USED FOR append() function
print(myList)

myList = [num for num in range(0, 11)]
print(myList)

myList = [num ** 2 for num in range(0, 11)]
print(myList)

myList = [letter.upper() for letter in "hello"]
print(myList)

myList = [num ** 2 for num in range(0, 11) if num % 2 == 0]  # only the powered by 2 of the even numbers
print(myList)

celcius = [0, 10, 30.4]

fahrenait = [((9 / 5 * temp) + 32) for temp in celcius]  # convert from celcius to fahrenait
print(fahrenait)

fahrenait = []

for x in celcius:  # the same as above but only with for loop
    fahrenait.append((x * 9 / 5) + 32)

print(fahrenait)

results = [x if (x % 2 == 0) else "ODD" for x in range(0, 11)]  # print the even number, if its odd, print "ODD"
print(results)
myList = [x if (x == "a") else "Nope" for x in "welcome to africa"]
print(myList)

x = [2, 4, 6]
y = [100, 200, 300]

results = [x * y for x in [2, 4, 6] for y in [100, 200, 300]]  # NESTED FOR LOOPS in LIST COMPREHENSION
print(results)

# -----execises

s = "Print the only words in the sentence that starts with a s"

list = []
print(s.split(" "))

for x in s.split(" "):
    if x.lower().startswith("s"):
        list.append(x)
print(list)

# print all even numbers from 0 - 10

list = [num for num in range(0, 11) if (num % 2 == 0)]
print("----------")
print(list)

# ----------------
st = "print all the words in this sentence that has an even number of letters"

x = [x for x in st.split(" ") if len(x) % 2 == 0]
print(x)

# ----------------fizBuzz challange


# myList = ["fizzBuzz" if(x % 15 == 0) else "fizz" if(x%5==0) " for x  in range(0, 101)]
# print(myList)
# a = [ x if(x=="a") else "Nope" for x in "welcome to africa"]

for x in range(1,101):
    if(x%15==0):
        print("FizzBuzz")
    elif(x%5==0):
        print("Fizz")
    elif(x%3==0):
        print("Buzz")
    else:
        print(x)

r = "create a list of first letter in every word in this senctence using list comprehension"

list=[x[0] for x in r.split(" ")]
print(list)