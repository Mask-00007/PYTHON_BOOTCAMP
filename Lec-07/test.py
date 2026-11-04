# LECTURE - 07

# * FOR LOOP :-
"""

Before moving to the for loop, one should must know about the range() function.
#? range(start, stop, step) :
                            : by default, the start value is always 0.
                            : step is optional(default value is 1).
                            : stop will be stop - 1.

"""

# ! SUM OF n NATURAL NUMBERS
n = int(input("Enter number: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum of n:", sum)

print("------------------------------------")

# ! FACTORIAL OF A NUMBER
n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial of number:", fact)

print("------------------------------------")

# ! FIBONACCI SERIES
a = 0
b = 1
n = int(input("Enter number: "))

for i in range(0, n):
    c = a + b
    a = b
    b = c

print(a)

print("------------------------------------")

# ! FACTORS OF A NUMBER
n = int(input("Enter your number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)

print("------------------------------------")

# ! CHECK IF PRIME NUMBER
n = int(input("Enter your number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
    if count > 2:
        break

if count == 2:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")

print("------------------------------------")


# * NESTED LOOP :- used for accessing two dimensional data or tabular data or matrices
# ! Prime numbers between 1 to 100
for n in range(1, 101):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        print(n)


print("------------------------------------")

# ! Patterns
for i in range(1, 6):
    for j in range(1, 6):
        print("*", end="   ")

    print("")


print("------------------------------------")

# Lower Triangle Matrix
for i in range(1, 6):
    for j in range(1, 6):
        if i >= j:
            print("*", end=" ")

    print("")


print("------------------------------------")

# ? Another Method
for i in range(1, 6):
    print("* ", *i)


print("------------------------------------")

# * Match Case :-
dayNo = int(input("Enter a day number: "))

match dayNo:
    case 0:
        print("Monday")
    case 1:
        print("Tuesday")
    case 2:
        print("Wednesday")
    case 3:
        print("Thursday")
    case 4:
        print("Friday")
    case 5:
        print("Saturday")
    case 6:
        print("Sunday")
    case _:
        print("Invalid day number")
