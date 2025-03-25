# from random import randint

# num = randint(1, 100)
# print(num)
# if num%2 == 0:
#     print("Even")
# else:
#     print("Odd")


# if num > 50:
#     print("High")
# elif num < 50:
#     print("Low")
# else:
#     print("Equal")


# from random import randint

# num = randint(1, 7)
# print(num)

# match(num):
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case 4:
#         print("Four")
#     case 5:
#         print("Five")
#     case _:
#         print("Other Number")


## Loops
### While

# num = 0
# while num <= 10:
#     print(num, end=", ")
#     num += 1

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# x = 17
# idx = 0
# while idx < len(lst):
#     if lst[idx] == x:
#         print("Found the number")
#         break
#     else:
#         print(".", end="")
#     idx += 1
# else:
#     print("Number not Found")

### for loops
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# idx = 0
# for(init; cond; step)
x = 17
for idx in range(len(lst)):
    # print(idx, " -- ", lst[idx])
    if lst[idx] == x:
        print("Found the number")
        break
    else:
        print(".", end="")
else:
    print("Number not Found")

if 17 in lst:
    print("present")
else:
    print("absent")

print("="*20)
for element in lst:
    print(element, end=", ")
print()

print("="*20)
for idx, element in enumerate(lst):
    print(idx, " -- ", element)

print("="*20)
for ele in lst:
    if ele == 5:
        continue
    print(ele)

for i in range(1, 11):
    pass

print("End")