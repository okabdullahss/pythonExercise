#-------MAPS----------
#suppose you have a function and a list of iterable items. You want to apply this function for every single element
#heres where maps come into play

def my_func(num):
    return num**2

myList = [1,2,3,4,5]

print(map(my_func, myList)) #this will give the reference of map object <map object at 0x000001D3870497E0>

for x in map(my_func, myList):#however this will give each element applied by the function
    print(x)

    #or better way if you just want the list
print("--------")
print(list(map(my_func,myList)))

#lets say you have a more complex function that returns EVEN if the parameter length is even, and returns 1st letter of a string if string length is odd

def slicer(string):
    if len(string)%2 ==0:
        return "EVEN"
    else:
        return string[0]

str_list = ["Hello","My","surname ", "is", "White"]

print(list(map(slicer, str_list)))
print("--------")
#-----FILTERs---------

def filter_evens(num):
    if num%2==0:
        return num

listNum=[1,2,3,4,5,6]

print(list(filter(filter_evens, listNum)))
print("--------")
#----LAMBDAS--------

def square(num):
    return num**2

newSquareFunc = lambda num : num**2

print(newSquareFunc(5))

print(list(map(lambda num: num ** 2, listNum)))  #instead of using a function as parameter(Slicer), we simply put lambda expression

print(list(filter(lambda num : num%2==0,listNum))) #instead of using a function as parameter(Filter_evens), we simply put lambda expression

print(list(filter(lambda x : x[0].lower()=="h",str_list))) #instead of using a function as parameter(first letter of strings), we simply put lambda expression

print(list(map(lambda x : x[::-1],str_list))) #mapping the elements reverting them