# LECTURE - 18

# ! SETS :-
"""
Set is a collection of elements which are defined inside a curly brackets.
It does not contain duplicate values.
It is heterogeneous in nature.
Indexing and Slicing is not allowed.
It is unordered data type.
It is mutable as well.

# ? Creating set :-
s1 = {1, 2, 3, 4, 5}
s2 = set(iterable)
s3 = set("python")
s4 = set{8} ; empty set is not possible, we have to fill at least one value.

"""

# ? SET IS MUTABLE :- A set is mutable, but its elements must be immutable.
# add()
# remove()
# discard()
# pop()
# clear()
# update()

fruits = {"apple", "banana", "mango"}

fruits.add("orange")

print(fruits)

fruits.remove("banana")

print(fruits)

nums = {1, 2, 3}

nums.update([4, 5, 6])

print(nums)

print("----------------------------")

# ! How a Set Works Internally ?
"""
A Python set is implemented using a hash table.

When you add an element to a set:

Python calculates its hash value using hash().
The hash value determines where the element should be stored in memory.
To search for an element, Python computes the hash again and directly jumps to that location instead of scanning every element.

Time taken for the inserting will be O(1).

"""

# ! Set in Python VS Mathematics

# Mathematics:
# 1. Collection of unique elements.
# 2. No duplicate values.
# 3. Order does not matter.
# 4. Supports Union (∪), Intersection (∩), Difference (-).
# Example:
# A = {1, 2, 3}
# B = {3, 4, 5}

# Python:
A = {1, 2, 3}
B = {3, 4, 5}

print("Union:", A | B)  # {1, 2, 3, 4, 5}
print("Intersection:", A & B)  # {3}
print("Difference:", A - B)  # {1, 2}
print("Symmetric Diff:", A ^ B)  # {1, 2, 4, 5}

print("----------------------------")

# Additional Python Features:
# 1. Implemented using Hash Tables.
# 2. Fast lookup (O(1) average).
# 3. Mutable (can add/remove elements).
# 4. Elements must be immutable/hashable.


# ! Mathematics vs Python Set Operations

A = {1, 2, 3}
B = {3, 4, 5}

# ∪ (Union)
print("A ∪ B =", A | B)
# Output: {1, 2, 3, 4, 5}

# ∩ (Intersection)
print("A ∩ B =", A & B)
# Output: {3}

# - (Difference)
print("A - B =", A - B)
# Output: {1, 2}

# Δ (Symmetric Difference)
print("A Δ B =", A ^ B)
# Output: {1, 2, 4, 5}

# ⊆ (Subset)
C = {1, 2}
print("C ⊆ A =", C.issubset(A))
# Output: True

# ∈ (Membership)
print("2 ∈ A =", 2 in A)
# Output: True

print("10 ∈ A =", 10 in A)
# Output: False

print("----------------------------")

# ! Operators on Set :-

# |       Union
# |=      Union Update

# &       Intersection
# &=      Intersection Update

# -       Difference
# -=      Difference Update

# ^       Symmetric Difference
# ^=      Symmetric Difference Update

# in      Membership
# not in  Non-Membership

# <=      Subset
# <       Proper Subset

# >=      Superset
# >       Proper Superset

# ==      Equality
# !=      Inequality

# ! Set Operators Cheat Sheet

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {1, 2}

# ? UNION ( ∪ )
print("A | B =", A | B)
# {1, 2, 3, 4, 5, 6}

# ? UNION UPDATE ( ∪= )
temp = A.copy()
temp |= B
print("A |= B ->", temp)
# {1, 2, 3, 4, 5, 6}

# ? INTERSECTION ( ∩ )
print("A & B =", A & B)
# {3, 4}

# ? INTERSECTION UPDATE ( ∩= )
temp = A.copy()
temp &= B
print("A &= B ->", temp)
# {3, 4}

# ? DIFFERENCE ( − )
print("A - B =", A - B)
# {1, 2}

# ? DIFFERENCE UPDATE ( −= )
temp = A.copy()
temp -= B
print("A -= B ->", temp)
# {1, 2}

# ? SYMMETRIC DIFFERENCE ( Δ )
print("A ^ B =", A ^ B)
# {1, 2, 5, 6}

# ? SYMMETRIC DIFFERENCE UPDATE ( Δ= )
temp = A.copy()
temp ^= B
print("A ^= B ->", temp)
# {1, 2, 5, 6}

# ? MEMBERSHIP ( ∈ )
print("3 in A =", 3 in A)
# True

# ? NON-MEMBERSHIP ( ∉ )
print("10 not in A =", 10 not in A)
# True

# ? SUBSET ( ⊆ )
print("C <= A =", C <= A)
# True

# ? PROPER SUBSET ( ⊂ )
print("C < A =", C < A)
# True

# ? SUPERSET ( ⊇ )
print("A >= C =", A >= C)
# True

# ? PROPER SUPERSET ( ⊃ )
print("A > C =", A > C)
# True

# ? EQUALITY ( = )
print("{1, 2, 3} == {3, 2, 1} =", {1, 2, 3} == {3, 2, 1})
# True

# ? INEQUALITY ( ≠ )
print("A != B =", A != B)
# True

print("----------------------------")

# ! Methods for adding and deleting elements :-
# ? For adding :- add(element), update(iterable), copy()
# ? For removing :- pop(), discard(element), remove(element), clear()

s = {10, 20, 30}

# ? add(element) -> Adds a single element
s.add(40)
print("add(40)                :", s)
# {10, 20, 30, 40}

# ? update(iterable) -> Adds multiple elements
s.update([50, 60])
print("update([50, 60])       :", s)
# {10, 20, 30, 40, 50, 60}

# ? copy() -> Creates a shallow copy
c = s.copy()
print("copy()                 :", c)
# {10, 20, 30, 40, 50, 60}

# ? pop() -> Removes and returns an arbitrary element
item = s.pop()
print("pop() removed          :", item)
print("after pop()            :", s)

# ? discard(element) -> Removes element if present
s.discard(20)
print("discard(20)            :", s)

# No error if absent
s.discard(100)
print("discard(100)           :", s)

# ? remove(element) -> Removes element if present
s.remove(30)
print("remove(30)             :", s)

# Raises KeyError if absent
# s.remove(100)

# ? clear() -> Removes all elements
s.clear()
print("clear()                :", s)
# set()

print("----------------------------")

# ! Set Comprehensions :- S = {exp for item in iterable}

S1 = {x for x in range(1, 5)}
print(S1)

S2 = {x**2 for x in [-2, -1, 0, 1, 2]}
print(S2)  # It will take only distinct values.

S3 = {x.lower() for x in "PhillipInes"}
print(S3)  # It will take only distinct values.
