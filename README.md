# Object Oriented Programming in Python

00. [OOPs](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#what-do-you-understand-by-oops)
01. [Classes](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#01-classes)
02. [Methods-Functions](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#02-methodsfunctions)
03. [Objects](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#03-objects)
04. [Constructors](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#04-constructors)
05. [Inheritance](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#05-inheritance)
06. [Encapsulation](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#06-encapsulation)
07. [Polymorphism](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#07-polymorphism)
08. [Decorators](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#08-decorators)
09. [Method Overloading](https://github.com/Shikha-code36/Object-Oriented-Programming-OOPs-Python#09-method-overloading)

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
[Class Attributes](01.Class-Attributes)

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

- Types of methods- [Check code for reference](02.Methods/methods.py))
    * Instance Method
    * Class Method
    * Static Method
        
        * We have one more method called [magic method](02.Methods/magic-method.py)

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

* More about __init__ constructor [Link](04.init-constructor)
------------
------------
#### 05. Inheritance

With inheritance one class can derive the properties of another class.
ex- Man Inheriting features from his father

[Detailed Explanation](05.Inheritance)

------------
#### 06. Encapsulation

Encapsulation involves the bundling of data members and functions inside a single class. Bundling similar data members and functions inside a class also helps in data hiding. Encapsulation also ensures that objects are self-sufficient functioning pieces and can work independently.

[Detailed Explanation](06.Encapsulation)

------------
------------
#### 07. Polymorphism

The literal meaning of polymorphism is the condition of occurrence in different forms.
Polymorphism in python defines methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class. Also, it is possible to modify a method in a child class that it has inherited from the parent class.

[Detailed Explanation](07.Polymorphism)

------------
------------
#### 08. Decorators

A decorator takes in a function, adds some functionality and returns it.
Decorators are used to add functionality to an existing code.

This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time.

[Detailed Explanation](08.Decorators)

------------
------------
#### 09. Method Overloading

Two methods cannot have the same name in Python. Method overloading in Python is a feature that allows the same operator to have different meanings.

Overloading is the ability of a function or an operator to behave in different ways based on the parameters that are passed to the function, or the operands that the operator acts on.

In Python, you can create a method that can be called in different ways. So, you can have a method that has zero, one or more number of parameters. Depending on the method definition, we can call it with zero, one or more arguments.

[Detailed Explanation](09.Method_overloading)

------------