myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in myList:
    print(x)

print("-------")

for a in myList:
    print("hello")

print("---print the odd & even numbers----")

for b in myList:
    if (b % 2 == 0):
        print(b)
    else:
        print(f'Odd Number: {b}')

print("---print the sum of all elements in the list----")
sum_list = 0
for x in myList:
    sum_list += x
    # print(f'sum of all elements in the list is: {sum_list}')
print(
    f'sum of all elements in the list is: {sum_list}')  # !!! IMPORTANT: if I put this line in alignment with the sum_list+=x, it will be
# inside of the for loop, which will print every time it iterates


print("---prints all the elements in the string----")

s = "Hello World"

for x in s:
    print(f' {id(x)} : {x}')

print("------list in for loop(tuples are immutable so we wont iterate) -------")

tuple = (1, 2, 3)
list = [10, 50, 40]

for _ in list:
    list[list.index(_)] += 1

print(list)

print("-------TUPLE UNPACKING(VERY COMMON IN PYTHON BUILT IN)")

t_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

for a, b in t_list:
    print(a)

print("-------loops for DICTIONARY--------------")

myDictionary = {"k1": 1, "k2": 2, "k3": 3}

for item in myDictionary:
    print(item)  # if you put item here, by default python prints ONLY THE KEYS.

for item in myDictionary.items():  # by adding PLURAL FORM OF "item", it can print out the whole key value pairs
    print(item)

for item in myDictionary.keys(): # if you add "keys()" it can print out the keys
    print(item)

for key,value in myDictionary.items():# another method for printing keys(tuple unpackacking)
    print(f'keys are : {key}')

for item in myDictionary.values(): # if you add "values()" it can print out the values
    print(item)

for key,values in myDictionary.items(): # another method for printing values (tuple unpackacking)
    print(f'values are: {values}')

for item in myDictionary.values():
    if(item % 2 == 0):
        print(f' item is : {item}')