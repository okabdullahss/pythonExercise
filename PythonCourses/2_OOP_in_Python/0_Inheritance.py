class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_I(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


asdf = Animal() # Animal Created/ Create an instance of a class. init method is automatically run
asdf.who_am_I() #I am an animal
asdf.eat() # I am eating
print("---------------------")

class Dog(Animal): # Inherited the Animal() class. Now we are able to use the methods of Animal class in Dog class
    def __init__(self):
        Animal.__init__(self)
        print("I am a dog class")

    # d1 = Dog()  # I am a dog class
    # d1.eat()  # I am eating
    # d1.who_am_I()  # I am an animal
#Heres the trick part. You can override the methods of Animal class inside the Dog class
    def who_am_I(self):
        print("I am a dog. Override the method")
    def eat(self):
        print("I am dog, eating meat")


# d1 = Dog() #I am a dog class
# d1.who_am_I() #I am a dog. Override the method
# d1.eat() #I am dog, eating meat

#TOSTRING() / if you just print the object you created from a class, it will prin the referance, not the object. so you override a __str__ method for it

class Book():
    def __init__(self,author, name, pages):
        self.author = author
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Book name {self.name} author is {self.author} and it contains {self.pages} pages"
    def __len__(self):
        return self.pages
    def __del__(self):
        print(f"Book name {self.name} has been succesfully deleted")


b1 = Book("Apo", "Alaman Bombası", 200)

print(b1) #Book name Alaman Bombası author is Apo and it contains 200  pages
#if you dont use __str__ method, it print outs the referance of the object b1 / <__main__.Book object at 0x00000203B69F0E10>

len(b1) #somewho not showing anything on the console
del b1 #Book name Alaman Bombası has been succesfully deleted / Because we override the delete method with __del__(self)
# print(b1) # NameError: name 'b1' is not defined because we deleted b1 with built in method del