#ENUMERATION  /  ZIP  /MAX()  MIN() FUNCTION / TUPLE UNPACKING / CHECK IF AN ITEM IS IN LIST OR DICTIONARY/ SHUFFLE LIBRARY
# RANDOM INTEGER randint()  / HOW TO GET AN INPUT FROM THE USER
                #1'den başla, 10'a kadar sayıları 2şer atlayarak yazdır

from random import shuffle
from random import randint


for num in range(1,10,2):
    print(num)


# CAST TO A LIST

print(list(range(0, 10, 3)))

#BİR STRİNG'DEKİ HARFLERİ İNDEXLERİYLE BİRLİKTE YAZDIR

x = "Abdullah"
index_num = 0
for letter in x:
    print("the index is {} and the letter is {}".format(index_num,letter))
    index_num+=1

    # YUKARIDAKİNİN DAHA KOLAY YOLU ""ENUMERATE FUNCTION""
print("-------")
for ltr in enumerate(x):
    print(ltr)
    # (0, 'A')
    # (1, 'b')
    # (2, 'd')
    # (3, 'u')
    # (4, 'l')
    # (5, 'l')
    # (6, 'a')
    # (7, 'h')

#lets use it with tuple unpacking

for x, y in enumerate(x):
    print(x)
    print(y)
    print("\n")

#OPPOSITE OF ENUMERATION == ZIP

myList1 = [1,2,3,]
myList2 = ["a","b","c"]

for item in zip(myList1,myList2):
    print(item)
    # (1, 'a')
    # (2, 'b')
    # (3, 'c')

    #note that if there are more elements in one list than the other, python just ignores the additional elements and zips the correspondings

    #we can cast it to the list
print(list(zip(myList1, myList2)))


#CHECK IF "x" IS PRESENT IN THE LIST OF [1,2,3]

print("x" in [1, 2, 3])

#CHECK IF myKey IS PRESENT IN THE DICTIONARY OF {"myKey":100,"yourKey":200}

print("myKey" in {"myKey":100,"yourKey":200})
print(100 in {"myKey":100,"yourKey":200}.values())

#FIND THE MINIMUM VALUE / MAX VALUE

numList = [100,2,500,4,66]

print(min(numList))
print(max(numList))

#SHUFFLE A LIST

numList2 = [1,2,3,4,5,6,7,8]
shuffle(myList2) #somehow its not working but you got the idea. it simply shuffles
print(numList2)

#random integer  runint()

print(randint(0, 20))

#GET AN INPUT FROM THE USER  !!! IMPORTANT: INPUT FUNCTION ALWAYS ACCEPTS STRING NO MATTER WHAT YOU WRITE

userName = input("Hey please write down your name")
print(f"you username is: {userName}")