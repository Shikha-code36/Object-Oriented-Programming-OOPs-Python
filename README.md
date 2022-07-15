# Object Oriented Programming in Python

00. [OOPs](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#what-do-you-understand-by-oops)
01. [Classes](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#01-classes)
02. [Methods-Functions](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#02-methodsfunctions)
03. [Objects](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#03-objects)
04. [Constructors](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#04-constructors)
05. [Inheritance](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#04-constructors)

------------
## What do you understand by OOPs?
- Object-Oriented Programming (OOP).
The concept of OOP in Python focuses on creating reusable code. 
An object-oriented paradigm is to design the program using classes and objects. 
The object is related to real-word entities such as book, house, pencil, etc. 
The oops concept focuses on writing the reusable code. 
It is a widespread technique to solve the problem by creating objects.

------------

## NOTES
------------
#### 01. Classes

It is you can say a template.
Classes are the building blocks in Object Oriented Programming. 
Classes can be seen as blueprints from which you create your Instances or Objects. 
In Python, classes are defined by the “Class” keyword

```
class myClass():
```
------------
------------

#### 02. Methods-Functions

- Inside classes, you can define functions or methods that are part of this class
- Difference between functions and methods
    * Functions can be called only by its name, as it is defined independently. But methods can't be called by its name only, we need to invoke the class by a reference of that class in which it is defined, i.e. method is defined within a class and hence they are dependent on that class.

```
def method1 (self):
   print("OOPs")
def method2 (self,someString): 
   print ("Program-Method"+ someString)
```
. Here we have defined method1 that prints “OOPs”
. Another method we have defined is method2 that prints “Program-Method”+ SomeString. SomeString is the variable supplied by the calling method

- Everything in a class is indented, just like the code in the function, loop, if statement, etc. Anything not indented is not in the class
```
class myClass():
    def method1 (self):
        print("OOPs")
    def method2 (self,someString): 
        print ("Program-Method" + someString)
```
- [Note]
    - “self”
        - The self-argument refers to the object itself. Hence the use of the word self. So inside this method, self will refer to the specific instance of this object that’s being operated on.
        - Self is the name preferred by convention by Pythons to indicate the first parameter of instance methods in Python. It is part of the Python syntax to access members of objects

- Types of methods- [Check code for reference](Methods/methods.py))
    * Instance Method
    * Class Method
    * Static Method
------------
------------
#### 03. Objects

- How to make an object of the class?
```
obj = myClass()
```

- How to call a method in a class?
```
obj.method1()
    obj.method2("Learning OOPs")
```
* Notice that when we call the method1 or method2, we don’t have to supply the self-keyword. That’s automatically handled for us by the Python runtime.
* Python runtime will pass “self” value when you call an instance method on in instance, whether you provide it deliberately or not
* Just work on non self arguments

- complete code
```
# Example file for working with classes
class myClass():
  def method1(self):
      print("OOPs")
        
  def method2(self,someString):    
      print("Program-Method" + someString)
  
      
def main():           
  # exercise the class methods
  obj = myClass ()
  obj.method1()
  obj.method2("Learning OOPs")
  
if __name__== "__main__":
  main()
```
------------
------------
#### 04. Constructors

Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created.

The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.

```
def __init__(self):
    # body of the constructor
```
------------
------------
#### 05. Inheritance


------------