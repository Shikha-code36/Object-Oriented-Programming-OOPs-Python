# In the backend, python is mostly objects and method
# calls on objects.

# Here we see an example, where the `print()` function
# is just a call to the magic method `__repr__()`.


class PrintList(object):
    def __init__(self, my_list):
        self.mylist = my_list

    def __repr__(self):
        return str(self.mylist)


printlist = PrintList(["a", "b", "c"])
print(printlist.__repr__()) #['a', 'b', 'c']


# To read more on magic methods, refer :
# http://www.rafekettler.com/magicmethods.html

my_list_1 = ["a", "b", "c"]

my_list_2 = ["d", "e", "f"]

print("\nCalling the `+` builtin with both lists")
print(my_list_1 + my_list_2)

print("\nCalling `__add__()` with both lists")
print(my_list_1.__add__(my_list_2))
'''
O/P-
Calling the `+` builtin with both lists
['a', 'b', 'c', 'd', 'e', 'f']

Calling `__add__()` with both lists
['a', 'b', 'c', 'd', 'e', 'f']
'''