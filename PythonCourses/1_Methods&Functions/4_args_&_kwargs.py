#it is the equivelant version of vararghs in java. it lets the user pass as many item in the function as possible


def myfunc(*args):   # star(*) here is what matters here. you can replace args with any string you want
    return sum(args)*0.05

def myfunc2(*asdf):
    return sum(asdf)

print(myfunc(100, 200, 300))
print(myfunc2(1,2,3))

# *args returns TUPLES,     **kwargs return DICTIONARY

def myfunc3(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print(f'My favourite fruit is {kwargs["fruit"]}')
    else:
        print("I dont see any fruit in here")

myfunc3(fruit='apple', veggies="cucumber")
myfunc3(veggies="cucumber")


print("---YOU CAN USE BOTH *args and **kwargs  TOGETHER----")
#please keep in mind that whichever orders of parameters you created your function( first param-> args, second param->kwarg),
#you must call your function and pass the parameters in the same order

def myfunc4(*args,**kwargs):
    print(f'I would like to have {args[0]} {kwargs["food"]}')

myfunc4(10,20,30,food="egg",clothing="shirt", trip="holiday")