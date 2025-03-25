x = 1024
y = 1024

print(id(x))
print(id(y))
print()

x += 1
y += 1

print(id(x))
print(id(y))
print()

x += 1
y += 1

print(id(x))
print(id(y))
print()


s1 = "Test"
print(type(s1), id(s1), s1)

s1 = "Fest"
print(type(s1), id(s1), s1)

for ch in s1:
    print(ch, end=" - ")
print()

print(s1[0])
s1[0] = "B"

