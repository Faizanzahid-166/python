# Step 1: Simple example
numbers = [1, 2, 3, 4]
squared = [x**2 for x in numbers]
print(squared)


# Step 2: Maths for ML
import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print(np.dot(v1, v2))  # 32

# Step 3: NLP (Natural Language Processing)
# from sklearn.feature_extraction.text import CountVectorizer

# texts = ["I love AI", "AI is awesome"]
# vectorizer = CountVectorizer()

# X = vectorizer.fit_transform(texts)
# print(X.toarray())

# Step 4: Transformers
from transformers import pipeline

generator = pipeline("text-generation")
print(generator("AI is the future", max_length=20))