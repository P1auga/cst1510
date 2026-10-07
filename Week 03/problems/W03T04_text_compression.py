def compress_string(text):
    if not text:
        return text

    parts = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            parts.append(f"{text[i - 1]}{count}")
            count = 1
    parts.append(f"{text[-1]}{count}")

    compressed = "".join(parts)
    return compressed if len(compressed) < len(text) else text


if __name__ == "__main__":
    print(compress_string("aaabbbbcccddeee"))
    print(compress_string("Hello"))
