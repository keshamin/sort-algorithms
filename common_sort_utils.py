from collections import Iterable
from functools import wraps


def iterables_only(func):
    """
    Decorator validates that first argument is iterable
    :param func: sorting function taking iterable as a first argument
    :return: decorated function
    """

    @wraps(func)
    def wrapper(iterable, *args, **kwargs):
        if not isinstance(iterable, Iterable):
            raise ValueError('Cannot sort non-iterable object!')
        return func(iterable, *args, **kwargs)

    return wrapper
