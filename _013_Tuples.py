# Immutable collection of sequential non-homogeneous objects
tp1 = (1, 2, 3)
tp2 = ()
tp3 = (1,)
tp4 = tuple([1])
tp5 = tp1 + tp4
tp6 = tuple()

print(type(tp1), tp1)
print(type(tp2), tp2)
print(type(tp3), tp3)
print(type(tp4), tp4)
print(type(tp5), tp5)

for el in tp5:
    print(el, end=", ")
print()

for idx in range(len(tp5)):
    print(tp5[idx], end=", ")
print()


def fun1():
    return 1, 2, 3

ret = fun1()
print(type(ret), ret)

# Tuples are also used for variable argument functions
# the group of data is passed acros function boundary 
# as a tuple to prevent tampering

# This will also be obvious when we speak to packing-unpacking



###############################################################

# Named Tuples
from collections import namedtuple

# Point = namedtuple('Point', 'x y')        # <--- Valid declaration
Point = namedtuple('Point', ["x", "y"])
p1 = Point(10, 20)
print(hash(p1))
print(p1[0], p1[1])
print(p1.x, p1.y)


Student = namedtuple("Student", ["roll", "name", "std"])
s1 = Student(25, "Vijay", 7)
print(s1.roll, s1.name, s1.std)