# LECTURE - 16

# ! List Comprehensions :- L = [exp for item in iterable]

L1 = [x for x in range(1, 5)]
print(L1)

L2 = [x.lower() for x in "PyThoN"]
print(L2)

print("----------------------------")

# ! Split Odd & Even :-

nums = [4, 8, 3, 5, 10, 7, 2, 9, 13, 6]

odd = [x for x in nums if x % 2 != 0]
even = [x for x in nums if x % 2 == 0]

print("Odd list: ", odd)
print("Even list: ", even)

print("----------------------------")

# ! Find Longest List :-

lists = [[1, 2, 3], [1, 1, 1, 1], [2, 2, 3, 4, 5]]
max_list = max(lists, key=len)

print("Maximum Length: ", max_list)
