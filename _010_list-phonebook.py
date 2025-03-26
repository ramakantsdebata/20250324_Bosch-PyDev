pb = ["Manish", "Abhijeet", "Rakesh", "Kiran"]


def add_entry(coll, entry):
    coll.append(entry)
    return coll

# updated = add_entry(list(pb), "Pravin")  # <-- Valid code; Same effect as below
updated = add_entry(pb[:], "Pravin")
print(f"{updated=}")

print(f"{pb=}")

print("="* 40)
s1 = "This is a string"

def punctuate(st:str, punctuation):
    print(id(st), st)
    st += punctuation
    print(id(st), st)
    return st

print(id(s1), s1)
res = punctuate(s1, ".")
print("Calling...")
print(id(res), res)
print(id(s1), s1)



