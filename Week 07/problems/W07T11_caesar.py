def encode(text, key):
    result = ""
    for char in text:
        if char.isalpha() and char.isascii():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result


def decode(text, key):
    return encode(text, -key)


original = "Hello World! 123"
key = 5

encoded = encode(original, key)
decoded = decode(encoded, key)

print("Original:", original)
print("Encoded: ", encoded)
print("Decoded: ", decoded)
print("Round-trip ok:", decoded == original)
