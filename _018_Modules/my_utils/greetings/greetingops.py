__all__ = ['greet', 'greetName', 'greetInteract']

def greet():
    print("Hi there")

def greetName(name):
    print(build_greeting("Hi", name))

def greetInteract():
    name = input("Enter you name: ")
    print(build_greeting("Hi", name))

def build_greeting(greeting, name):
    return greeting + " " + name + "!"

def TestAll():
    greet()
    greetName("Test")
    greetInteract()

def TestSmoke():
    greet()
    greetName("Test")

print((f"{__name__=}"))

def print(str):
    pass

if __name__ == "__main__":
    TestAll()
    TestSmoke()
