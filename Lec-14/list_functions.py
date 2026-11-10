# LECTURE - 14

# * List Methods :-

# ! Adding elements methods :-
# ? append(element) : adds element at the end of the list
# ? extend(iterable) : add one or more elements at the end of the list
# ? insert(index, element) : adds the element at the given index from the input
# ? copy() : it will create the duplicate of the list


l1 = [1, 2, 3, 4, 5]

(l1.append(6))
(l1.extend([7, 8]))
(l1.insert(0, 0))

print(l1)

# ! Removing Elements :-
# ? pop(index), remove(element), clear(), del

l1.pop(2)
l1.remove(6)

print(l1)


# ! Index & Sorting :-
# ? index(element, start, end), count(element), reverse(), sort(*,key=None, reverse=False)

l2 = [10, 20, 30, 40, 10, 20, 30, 20]

print(l2.index(40))
print(l2.count(20))

(l2.reverse())
print("Reversed List: ", l2)

l3 = [70, 10, 60, 20, 50, 30, 40]
l3.sort(reverse=True)
print(l3)

l4 = ["coat", "python", "black", "cat"]
l4.sort()  # sorts the list in the increasing order
l4.sort(key=len)
print(l4)

l5 = ["apple", "Bar", "cat", "Dog"]
l5.sort(key=str.lower)
print(l5)
