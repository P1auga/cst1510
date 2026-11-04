# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

piece = "note=server=east"
key, value = piece.split("=", 1)   # maxsplit: the value keeps its own "="

print(key, value)
