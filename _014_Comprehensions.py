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

obj = 10
public_members = [member    for member in dir(obj)     if member.startswith("_") is False and callable(HOMEWORK)]
print("+"* 40, "\n")

print(public_members)
# print(str(public_members))
# print(public_members.__str__())


print(10)

