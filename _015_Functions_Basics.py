# Define higher (others) vs. Define earlier (Python)

"""
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
"""

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
## Function Arguments- Positional, Default, Special
"""# def add(a:int, b:int) -> int:
def add(a:int, b:int, c:int):
# def add(a, b):
    print(f"{a=}, {b=}, {c=}")
    sum = a + b + c
    return sum

# print(add(1, 2)) # Positional arguments
# print(add(1, 2, 3)) # Positional arguments
# print(add(2))

# print(add(c=2, a=1)) # KeyWorded arguments

print(add(1, 2, 3))
print(add(1, c=2, b=3))
"""

"""
def add(a, b, /, c=0, *, d=0):
    print(f"{a=}, {b=}, {c=}, {d=}")
    sum = a + b + c + d
    return sum

def mul(a, b, c=1, d=1):
    print(f"{a=}, {b=}, {c=}, {d=}")
    prod = a * b * c * d
    return prod

print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, d=3, c=4))
print(add(1, 2, d = 3, c = 4))

print(add(1, 2, 3, d=4))
"""
"""
def add(a, b, /, c, d, *, e=0, f=0, g):
    sum = a + b + c + d + e + f
    return sum

# print(add(1, 2, 3, 4, 5, f=6))
print(add(1, 2, 3, 4, f=5, e=6, g=1))
print(add(1, 2, d=3, c=4, f=5, e=6, g=1))
# print(add(1, b=2, d=3, c=4, f=5, e=6))

print(add(1, 2, 3, 4, g=1))
print(add(1, 2, 3, 4, f=5, g=1))

def fun1(*, a, b=1, c, d=2):
    print(f"{a=}, {b=}, {c=}, {d=}")

fun1(a=3, c=4)
"""

##############################################################
## Unpacking, Packing
"""
lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
# a = lst1[0]
# b = lst1[1]
# lst3 = lst2 = lst1
a, *_, c = lst1

print(a, c)
"""

"""
def add(a, b=0, c=0):
    print(f"{a=}, {b=}, {c=}")
    sum = a + b + c
    return sum


lst1 = [1, 2, 3]
print(add(lst1[0], lst1[1], lst1[2]))
print(add(*lst1))
"""
"""
def fun1():
    a, *lst = 1, 2, 3
    print(type(lst), lst)

fun1()

#####################################################################
## Variable arguments
def add(a, b, *data):                     
    print(type(data), data)
    sum = a + b 
    for val in data:
        sum += val
    return sum

def consumer():
    # print(add())
    # print(add(1)2)
    print(add(1, 2))
    print(add(1, 2, 3))
    print(add(1, 2, 3, 4))
    print(add(1, 2, 3, 4, 5))

consumer()
"""

"""
#####################################################################
## KeyWorded variable arguments
# def PrintLeadership(ceo, vp):
#     print(f"{ceo=}, {vp=}")

def PrintLeadership(**leaders):     # Packing the key-value pairs
    for pos, name in leaders.items():
        print(f"{pos} --> {name}")

# PrintLeadership(ceo="Vivek")
# PrintLeadership(ceo="Vivek", vp="Santosh")
# PrintLeadership(ceo="Vivek", cfo="Abhay")

emps = {
    "ceo": "Vivek", 
    "vp": "Santosh",
    "rm": "Vineet"
}

PrintLeadership(**emps)         # Unpacking the key-value pairs from the dictionary
"""

###########################################################
## Scopes - LEGB
# """
# s1 = "Global string"

# def Outer():
#     """This is the Outer method for our trials"""
#     # global s1
#     print(f"{globals()=}")
#     print(f"{locals()=}")
#     print("Outer Scope -->", globals()["s1"])
#     s1 = "Outer string"
#     print("Outer Scope -->", s1)
#     def Inner():
#         """This is the Inner method for our trials"""
#         global s1
#         s1 = "Inner string"
#         print("Inner string -->", s1)
#     Inner()
#     print(f"{locals()=}")
    
# Outer()

# print("Global scope -->", s1)

# print(Outer.__doc__)            ## Doc Strings
# """

#############################################
## Lambdas - Anonymous functions
## one codeline, no loops no blocking code, can have simple if-else conditions
def square(num):
    return num * num

sq1 = lambda num : num * num

print(square(2))
print(sq1(2))

toolkit = []
toolkit.append(lambda num: num**2)
toolkit.append(lambda num: "yes" if num%2 == 0 else "no")

print(toolkit[0](9))
print(toolkit[1](9))


