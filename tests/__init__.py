from decor8.describe import describe
from decor8.delegate import delegator, delegate, Kind


@describe(name='hello')
@delegator
def hello():
    print("Hello World!")


@delegate(hello, Kind.BEFORE)
def hello_delegate(of):
    print("HELLO RUN")


if __name__ == '__main__':
    print(hello.name)
    hello()
