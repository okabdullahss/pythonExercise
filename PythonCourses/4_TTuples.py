
# immutable lists are called Tuples

t = ("a","a","b")

print(type(t))

myList = [10,20,30]

myList[0] = "x"
print(myList)

print(t[1])
print("------")
print(t.count(1))

print(t.index("a")) #this appears twice but index method show the first occurance in the tuple
print(t.index("b"))

#t[1] = " e" ## error here. you can not make assignment on tuples since they are immutable