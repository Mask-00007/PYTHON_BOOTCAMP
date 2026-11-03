# LECTURE - 06

# * LOOPS :-
"""
#? While Loop also known to be Sentinel Loop
#? For Loop also known to be For each Loop

"""

# Example 01
n = 5

while n > 0:
    print(n)
    n = n - 1

print("-----------------------------------------")

# Example 02
n = 3
i = 0

while i < 10:
    i = i + 1
    print(n, "X", i, "=", n * i)

print("-----------------------------------------")

# Example 03
n = 2546

while n > 0:
    r = n % 10
    print(r)
    n = n // 10

print("-----------------------------------------")

# ! COUNT THE DIGITS OF A NUMBER
x = int(input("Enter your number: "))
i = 0

while x > 0:
    i = i + 1
    x = x // 10
    print(
        "Number of digits: ", i
    )  # It iterates every count one by one but if you want the final count only, move print() outside the loop

print("-----------------------------------------")

# ! SUM OF DIGITS OF A NUMBER
y = int(input("Enter your number: "))
sum = 0

while y > 0:
    digit = y % 10
    sum = sum + digit
    y = y // 10

print("Sum of the digits of a number: ", sum)

print("-----------------------------------------")


# ! REVERSE A NUMBER
z = int(input("Enter your number: "))
rev = 0

while z > 0:
    r = z % 10
    rev = rev * 10 + r
    z = z // 10
print("Reverse of the input is: ", rev)

print("-----------------------------------------")

# ! PALINDROME VALIDATION
w = int(input("Enter your number: "))
original = w
rev = 0

while w > 0:
    digit = w % 10
    rev = rev * 10 + digit
    w //= 10

if rev == original:
    print("Palindrome")
else:
    print("Not Palindrome")

print("-----------------------------------------")


# ! FIND MAX ELEMENT
n = 5
print("Enter", n, "Elements")
i = 0
Max = 0

while i < n:
    i = i + 1
    x = int(input(""))

    if x > Max:
        Max = x

print("Max element is: ", Max)

print("-----------------------------------------")

# ! FIND MAX AND MIN ELEMENT

n = 5
print("Enter", n, "Elements")

i = 0
x = int(input("Enter number: "))

Max = x
Min = x

i = 1

while i < n:
    x = int(input(""))

    if x > Max:
        Max = x

    if x < Min:
        Min = x

    i = i + 1

print("Max element is:", Max)
print("Min element is:", Min)

print("-----------------------------------------")


# * else Suite :- works well with while, for, try & if statements
i = 0

while i < 5:
    i = i + 1
    print(i)

    if i == 3:
        break

else:
    print("end of loop")

print("end of program")
