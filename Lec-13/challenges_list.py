# LECTURE - 13

# ! Remove Duplicates :-
List1 = list(map(int, input("Enter numbers: ").split()))
List2 = []

for el in List1:
    if el not in List2:
        List2.append(el)

print(List2)

print("------------------------")

# ! Rotate a list :-
List1 = list(map(int, input("Enter numbers: ").split()))
n = int(input("Enter number of rotations: "))

RotatedList = List1[n:] + List1[:n]

print("Rotated list: ", RotatedList)

print("------------------------")

# ! Palindrome List :-
List1 = list(map(int, input("Enter numbers: ").split()))

rev_list = List1[::-1]
if List1 == rev_list:
    print("List is palindrome")
else:
    print("List is not palindrome")
