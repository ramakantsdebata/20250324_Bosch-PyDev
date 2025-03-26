# Mutable collection of non-homogeneous objects

lst1 = [10, 20, 30]
lst2 = []
lst3 = list()
lst4 = list(lst1)

print(type(lst1), lst1)
print(type(lst2), lst2)
print(type(lst3), lst3)
print(type(lst4), lst4)

print(lst1[0])

lst4.append("Manish")
print(f"{lst4=}")

print(len(lst4))
print(len(lst4))
print(lst4.__len__())
lst5 = [1, 2, 3, 4, 5]
print(lst5 > lst1)
lst5.extend(lst1)
print(f"{lst5=}")

print(10 in lst5)

# for e in lst5:
#     if e == 10:
#         print("Found")
#         break

print(sum(lst5))
lst6 = ["Abhijeet", "Rakesh", "Pravin"]
# print(sum(lst6))
print(">>", (10 in lst5) and (lst5.index(10)))


print(lst5.index(10, 0, 6))
# sort(lst5)
print(f"{lst6=}")
lst6.sort()
print(f"{lst6=}")
# str < str
# str.__le__(str)


lst1 = [45, 23, 67, 87, 23, 98, 12]
print(lst1.count(23))


# min()
# max()
# +
# *

print(min(lst1))
print(max(lst1))

lst7 = ["a" * 10]
print(lst7)

lst7 = ["a"] * 10
print(lst7)

print(lst6 + lst7)


print("="*40)

print(f"{lst6=}")
print(f"{lst7=}")

lst6.extend(lst7)

print("After")
print(f"{lst6=}")
print(f"{lst7=}")
# print(f"{lst8=}")


lst6.remove('Pravin')
print(f"{lst6=}")

del lst6[0]
print(f"{lst6=}")


s1 = "Manish"
s2 = s1
print(id(s1), id(s2), sep='\n')
s1 += "!!"
print(s1, s2, sep="\n")
print(id(s1), id(s2), sep='\n')


l1 = [1, 2, 3]
l2 = l1
print(id(l1), l1)
print(id(l2), l2)

l1.append(4)
print(id(l1), l1)
print(id(l2), l2)


def mod_list(lst:list, data):
    lst.append(data)
    print(f"{lst=}")

mod_list(l1, 100)
print(id(l1), l1)
print(id(l2), l2)

