"""The common module contains common functions and classes used by the other modules.
"""

def hello_world():
    """Prints "Hello World!" to the console.
    """
    print("Hello World!")


def random_numb():
    """return a random number between 0 and 1

    Returns:
        float:a random number between 0 and 1
    """
    import random
    return random.random()

def hello(name):
    print(f'Hello {name}!')


