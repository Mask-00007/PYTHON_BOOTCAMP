# LECTURE - 21


# ! Maximum of Three :- only positional
def max3(a, b, c, /):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


a = int(input("Enter first number  : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number  : "))

print("Maximum =", max3(a, b, c))


print("------------------------------")


# ! Simple Interest :-
# Keyword-Only Arguments
def simple_interest(*, principal, rate, time):
    return (principal * rate * time) / 100


p = float(input("Enter Principal : "))
r = float(input("Enter Rate (%)  : "))
t = float(input("Enter Time      : "))

si = simple_interest(principal=p, rate=r, time=t)

print("Simple Interest =", si)

print("------------------------------")

# ! Pangram Phrase :-
s = input("Enter a sentence: ").lower()

letters = set()

for ch in s:
    if "a" <= ch <= "z":
        letters.add(ch)

if len(letters) == 26:
    print("Pangram")
else:
    print("Not a Pangram")
