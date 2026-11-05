# ! PALINDROME STRING

phrase = input("Enter your phrase: ")

phrase1 = phrase.replace(" ", "")
rev = phrase1[::-1]

if phrase1.casefold() == rev.casefold():
    print(phrase, "is a palindrome")
else:
    print(phrase, "is not a palindrome")
