# LECTURE - 03


# * BASE CONVERSION FUNCTIONS
"""
Number Systems:
          DECIMAL --> base 10 {0...9}
          BINARY --> base 2 {0,1}
          OCTAL --> base 8 {0...7}
          HEXADECIMAL --> base 16 {0..9, A..F}

OUTPUT --> All the built-in functions returns output as STRING.

PREFIXES --> Binary - 0b....
             Octal - 0o...
             Hexadecimal - 0x...
"""

a = 10
print(bin(a))
print(hex(a))
print(oct(a))

# * TYPE CONVERSION
"""
Type Conversion: Python is having built in functions for converting
                 one data type into another data type. So, those built
                 in functions are called as type conversion functions.
                                  
"""

# ! For INTEGER
b = 16.59
print(int(b))
print(bool(b))
print(complex(b))

c = "Alexa"  # You have to pass only valid strings like numbers not letters
# print(int(c))

d = "125"
print(int(d))

e = "0b1010"
print(int(e, 2))  # Have to provide, then only it will convert into decimal


# ! For FLOAT
s1 = 125
s2 = True
s3 = "12.75"
print(float(s1), type(s1))
print(float(s2))
print(float(s3))

# ! For BOOLEAN
d1 = True
d2 = False
d3 = 12
print(bool(d1))
print(bool(d2))
print(bool(d3))

# ! For STRING
e1 = "10"
e2 = "-12"
e3 = "-1.2E-3"
print(str(e1))
print(str(e2))
print(str(e3))
