class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

'''
Instance Methods-
The first method on MyClass, called method, is a regular instance method.
the method takes one parameter, self, which points to an instance of MyClass when the method is called 
(but of course instance methods can accept more than just one parameter).

It can modify object's state and class state.
Through the self parameter, instance methods can freely access attributes and other methods on the same object. 
Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute. This means instance methods can also modify class state.
'''
'''
>>> obj = MyClass()
>>> obj.method()
('instance method called', <MyClass instance at 0x10205d190>)
This confirmed that method (the instance method) has access to the object instance (printed as <MyClass instance>) via the self argument.

When the method is called, Python replaces the self argument with the instance object, obj.

we can also do like this 
>>> MyClass.method(obj)
('instance method called', <MyClass instance at 0x10205d190>)
'''

'''
Class Methods-
@classmethod decorator to flag it as a class method.

Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.
Because the class method only has access to this cls argument, it can’t modify object instance state. 
That would require access to self. 
However, class methods can still modify class state that applies across all instances of the class.
'''
'''
>>> obj.classmethod()
('class method called', <class MyClass at 0x101a2f4c8>)
Calling classmethod() showed us it doesn’t have access to the <MyClass instance> object, but only to the <class MyClass> object, representing the class itself (everything in Python is an object, even classes themselves).
'''

'''
Static Methods-
 @staticmethod decorator to flag it as a static method.

This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).

Therefore a static method can neither modify object state nor class state.
Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.
'''
'''
>>> obj.staticmethod()
'static method called'
'''