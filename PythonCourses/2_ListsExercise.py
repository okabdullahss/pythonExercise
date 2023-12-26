myList = [1, 2.2, "Hello", 3, 4 ,5 ,6 ,7 ]
print(len(myList))
anotherList = ["x","y"]
print(myList[2:6:2])

newList = myList + anotherList
print(newList)

#UNLIKE Strings, LITS ARE MUTABLE, which means you can change a list item

newList[0] = "ONE ALL CAPS "
print(newList)
newList.append(8)
print(newList)

print(newList.pop())      #removes the last item and returns it as a result
print(newList)

print(newList.pop(1))   #removes the provided index item

list2 = [3,6,1,4,2]
print(list2)
list2.sort()   #this DOES NOT RETURN ANY VALUE so do not try to assing this into new list. It already changes the existing list2
                # immutable lists are called Tuples
print(list2)

list2.reverse()
print(list2)

list3 = [1,2, [3,4]]

