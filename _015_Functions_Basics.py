# Define higher (others) vs. Define earlier (Python)


def Bar():
    print("Bar")
    Baz()

def Foo():
    print("Foo")
    Bar()

def Start():
    print("Start")
    Foo()

def Baz():
    print("Baz")

Start()

print("End of prog")


###########################
"""
class Emp:
    Company ref

    kjhskjhg
    hjksdfhgkjsd

class Company:
    Emp obj


Company c1
c1.oper()
"""

#################################################