#decorators-7.py

# We have two functions, one which adds two numbers,
# and another which subtracts two numbers.

# We apply the decorator @double which takes in the
# functions that is called with the decorator, and doubles
# the output of the respective function.


def double(my_func):
    def inner_func(a, b):
        return 2 * my_func(a, b)

    return inner_func


@double
def adder(a, b):
    return a + b


@double
def subtractor(a, b):
    return a - b


print(adder(5, 6)) #22
print(subtractor(8, 2)) #12
