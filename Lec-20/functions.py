# LECTURE - 20

# ! Functions :- Function is a piece of code which performs specific task.
# ? How can i define my own function ?
# def fun1(<parameter>):
#     return result

# ? How to write functions ? --> Header, Return, Calling, Parameters
"""
SKELETON :- def fun_name(<parameter list>):
                Statement 1
                Statement 2
                return value

"""


# ? Writing function for the volume of the cuboid :-
def volume(length, breadth, height):
    vol = length * breadth * height
    return vol


v = volume(10, 5, 3)
print("Volume:", v)

print("---------------------")


# ! Positional VS Keyword Arguments :-
# ? Positional Arguments : Values are assigned based on their position.
def add(a, b):
    print(a, b)
    return a + b


sum = add(10, 20)
print("Sum:", sum)

print("---------------------")


# ? Keyword Arguments :
# Values are assigned using parameter names.
# Order does not matter.
def student(name, age, city):
    print("Name :", name)
    print("Age  :", age)
    print("City :", city)


student(age=21, city="Patna", name="Ram")

print("---------------------")


# ? Mixed Arguments :-
# Positional arguments + Keyword arguments together.
# Positional arguments must come first.
def student(name, age, city):
    print(name, age, city)


student("Dha", age=21, city="Patna")


print("---------------------")


# ! Default Arguments :-
# Parameters are given default values.
# If no argument is passed, the default value is used.
def volume(l=1, b=1, h=1):
    v = l * b * h
    return v


print(volume(10, 5, 3))
print(volume(10, 5))
print(volume(10))
print(volume())

print("---------------------")


# ? Positional-Only Arguments :-
# Parameters placed before "/" can only be passed by position.
# They cannot be passed using parameter names (keywords).
# Introduced in Python 3.8.
# /  → Before it = Positional-Only
# *  → After it = Keyword-Only
def student(name, age, /):
    print(name, age)


student("Prem", 21)  # ✅ Valid
# student(name="Prem", age=21)  # ❌ Error

print("---------------------")


# ? Keyword-Only Arguments :-
# Parameters placed after "*" can only be passed using keywords.
# They cannot be passed by position.
def student(*, name, age):
    print(name, age)


student(name="Randy", age=21)  # ✅ Valid
# student("Randy", 21)  # ❌ Error

print("---------------------")


# ? Positional-Only + Normal + Keyword-Only Arguments :-
def student(name, age, /, city, *, country):
    print(name, age, city, country)


student("Snail", 21, "Patna", country="India")
