# Mutable non-seq collection of key-value pairs
dt1 = {'key': 'value'}
print(type(dt1), dt1)

dt2 = {'key': [1, 2, 3]}
# dt3 = {{'a', 'b', 'c'}: [1, 2, 3]}

key_1 = frozenset({'heated', 'medium', 'reinforced'})
cont = {key_1: "India to Bhutan"}
print(f"{cont=}")
print('heated' in key_1)

dt4 = dict.fromkeys({'a', 'b', 'c', 'd'})
print(f"{dt4=}")
dt4["b"] = "bat"
print(f"{dt4=}")

# print(dt4["e"])

if "e" in dt4:
    print(dt4["e"])
else:
    print("data not found")

# val = dt4.get("e")
# if val:
#     print(val)
# else:
#     print("data not found")

# x = 1
# z = y = x
# print(x, y, z)

# if dt4.get("e"):
if val := dt4.get("b"):
    print(val)
else:
    print("data not found")

emp = {
    1: "Manish",
    2: "Abhijeet",
    3: "Rakesh",
    4: "Parag",
}

lst1 = [1, 2, 3, 4]
for val in lst1:
    print(val)

st1 = set(emp)
st1 = set(emp.keys())
print(f"{st1=}")

print("Printing the dictionary")
for val in emp.keys():
    print(val)

for val in emp.values():
    print(val)

for key, val in emp.items():
    print(key, "-->", val)

l1 = list(emp.values())
print(f"{l1=}")


print(f"{emp=}")

del emp[4]
print(f"{emp=}")
print("Popped the emp ", emp.pop(2))
print(f"{emp=}")
print("Popped the emp ", emp.popitem())


dt4["c"] = [1,2]
dt4.get("c").append(3)
print(f"{dt4=}")
