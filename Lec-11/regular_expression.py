# LECTURE - 11

# * REGULAR EXPRESSION :-
# ? String Pattern Matching, Validation, Generating Strings
# ? How to import module ?
# import re, import re as regex, from re import *.....

# ? Validation :-
# match(pattern, string, flag=0) --> only match the beginning of the string
# fullmatch(pattern, string, flag=0) --> checks the entire string

# ? Search and Extract :-
# search(pattern, string, flag=0) --> It will take the first match only
# findall(pattern, string, flag=0)
# split(pattern, string, flag=0)

import re

print(re.match("abc", "abcde"))
print(re.fullmatch("python", "python").group())
print(re.search("very", "python is very easy").span())
print(re.findall("can", "can you can a can as a canner"))

print("-----------------------------------------")

# ! QUANTIFIERS :-
# ? + --> 1 or more
# ? * --> 0 or more
# ? ? --> 0 or 1
# ? {m} --> exactly m
# ? {m, n} --> from m to n (by default, it will be infinity)

print(re.fullmatch("(ab)?", "ab"))
print(re.fullmatch("(ab)?", ""))
print(re.fullmatch("(ab)*", ""))
print(re.findall("[abc]+", "123 abc 987 bbcc@cbac"))

print("-----------------------------------------")
