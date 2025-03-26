# Mutable collection of 'keys'
# key --> hashable --> immutable
data = [1, 2, 3, "Python"]  #, {1, 2, 3}]
# print(hash(data))

st1 = set()
st2 = set(data)
st3 = {}
st4 = {1, 2, 3, 4}
st4.add(5)

print(st1, st2, st3, st4, sep="\n")