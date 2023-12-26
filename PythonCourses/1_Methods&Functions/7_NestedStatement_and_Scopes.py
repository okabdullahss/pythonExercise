
name = "THIS IS A GLOBAL STATEMENT"

def greet():
    name ="Tuco"

    def hello():
     print("Hello "+{name})

     hello()

print("-----")

greet()#not working but it prints Hello Tuco. If you comment out line4 , itll print out Hello THIS IS A GLOBAL STATEMENT


print("----")

x = "50"

def asdf():
    print(f'X is {x}')