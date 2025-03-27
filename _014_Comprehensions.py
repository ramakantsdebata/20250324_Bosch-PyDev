# Always create a new collection from an existing one

"""
lst  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for el  in lst:
    print(el, end="-")
print()

for el in range(1, 11):
    print(el, end="-")
print()
"""
"""
fruits = ["apple", "banana", "cherry", "dragonfruit", "erdbeeren"]
bowl = []

for fr in fruits:
    if "a" in fr:
        bowl.append(fr)

print(f"{bowl=}")

bowl = [fr       for fr in fruits     if "a" in fr ]
print(f"{bowl=}")


lst = [fr       for fr in fruits     if "a" in fr ]; print(type(lst), lst)
st = {fr       for fr in fruits     if "a" in fr }; print(type(st), st)
dt = {fr:len(fr)       for fr in fruits     if "a" in fr }; print(type(dt), dt)
tup = tuple(fr       for fr in fruits     if "a" in fr ); print(type(tup), tup)
"""

lst = []
print(dir(lst))
print(dir(list))

print("+"* 40, "\n")
obj = 10
public_members = [member    for member in dir(obj)     if member.startswith("_") is False]
print(f"[{len(public_members)}]", public_members)
# print(str(public_members))
# print(public_members.__str__())

print("+"* 40, "\n")

# callable(int.conjugate)
# callable(getattr(int, "conjugate"))
public_methods = [member    for member in dir(obj)     if member.startswith("_") is False and callable(getattr(obj, member))]
print(f"[{len(public_methods)}]", public_methods)


""" # FEEL FREE TO IGNORE THIS
def hello1():
    print("Hello")

hello2 = 10

print(type(hello1), type(hello2))
print(callable(hello1), callable(hello2))


hello1()
hello1.__class__.__call__(hello1)
"""