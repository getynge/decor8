from decor8.functions import describe, delegate, delegator, DelegateKind


@describe(name='hello')
@delegator
def hello():
    print("Hello World!")


@delegate(hello, DelegateKind.BEFORE)
def hello_delegate(of):
    print("HELLO RUN")


@delegate(hello, DelegateKind.AFTER)
def hello_after_delegate(of, r):
    print("HELLO AFTER RUN")


if __name__ == '__main__':
    print(hello.name)
    hello()
