from decor8 import describe


@describe(name='hello')
def hello():
    print("Hello World!")


if __name__ == '__main__':
    print(hello.name)
    hello()
