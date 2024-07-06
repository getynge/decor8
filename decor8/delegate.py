from enum import Enum


class Kind(Enum):
    BEFORE = 0
    AFTER = 1


class InvalidKind(Exception):
    pass


def delegator(f):
    """
    :param f: The function to be delegated
    :return: A Delegator object

    The delegator decorator takes in a function f as a parameter and returns a Delegator object.

    The Delegator object acts as a wrapper around the function f. It allows us to add before and after delegates
    that will be called before and after the function f is executed.
    """
    class Delegator:
        def __init__(self):
            self.before_delegates = []
            self.after_delegates = []
            self.function = f

        def __call__(self, *args, **kwargs):
            for delegate in self.before_delegates:
                delegate(f, *args, **kwargs)
            result = self.function(*args, **kwargs)
            for delegate in self.after_delegates:
                delegate(f, result, *args, **kwargs)

        def add_before_delegate(self, func):
            self.before_delegates.append(func)

        def add_after_delegate(self, func):
            self.after_delegates.append(func)
    return Delegator()


def delegate(of, kind: Kind):
    """
    :param of: The object on which the delegates will be registered.
    :param kind: The kind of delegation to be performed. Should be one of the values from the `Kind` enumeration.
    :return: The decorator function that registers the given function as a delegate on the specified object.
    """
    def decorator(func):
        match kind:
            case Kind.BEFORE:
                of.before_delegates.append(func)
            case Kind.AFTER:
                of.after_delegates.append(func)
            case _:
                raise InvalidKind(f'Type {kind} not supported')
        return func
    return decorator
