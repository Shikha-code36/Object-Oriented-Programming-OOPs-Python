# This is an updated version of decorators-2.py.
# Here, the `decorated()` function takes an argument
# and prints it back on terminal.

# When the decorator `@my_decorator` is called, it
# takes the function `decorated()` as its argument, and
# the argument of `decorated()` as the argument of `inner_decorator()`.
# Hence the arg `number` is passed to `num_copy`.

import datetime


def my_decorator(inner):
    def inner_decorator(num_copy):
        print(datetime.now(datetime.UTC))
        inner(int(num_copy) + 1)
        print(datetime.now(datetime.UTC))

    return inner_decorator


@my_decorator
def decorated(number):
    print("This happened : " + str(number))


if __name__ == "__main__":
    decorated(5)

'''
O/P-
2022-07-16 12:26:14.060603
This happened : 6
2022-07-16 12:26:14.060603
'''
