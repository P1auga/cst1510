positive_words = ['amazing', 'love', 'fantastic', 'great', 'excellent']
negative_words = ['terrible', 'worst', 'poor', 'awful', 'horrible']


def analyse_sentiment(reviews):
    counts = {"positive": 0, "negative": 0, "neutral": 0}
    negative_reviews = []

    for review in reviews:
        clean = review.strip().lower()

        if any(word in clean for word in positive_words):
            counts["positive"] += 1
        elif any(word in clean for word in negative_words):
            counts["negative"] += 1
            negative_reviews.append(clean)
        else:
            counts["neutral"] += 1

    counts["negative_reviews"] = negative_reviews
    return counts


reviews = [
    "  AMAZING product, Love it!!!  ",
    "terrible experience   ",
    "  It was okay  ",
    "WORST purchase ever",
    "  fantastic quality  ",
    "poor customer service",
    "  Not bad, not great  "
]

result = analyse_sentiment(reviews)
print("Positive:", result["positive"])
print("Negative:", result["negative"])
print("Neutral:", result["neutral"])
print("Negative reviews:", result["negative_reviews"])
