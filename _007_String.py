# Quotes (Single, Double, Triple)
s1 = "This is Vinay's car"
s2 = 'He say, "Let us go!!"'
print(s1)
print(s2)

comment = """This is
a 
multiline
string."""
print(comment)

help = '''
Usage: asjhakfhdas
Syntax: ljaskjlhsdfj

Switches:
a: adsfads
b: asdfasdf
c: asdfasd'''
print(help)

str1 = "Component""Feature"
print(str1)


## Format strings
tech = "Python"
duration = 5
s1 = "This is a Python Training for 5 days"
s2 = "This is a {} training for {} days"
s3 = "This is a %s training for %d days"
s4 = f"This is a {tech} training for {duration} days"
print(s1)
print(s2.format(tech, duration))
print(s3%(tech, duration))
print(s4)

x = 10
y = 20
print("x =", x)
print(f"x = {x}")
print(f"{x=}, {y=}")

## Accessing the data of strings
s1 = "This is a Python Training for 5 days."
print(s1[10])
print(s1[10:15])
print(s1[10:16])
print(s1[10:])
print(s1[:16])
print(s1[:])
print(s1[-1:])
print(s1[-5:])
print(s1[-7:-1])
print(s1[-7:5])
print(s1[-7:], s1[:5])
print(s1[-7:], s1[:5], sep="")

print(f"%d%d"%(x, y))
print(x, y)
print(x, y, sep="")


print("="*20)
str = "1234567890"
print(str[:6])
print(str[:6:2])
print(str[1:6:2])
print(str[::2])
print(str[1::2])
print(str[::-1])
print(s1[::-1])
print(s1[-7:-27:-1])
print(id(s1), id(s1[-7:-27:-1]), sep="\n")
