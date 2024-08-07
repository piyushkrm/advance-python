#  5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

ls= [1, 22, 36, 56, 78957521, 15690, 985, 6955, 27120, 5555, 225110]


def greater(a, b) :
    if a > b:
        return a
    return b


print(reduce(greater, ls))