import functools


def describe(**kwargs):
    """
    Decorator for adding attributes to a function or method.

    :param kwargs: A dictionary of key-value pairs representing the attributes to be added.
    :return: The decorated function or method.
    """
    def decorator(target):
        @functools.wraps(target)
        def wrapper(*args, **kwargs):
            return target(*args, **kwargs)
        for key, value in kwargs.items():
            wrapper.__setattr__(key, value)
        return wrapper
    return decorator


def announce_before(*args):
    """
    Decorator to announce function calls to other functions or classes.
    announcement occurs before actual function call.

    :param args: the functions to announce calls to
    :return: The wrapper function.
    """
    def decorator(target):
        @functools.wraps(target)
        def wrapper(*inner_args, **kwargs):
            for arg in args:
                arg(target, *inner_args, **kwargs)
            return target(*inner_args, **kwargs)
        return wrapper
    return decorator


def announce_after(*args):
    """
    Decorator to announce function calls to other functions or classes.
    announcement occurs after actual function call.

    :param args: the functions to announce calls to
    :return: The wrapper function.
    """

    def decorator(target):
        @functools.wraps(target)
        def wrapper(*inner_args, **kwargs):
            result = target(*inner_args, **kwargs)
            for arg in args:
                arg(target, *inner_args, **kwargs)
            return result

        return wrapper

    return decorator
