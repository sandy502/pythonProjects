from unicodedata import name


class Dog:
    pass    # empty class declaration
# The self  
# When we call a method of this object 
# as myobject.method(arg1, arg2), 
# this is automatically converted by Python into 
# MyClass.method(myobject, arg1, arg2) – this is all the special self is about.

# The __init__ method 
# The __init__ method is similar to constructors in C++ and Java. 
# It is run as soon as an object of a class is instantiated. 
# The method is useful to do any initialization you want to do with your object. 

class Cat:

    attr1 = "mammal" # attribute or variable also a static variable or class variable

    # instance attribute or constructor
    def __init__(self, name):
        self.name = name  # this is an instance variable

    # method or function of a class
    def speak(self):
        print('{} can only mew.'.format(self.name))   

Tom = Cat("Tom")

# print('Tom is a {}'.format(Tom.__class__.attr1)) # accessing class attr1
# print('{} is a cat.'.format(Tom.name)) # accessing attribute 'name' of the instance
# attribute of an instance can only be accessed with the help of an instance of the class which denotes an object.
# Tom.speak() # we can call a method of the class directly through object.


# inheritance
# Inheritance is the capability of one class to derive or inherit the properties from another class. 
# The class that derives properties is called the derived class or child class and 
# the class from which the properties are being derived is called the base class or parent class.


# Example of single inheritance
class Mom(object): # (Generally, object is made ancestor of all classes)
    def __init__(self, name):
        print('Mom class')
        self.name = name

    def display(self):
        print(self.name)


class Child(Mom):
    def __init__(self, name, id):
        print('Child class')
        self.id = id

        # invoking parent class constructor
        # If we forget to invoke the __init__() of the parent class then its 
        # instance variables would not be available to the child class.
        # and therefore it will throw an error. 
        Mom.__init__(self, name)    
                
# Ch1 = Child('child1', 1)

# Ch1.display()

# example of a multiple inheritance
class Orange(object):
    def __init__(self):
        self.str1 = 'this is orange'
        print('orange')

class Lemon(object):
    def __init__(self):
        self.str2 = 'this is lemon'
        print('lemon')
        
class Kinu(Orange, Lemon):
    def __init__(self):
        Orange.__init__(self)
        Lemon.__init__(self)
        print('derived')

    def printstr(self):
        print(self.str1, self.str2)

# kinu1 = Kinu()
# kinu1.printstr()         


# Multilevel inheritance
class Mom(object): # (Generally, object is made ancestor of all classes)
    def __init__(self, name):
        print('Mom class')
        self.name = name


class Child(Mom):
    def __init__(self, name, id):
        print('Child class')
        Mom.__init__(self, name)
        self.id = id

class Grandchild(Child):
    def __init__(self, name, id, gen):
        print('GrandChild class')
        Child.__init__(self, name, id)
        self.gen = gen

    def printall(self):
        print(self.name)
        print(self.id)
        print(self.gen)

# gc = Grandchild('abc', 1, 'third') 
# gc.printall()               


# Private members of parent class

class Mom(object): # (Generally, object is made ancestor of all classes)
    def __init__(self):
        self.name = 'Mom'

        self.__id = 1 # here we are making id private using double underscores


class Child(Mom):
    def __init__(self):
        self.name = 'child'
        Mom.__init__(self)

# ch1 = Child()
# print(ch1.id) # here this is throwing error Child' object has no attribute 'id'.


# Polymorphism
# Polymorphism simply means having many forms.
# function overiding is done here
# process of re-implementing a method in the child class is known as Method Overriding. 

# Encapsulation 
#  idea of wrapping data and the methods that work on data within one unit. 
# This puts restrictions on accessing variables and methods directly and 
# can prevent the accidental modification of data. 
# To prevent accidental change, an object’s variable can only be changed by an object’s method. 
# Those types of variables are known as private variables.

# Protected members
# the convention is of prefixing the name of the member by a single underscore '_'.
class Base:
    def __init__(self): # __init__ is called double leading and double trailing underscore
 
        # Protected member
        self._a = 2
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ", self._a)
        self._a = 3
        print("Calling modified protected member outside class: ", self._a)


obj1 = Derived()
 
obj2 = Base()

# print("Accessing protected member of obj1: ", obj1._a)
# print("Accessing protected member of obj2: ", obj2._a)

# print(issubclass(Derived, Base)) # check if a class is subclass of another
# print(isinstance(obj1, Derived)) # check if obj1 is an instance of Derived


# class method is a method that is bound to the class and not the object of the class
# The @classmethod decorator is a built-in function decorator that 
# is an expression that gets evaluated after your function is defined. 
# The result of that evaluation shadows your function definition. 
# A class method receives the class as an implicit first argument

# we use @staticmethod decorator to create a static method in python.
# A static method is also a method that is bound to the class and not the object of the class.

# Python program to illustrate reflection 
def reverse(sequence): 
    sequence_type = type(sequence) 
    empty_sequence = sequence_type() 
      
    if sequence == empty_sequence: 
        return empty_sequence 
      
    rest = reverse(sequence[1:]) 
    first_sequence = sequence[0:1] 
      
    # Combine the result 
    final_result = rest + first_sequence
      
    return final_result 
  
# Driver code 
print(reverse([10, 20, 30, 40])) 
print(reverse("GeeksForGeeks")) 

# Reflection-enabling functions include type(), isinstance(), callable(), dir() and getattr().