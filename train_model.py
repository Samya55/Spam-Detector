import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Sample data (replace with your actual data)
texts = [
    'Free money now!!!',
    'Hi, how are you?',
    'Buy cheap products here',
    'Hey, wanna catch up later?',
    'Congrats, you’ve won a lottery!',
    'Let’s go for lunch!',
    'This is spam, win a prize',
    'How about a meeting tomorrow?',
]
labels = [1, 0, 1, 0, 1, 0, 1, 0]  # 1 for spam, 0 for not spam

# Create a pipeline that first vectorizes the text and then applies a classifier
model = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

# Train the model with the data
model.fit(texts, labels)

# Save the trained model and vectorizer
joblib.dump(model, 'spam_classifier_model.joblib')
print("Model saved successfully as spam_classifier_model.joblib")

# Save the vectorizer (in case you want to use it separately)
vectorizer = model.named_steps['tfidfvectorizer']
joblib.dump(vectorizer, 'spam_classifier_vectorizer.joblib')
print("Vectorizer saved successfully as spam_classifier_vectorizer.joblib")
