letter = input("Enter a letter: ").lower()

if letter in "aeiou":
    print(f"{letter} is a vowel")
elif letter == "y":
    print("y is sometimes a vowel and sometimes a consonant")
else:
    print(f"{letter} is a consonant")
