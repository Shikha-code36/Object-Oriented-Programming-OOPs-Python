# inheritance-2.py

# The code below shows another example of inheritance
# Dog and Cat are two classes which inherits from Animal.
# This an instance created from Dog or Cat can access the methods
# in the Animal class, ie.. eat().

# The instance of 'Dog' can access the methods of the Dog class
# and it's parent class 'Animal'.

# The instance of 'Cat' can access the methods of the Cat class
# and it's parent class 'Animal'.

# But the instance created from 'Cat' cannot access the attributes
# within the 'Dog' class, and vice versa.


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating/drinking %s" % (self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print("%s goes after the %s" % (self.name, thing))


class Cat(Animal):
    def swatstring(self):
        print("%s shred the string!" % self.name)


dog = Dog("Tuffy")
cat = Cat("Mona")

dog.fetch("paper")
dog.eat("bone")
print("--------")
cat.eat("milk")
cat.swatstring()

'''
O/P-
Tuffy goes after the paper
Tuffy is eating/drinking bone
--------
Mona is eating/drinking milk
Mona shred the string!
'''

# The below methods would fail, since the instances doesn't have
# have access to the other class.

cat.fetch("frizbee")
dog.swatstring()
