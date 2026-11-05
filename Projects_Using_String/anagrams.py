# ! ANAGRAMS

phrase1 = input("Enter phrase1: ")
phrase2 = input("Enter phrase2: ")

phrase1 = phrase1.lower()
phrase2 = phrase2.lower()

if len(phrase1) != len(phrase2):
    print("not anagram")
else:
    for char in phrase1:
        if char.isalpha():
            if phrase1.count(char) != phrase2.count(char):
                print("not anagram")
                break
    else:
        print("anagrams")
