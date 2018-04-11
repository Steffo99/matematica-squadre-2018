import math


def recursive(iterations):
    if iterations == 0:
        return 0
    return math.sqrt(2 + recursive(iterations-1))


print(recursive(100))
