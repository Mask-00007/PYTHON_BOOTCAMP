CardNo = input("Enter your card number: ")

lastdigits = CardNo[-4:]
four = "X" * 4 + " "
DispNo = four * 3 + lastdigits

print(DispNo)
