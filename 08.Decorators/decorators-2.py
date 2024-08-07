# decorators-2.py
# An updated version of decorators-1.py

# This code snippet takes the previous example, and add a bit more information
# to the output.

import datetime


def my_decorator(inner):
    def inner_decorator():
        print(datetime.now(datetime.UTC))
        inner()
        print(datetime.now(datetime.UTC))

    return inner_decorator


@my_decorator
def decorated():
    print("This happened!")


if __name__ == "__main__":
    decorated()

'''
O/P: (NOTE: The time will change of course :P)

2022-07-16 12:24:18.704572
This happened!
2022-07-16 12:24:18.704572
'''
