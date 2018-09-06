
from random import choice


def quick(arr):
    """
    Quick sort
    """
    if len(arr) < 2:
        return arr
    pivot = choice(arr) 
    less = [i for i in arr if i < pivot]
    more = [i for i in arr if i > pivot]
    return quick(less) + [pivot] + quick(more)

