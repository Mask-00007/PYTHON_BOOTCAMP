# LECTURE - 05

# * CONDITIONAL STATEMENTS
"""
#? RELATIONAL OPERATORS:-
                        <
                        >
                        <=
                        >=
                        ==
                        !=
    RESULT --> Boolean type (True/False)

"""

# ! If/else Statement :-
# CHECK A NUMBER IS POSITIVE OR NEGATIVE
x = int(input("Enter a number: "))

if x >= 0:
    print(x, "is positive")
else:
    print(x, "is negative")


# * COMPOUND CONDITIONAL STATEMENTS
"""
# ? LOGICAL OPERATORS:-
                       AND
                       OR
                       NOT
    RESULT --> Boolean type (True/False) 
             
"""
a = 5
b = 7
c = 3

print(a > b and a > c)
print(a > b or a > c)

# ODD OR EVEN
x = int(input("Enter a number: "))

if x % 2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")

# ELIGIBLE TO VOTE
age = int(input("Enter age: "))

if age >= 18:
    print("Person is eligible to vote")
else:
    print("Person is not eligible to vote")


# * STRING COMPARISON :- 0 < 1 < 2 < 3...< A < B < C... < a < b < c...
# Strings are compared in Lexicographic Order(Dictionary Order)
s1 = "python"
s2 = "pycharm"

print(s1 > s2)

# * SHORT CIRCUIT :- works on 'and' & 'or' operator
# ? and --> If the first condition is False, it will not check the other conditions.
# ? or --> If the first condition is True, Python does not check the remaining conditions.
# This is called short-circuit evaluation.

a = 5
b = 7
c = 3

print(a > b and a > c)
print(a > b or a > c)


# * BITWISE OPERATORS :-
"""
                       &
                       |
                       ^
                       ~
                       <<
                       >>
"""

# * CHAINING COMPARISON :- only used with 'and' operator
a = 10
b = 5
c = 3

# if a > b and b > c:
# print("True")

if a > b > c:
    print("True")  # This is known as chaining comparison


# * is & is not :-
# ? is operator checks the ID of the two variable and if it is matching, then it returns True.
a = 10
b = a

if b is a:
    print("True")
