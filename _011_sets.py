# Mutable collection of non-sequential 'keys'
# key --> hashable --> immutable
data = [1, 2, 3, "Python"]  #, {1, 2, 3}]
# print(hash(data))

st1 = set()
st2 = set(data)
st3 = {}
st4 = {1, 2, 3, 4}
st4.add(5)

print(st1, st2, st3, st4, sep="\n")

st5 = {3, 4, 5, 6}
st5.update(st4)
print(f"{st5=}")

print("="* 40, "\n")

st1 = {'a', 'b', 'c', 'd'}
st2 = {'c', 'd', 'e', 'f'}
st3 = set(st2)
print(f"{st1=}")
print(f"{st2=}")
print(f"{st3=}")
for k in st3:
    if k == 'd':
        print(id(k))
        
st3.update(st1)
print(f"{st3=}")

# print('c' in st2)
for k in st3:
    if k == 'd':
        print(id(k))

print(f"{st1=}")
print(f"{st2=}")
print(st1.intersection(st2))
print(st1 | st2)
print(st1 & st2) #st1.intersection(st2)
print(st1 - st2) #st1.difference(st2)
print(st1 ^ st2) #st1.symmetric_difference(st2)
st4 = {'d'}
print(st4<=st2) #st4.issubset(st2)

st4.add('g')
st4.remove('d') # returns None; removes item if present and error if not
# st4.remove('d') # returns None; removes item if present and error if not
st4.discard('d') # returns the popped element

st4 = set(st1)
while len(st4):
    print("-->", st4.pop())

st2.clear()

fs1 = frozenset(st1)
print(f"{fs1=}")

st1 = {1, 2, 3, 4}
st2 = {5, 6, 7}

print(st1 <= st2)
print(st1 >= st2)
print(st1.isdisjoint(st2))

print((st1 & st2) == set())


##########################################

def remove_key(sObj, key):
    if key in sObj:
        sObj.remove(key)



#---------------------------------

st = {1, 2, 3, 4, 5}

remove_key(st, 4)
print(f"{st=}")



