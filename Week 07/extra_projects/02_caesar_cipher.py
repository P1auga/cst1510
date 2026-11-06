"""Caesar Cipher - shift letters, wrap with % 26, leave everything else alone."""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_text(original_text, shift_amount):
    """Shift every letter by shift_amount, passing other characters through."""
    output = ""

    for char in original_text:
        if char.lower() in ALPHABET:
            position = ALPHABET.index(char.lower())
            new_position = (position + shift_amount) % 26
            letter = ALPHABET[new_position]
            output += letter.upper() if char.isupper() else letter
        else:
            output += char

    return output


def encrypt(original_text, shift_amount):
    """Shift forwards."""
    return shift_text(original_text, shift_amount)


def decrypt(original_text, shift_amount):
    """Shift backwards - the same function with a negative shift."""
    return shift_text(original_text, -shift_amount)


def caesar(direction, text, shift):
    """Decrypt when direction is 'decode', otherwise encrypt."""
    if direction == "decode":
        return decrypt(text, shift)
    return encrypt(text, shift)


running = True

while running:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt: ").strip().lower()
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))

    print(f"Result: {caesar(direction, text, shift)}")

    if input("Type 'yes' to go again, anything else to stop: ").strip().lower() != "yes":
        running = False
