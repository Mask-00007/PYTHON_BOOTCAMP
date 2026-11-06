# LECTURE - 12

# * What is List ?
"""
# ? List is ordered collection of elements
Let us understand list...
L1 = [1,2,3,4,5,6]
L2 = [1.5,2.7,3.4,4.6,5.5,6.3]

Another method for creating list :- L3 = list((iterable))

# ? List is heterogenous
# ? List is mutable
# ? It can have duplicates

"""

# ! INDEXING & SLICING :- READ-WRITE

# ? Read : Indexing/Slicing
l1 = [3, 6, 9, 12, 15, 18, 21]
print(l1[4])  # This is indexing
print(l1[:])  # This is slicing
print(l1[::2])
print(l1[::-1])
print(l1[4::-1])

print("---------------------------------")

# ? Write : Means, modification is possible
l2 = [1, 2, 3, 4, 5]
l2[4] = 10
print(l2)

l2[3] = [11, 12]
print(l2)  # We can have nested list too.

print("---------------------------------")

# ! OPERATIONS ON LIST :-
# ? Concatenation(+), Repetition(*), Membership(in, not in), List Comparison

l3 = [1, 2, 3]
l4 = [5, 6, 7]
print(l3 + l4)  # Concatenation
print(l3 + [4])  # It will concatenate and give a new list, modification is not allowed

# For modification, use extend()
l3.extend([9, 8, 7])
print(l3)

l5 = [1, 2, 3]
print(
    l5 * 3
)  # It will repeat the same list 3 times and creates a new list with repeating elements
print(3 in l5)

n_l1 = [[1, 2], [3, 4], 5]
print([3, 4] in n_l1)

print("---------------------------------")

# ! LIST TRAVERSALS :- can be possible using for loop, while loop..

li = [5, 6, 7, 8, 9]

for x in li:
    print(x)

print("---------------------------------")

# ? for loop using range function :
for i in range(len(li)):
    print(li[i])

print("---------------------------------")

# ? using while loop :
i = 0

while i < len(li):
    print(li[i])
    i = i + 1
