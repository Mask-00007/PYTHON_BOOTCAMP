# LECTURE - 19

# ! Dictionary :-
"""
Dictionary is a collection of key value pairs where
the key and the value are separated by colon.

d1 = {1:"One"}

"""

# ! Creating dictionary : Read, Write, Update, Traverse
d1 = {1: "One", 2: "two", 3: "three"}
print(d1)

# ? Read : We cannot directly read the dictionary, we have to provide key for it.
print(d1[1])
print(d1[2])
print(d1[3])

print("-------------------------------------")

# ? Update : We will assign value to the key, and it will update the value.
# ? Update means changing the existing value.
d1[3] = "tres"
print("Updated dictionary: ", d1)

print("-------------------------------------")

# ? Write : How can we add new entry with key and value ?
d1[5] = "Five"
print("D1: ", d1)

print("-------------------------------------")

# ? Traverse : How to perform traverse operation ?
for i in d1:
    print(i, ":", d1[i])

print("-------------------------------------")

# ! Dictionary Creation Methods :-
"""
There are three methods by which dictionary can be created.
They are as follow : ITERABLE PAIRS
                   : ZIP FUNCTION
                   : ENUMERATE FUNCTION
                   
"""

# ? Iterable Pairs : using dict() function
d2 = dict([(1, "One"), (2, "two"), (3, "three")])
print(d2)

print("-------------------------------------")

# ? Zip Function : with the help of zip() function, you can pass L1 and L2, and zip() will zip them together
L1 = [1, 2, 3, 4]
L2 = ["ONE", "TWO", "THREE", "FOUR"]

d3 = dict(zip(L1, L2))
print(d3)

print("-------------------------------------")

# ? Enumerate Function : When only values are provided
# ? Enumerating means giving number in sequence starting form 0.
L3 = ["ONE", "TWO", "THREE", "FOUR"]

d4 = dict(enumerate(L3))  # By default, it will start form 0
print(d4)

d5 = dict(enumerate(L3, start=1))  # This is known as key/word argument
print(d5)

print("-------------------------------------")

# ! Dictionary Comprehensions :-
L5 = [(1, "ONE"), (2, "TWO"), (3, "THREE"), (4, "FOUR")]

d5 = {x: y for x, y in L5}
print(d5)

print("-------------------------------------")

fruits = ["Apple", "Banana", "Mango"]

d = {index: fruit for index, fruit in enumerate(fruits, start=1)}
print(d)

print("-------------------------------------")

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

d = {name: score for name, score in zip(names, scores)}
print(d)

print("-------------------------------------")

# ! Loop Over Methods :-
# ? keys(), values(), items(), get(key, alt_value), setdefault(key, alt_value)

d1 = {1: "One", 2: "two", 3: "three"}

for x in d1.keys():
    print("Keys: ", x)

print("-------------------------------------")

for y in d1.values():
    print("Values: ", y)

print("-------------------------------------")

for x, y in d1.items():
    print(x, y)

print("-------------------------------------")

print(
    d1.setdefault(5)
)  # It will assign new entry to the  dictionary key as 5 and value as None.
print(d1)  # It will print the updated dictionary.

print("-------------------------------------")

# ! Dictionary Methods :-
# ? update(), fromkeys(sequence, default), copy() , pop(key, alt_value), popitem(), clear()

# ? update() :
# Existing keys are updated.
# New keys are added.
d = {"a": 10, "b": 20}

d.update({"b": 99, "c": 30})
print(d)

print("-------------------------------------")

# ? fromkeys(sequence, default) :
# Original dictionary is not required.
# Creates a new dictionary.
keys = ["name", "age", "city"]

d = dict.fromkeys(keys, "Not Given")
print(d)

print("-------------------------------------")

# ? copy() :
d1 = {"a": 10, "b": 20}

d2 = d1.copy()
print(d2)

print("-------------------------------------")

# ? pop(key, alt_value) :
# Prevents KeyError if key doesn't exist.
d = {"a": 10, "b": 20, "c": 30}

x = d.pop("b")
print(x)
print(d)


d = {"a": 10, "b": 20}

x = d.pop("z", "Key Not Found")
print(x)

print("-------------------------------------")

# ? popitem() : Removes and returns the last inserted key-value pair.
# Follows LIFO (Last In First Out) in Python 3.7+
d = {"a": 10, "b": 20, "c": 30}

x = d.popitem()
print(x)
print(d)
