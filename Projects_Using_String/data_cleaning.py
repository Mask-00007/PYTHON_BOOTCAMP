# ! DATA CLEANING :-

scan = input("Enter your data: ")
clean = ""

for char in scan:
    if char.isalpha() or char.isspace():
        clean = clean + char
    else:
        clean = clean + " "

clean = " ".join(clean.split())
print("The formatted data: ", clean)
