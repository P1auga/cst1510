def palindrome_checker(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    word = input("Enter a word: ")
    print(palindrome_checker(word))
