#decorators-4.py

# This example builds on the previous decorator examples.
# The previous example, decorators-3.py showed how to
# deal with one argument passed to the function.

# This example shows how we can deal with multiple args.

# Reminder : `args` is a list of arguments passed, while
# kwargs is a dictionary passed as arguments.


def decorator(inner):
    def inner_decorator(*args, **kwargs):
        print(args, kwargs)

    return inner_decorator


@decorator
def decorated(string_args):
    print("This happened : " + string_args)


if __name__ == "__main__":
    decorated("Hello, how are you?")

# This prints :
# # python 22-decorators-4.py
# ('Hello, how are you?',)
