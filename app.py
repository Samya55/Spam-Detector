from flask import Flask, render_template, request
import re  # Import regular expressions if you want to add pattern matching in the future

app = Flask(__name__)

# Expanded function for spam classification
def predict_spam(message):
    # List of common spam keywords
    spam_keywords = ["win", "free", "prize", "gift", "claim", "congratulations"]
    message = message.lower()  # Convert message to lowercase to avoid case-sensitive matching

    # Check if any spam keyword is in the message
    for keyword in spam_keywords:
        if keyword in message:
            return "Spam"

    # Optional: You can add regex-based pattern matching for URLs or other signs of spam
    if re.search(r'http[s]?://', message):  # Detect URLs (often in spam)
        return "Spam"

    return "Not Spam"  # Default is Not Spam if no keywords or patterns match

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    result = predict_spam(message)  # Call the updated spam classification function
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
