
def say_hello(name="default"):
    print(f'Hello {name}')

say_hello()

def sum(a,b):
    return a+b
result = sum(10,20)
print(type(result))

def check_even(numList):
    for num in numList:
        if (num % 2 == 0):
           return True
    return False


print(check_even([1,3,5,7]))

#return all the even numbers on the list

def even_numbers(list):
    return [x for x in list if(x % 2 == 0)]


print(even_numbers([1,3,5]))
print(even_numbers(range(0,11)))
