# inheriting-init-constructor-1.py

# This is a normal inheritance example from which we build
# the next example. Make sure to read and understand the



class Animal(object):
    def __init__(self, name, thing):
        self.name = name
        self.thing = thing


class Dog(Animal):
    def fetch(self):
        print("%s goes after the %s" % (self.name, self.thing))


dog = Dog("Tuffy","Ball")
print("The dog's name is %s and he plays %s" % (dog.name, dog.thing))
dog.fetch()
'''
O/P-
The dog's name is Tuffy and he plays Ball
Tuffy goes after the Ball
'''

#ANOTHER WAY TO ACCESS
class Animal(object):
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def fetch(self, thing):
        print("%s goes after the %s" % (self.name, thing))


d = Dog("TUFFY")
print("The dog's name is", d.name)
d.fetch("Ball")
'''
O/P-
The dog's name is TUFFY
TUFFY goes after the Ball
'''