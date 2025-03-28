"""
def add1(a, b):
    return a + b

def add2(a, b, c):
    return a + b + c


def add(*data):
    match(len(data)):
        case 2:
            return add1(*data)
        case 3:
            return add2(*data)
    

################################
print(add(1, 2, 3))
print(add(1, 2))
"""


from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    print("add(int, int)")
    return a + b

@dispatch(int, int, int)
def add(a, b, c):
    print("add(int, int, int)")
    return a + b + c

print(add(1, 2, 3))
print(add(1, 2))
print(add(1.1, 2))
