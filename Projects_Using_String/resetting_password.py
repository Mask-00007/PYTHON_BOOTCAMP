# ! RESETTING PASSWORD :-

pwd1 = input("Enter your password: ")
pwd2 = input("Confirm your password: ")

if pwd1 == pwd2:
    print("Password Changed")
else:
    if pwd1.casefold() == pwd2.casefold():
        print("Please check cases and try again")
    else:
        print("Password do not match")
