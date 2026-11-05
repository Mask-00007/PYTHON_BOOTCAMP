# LECTURE - 09

# * STRING CLASS :- As an object and as class.../ Methods of class String

# ! STRING METHODS :-
# ? Find & Index : Find will give -1 error if substring or string will not be found..

S = "Hello How are you"
print(S.find("o"))  # find(sub, start, end)

# ? rfind(sub, start, end) :-

print(S.rfind("Hello"))

# ? index :- index will give ValueError: substring not found

print(S.index("a"))
print(S.index("How"))

# ? count :-

print(S.count("o"))

# ? Alignment & Padding :- ljust(width, fillChar), rjust(width, fillChar), centre(width, fillChar), zfill(width)

s1 = "hello"
print(s1.ljust(11, "X"))
print(s1.rjust(8, "*"))
print(s1.center(11, "&"))
print(s1.zfill(10))

# ? Strip Methods :- lstrip(chars), rstrip(chars), strip(chars)

s2 = "   String"
print(s2.lstrip())

s3 = "$$Hello"
print(s2.lstrip("$").lstrip())

s4 = "Hello!!!!!!"
print(s4.rstrip("!"))
print("-------------------")
s5 = "#!Hello  $ *"
print(s5.strip("#! $*"))


# ? Prefix & Suffix :- startswith(prefix, start, end), endswith(suffix, start, end),
# ? removeprefix(prefix), removesuffix(suffix), partition(sep), rpartition(sep)

x = "Rossum@gmail.com"
print(x.startswith("R"))
print(x.endswith("R"))
print(x.removeprefix("R"))
print(x.removesuffix("R"))
print(x.partition("R"))
print(x.rpartition("s"))

# ? CASE CONVERSION METHODS :- capitalize(), upper(), lower(), title(), swapcase(), casefold()

y = "hello dear"
print(y.upper())
print(y.lower())  # works for only english alphabet
print(y.title())
print(y.swapcase())  # it will interchange the casing of the characters
print(y.casefold())  # works for all the language and converts the input into lowercase


# ? INQUIRY METHODS :- It will return boolean type result.
# ? isalpha(), islower(), isupper(), istitle(),
# ? isspace(), isprintable(), isidentifier(),
# ? isdigit(), isdecimal(), isnumeric(), isascii(), isalnum()

s = "Hello World"
print(s.isalpha())
print(s.islower())
print(s.isupper())
print(s.istitle())

s = input("Enter a string: ")

print("isspace()      :", s.isspace())
print("isprintable()  :", s.isprintable())
print("isidentifier() :", s.isidentifier())
print("isdigit()      :", s.isdigit())
print("isdecimal()    :", s.isdecimal())
print("isnumeric()    :", s.isnumeric())
print("isascii()      :", s.isascii())
print("isalnum()      :", s.isalnum())
