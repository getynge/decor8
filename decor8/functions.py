from functools import wraps
from enum import Enum


class DelegateKind(Enum):
    BEFORE = 0
    AFTER = 1


class InvalidDelegateKind(Exception):
    pass


def delegator(f):
    """
    :param f: The function to be delegated
    :return: A Delegator object

    The Delegator acts as a wrapper around the function f. It allows us to add before and after delegates
    that will be called before and after the function f is executed.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        for delegate in decorated.before_delegates:
            delegate(f, *args, **kwargs)
        result = f(*args, **kwargs)
        for delegate in decorated.after_delegates:
            delegate(f, result, *args, **kwargs)
        return result
    decorated.before_delegates = []
    decorated.after_delegates = []
    return decorated


def delegate(of, kind: DelegateKind):
    """
    :param of: The object on which the delegates will be registered.
    :param kind: The kind of delegation to be performed. Should be one of the values from the `Kind` enumeration.
    :return: The decorator function that registers the given function as a delegate on the specified object.
    """
    def decorator(func):
        match kind:
            case DelegateKind.BEFORE:
                of.before_delegates.append(func)
            case DelegateKind.AFTER:
                of.after_delegates.append(func)
            case _:
                raise InvalidDelegateKind(f'Type {kind} not supported')
        return func
    return decorator


def describe(**kwargs):
    """
    Decorator for adding attributes to a function or method.

    :param kwargs: A dictionary of key-value pairs representing the attributes to be added.
    :return: The decorated function or method.
    """
    def decorator(target):
        @wraps(target)
        def wrapper(*args, **kwargs):
            return target(*args, **kwargs)
        for key, value in kwargs.items():
            wrapper.__setattr__(key, value)
        return wrapper
    return decorator
