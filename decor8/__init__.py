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
