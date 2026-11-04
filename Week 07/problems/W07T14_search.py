def search(documents, query):
    query_words = query.lower().split()
    results = []

    for document in documents:
        clean = document.lower()
        score = 0
        found = []

        for word in query_words:
            count = clean.count(word)
            if count:
                score += count
                found.append(word)

        if score:
            results.append((score, found, document))

    results.sort(key=lambda item: item[0], reverse=True)

    print(f"Query: {query!r}")
    if not results:
        print("  no matches")
        return results

    for score, found, document in results:
        print(f"  score {score} | found {found} | {document}")

    return results


documents = [
    "Python is a great programming language for data science and machine learning",
    "Data analysis with Python involves cleaning and processing large datasets",
    "Machine learning models can predict outcomes from historical data",
    "Web development with JavaScript and HTML is different from data work",
    "Python data science libraries include NumPy and Pandas for data processing"
]

search(documents, "data science")
search(documents, "Python machine learning")
