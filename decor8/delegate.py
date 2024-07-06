from functools import wraps
from enum import Enum


class Kind(Enum):
    BEFORE = 0
    AFTER = 1


class InvalidKind(Exception):
    pass


def delegator(f):
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
