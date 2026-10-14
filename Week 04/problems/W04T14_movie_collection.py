movies = (("Inception", 2010), ("Matrix", 1999), ("Interstellar", 2014))

oldest = min(movies, key=lambda movie: movie[1])
print("Oldest movie:", oldest[0], oldest[1])

print("Titles:", [title for title, _ in movies])

try:
    movies[0] = ("Inception", 2011)
except TypeError as error:
    print("Can't change a tuple:", error)
