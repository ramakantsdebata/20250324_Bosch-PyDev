


def logger(fn):
    def wrapper():
        print("Before", fn.__name__)
        fn()
        print("After", fn.__name__)
    return wrapper

@logger
def greet():
    print("hi")


@logger
def hello():
    print("Hello there")

# greet = logger(greet)
# wrapper()

################################
greet()
hello()