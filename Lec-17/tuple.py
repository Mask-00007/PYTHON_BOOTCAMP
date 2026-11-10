# LECTURE - 17

# ! TUPLE :-
"""
Tuple is same as List but immutable.
It will be created with the help of round brackets.

# ? Creation of tuple :
t1 = (1, 2, 3, 4)
t2 = tuple([1, 2, 3, 4, 5])
t3 = ()
t4 = (3, )
t5 = 10, 11, 12, 13, 14

"""

# ! Tuple Comprehensions and Methods :-
# ? T = (*(exp for item in iterable ),)

T1 = (*(x for x in range(1, 5)),)
print(T1)

print("-------------------------------")

# ! Indexing & Slicing :- Tuple
"""
Indexing → Access a single element using its position.
Positive Indexing starts from 0.
Negative Indexing starts from -1.
Slicing → Access multiple elements using:
# ? tuple[start : stop : step]

"""

colors = ("Red", "Green", "Blue", "Yellow", "Black")

# Indexing
print(colors[0])  # Red
print(colors[2])  # Blue
print(colors[-1])  # Black

print("-------------------------------")

# Slicing
print(colors[1:4])  # ('Green', 'Blue', 'Yellow')
print(colors[:3])  # ('Red', 'Green', 'Blue')
print(colors[2:])  # ('Blue', 'Yellow', 'Black')
print(colors[::-1])  # Reversed tuple

print("-------------------------------")

# ! Packing & Unpacking :-

T1 = 1, 2, 3, 4, 5
print(T1)  # This is called as packing
print(type(T1))

a, b, c, d, e = T1
print(a, b, c, d, e)  # This is called as unpacking

print("-------------------------------")

# a, b, c = T1
# This will give error.
# So, unpacking happens if the number of values and the variables are equal.

a, b, *c = T1
print(a, b, *c)
print(*c)
print(a, b, c)
