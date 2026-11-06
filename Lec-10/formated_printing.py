# LECTURE - 10

# * Formatted Printing

# ! ASCII Codes :- American Standard Code for Information Interchange
# ? A, B, C, ......, Z ---> 65, 66, 67, ......, 90
# ? a, b, c, ......, z ---> 97, 98, 99, ......, 122
# ? 0, 1, 2, ......, 9 ---> 48, 49, 50, ......, 57

# ? ord("A") --> 65, this method takes character as an input and gives the ASCII code
# ? chr(97) --> a, this method takes integer an an input and gives character as an output

print(ord("S"))
print(chr(87))

print("----------------------------------------------")

# ! Unicode :- Unified code means codes of all the language are combined together are called as uni code.
# ? Formatting of the Unicode :-
# UTF-8 : either it take 8-bit or 1 byte
# UTF-16 : either it take 16-bit or 2 byte
# UTF-32 : either it take 32-bit or 4 byte


# ! Escape Sequences :- Nothing but special characters that are use with print function
# ? \n : new line                     # ? \ : ignore newline
# ? \r : carriage return              # ? \\ : back slash
# ? \f : line feed                    # ? \' : quote
# ? \v : vertical tab                 # ? \" : double quote
# ? \b : backspace                    # ? \o : octal
# ? \a : alert                        # ? \x : hexa-decimal

print("Hello\nWorld")
print("Hello\rWorld")
print("Step1\fStep2")
print("Completed\a")
print("----------------------------------------------")

# ? \xhh : 2 digit Hexa
# ? \uxxxx : 4 digit Hexa
# ? \Uxxxxxxxx : 8 digit Hexa
# ? \N{name} : name in Unicode Database

# ! Print Function :- works on separator and end of line
# ? Signature of print Method :
# print(object, sep = "")

print("hi", 35, 12.7)
print("hi", 35, 12.7, sep="-")

# ? End of Line :
print("hello", end="\t")
print("world")
# the output will be displayed on the screen of a device and that will be known as "sys.stdout(SYSTEM.STANDARD OUTPUT)"
# print(object, sep="", end="\n", file=sys.stdout, flush=False)

print("----------------------------------------------")

# ! C Style Printing :-
# ? Control Characters : %s, %d, %i, %o, %x, %f, %F, %g, %e, %E

item = "Memory"
size = 23
price = 11.75

print("Cost of %dGB %s is $%f" % (size, item, price))

print("----------------------------------------------")

# ! Python's Formatted Printing :- We have to mention a placeholder {}...
# ? print("{index:f w.p con}".format(data))
# w --> width, p --> precision, f --> flag, con --> conversion

name = "Raj"
roll = 10
avg = 78.5

print("{0} {1} {2} ".format(name, roll, avg))

print("----------------------------------------------")
