feedback = [
    "The product quality is great",
    "Fast delivery but poor quality",
    "Great product and great delivery",
    "Quality could be better"
]

keywords = ['great', 'quality', 'delivery']

text = " ".join(feedback).lower()

for keyword in keywords:
    print(f"{keyword}: {text.count(keyword)}")
