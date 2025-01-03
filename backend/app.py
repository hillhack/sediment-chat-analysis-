from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob
from collections import Counter
import re

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) to allow requests from Vue.js

# Function for text preprocessing and word frequency count
def preprocess_and_analyze(text):
    # Remove non-alphabetic characters and split the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Calculate word frequencies
    word_count = Counter(words)
    
    # Perform sentiment analysis using TextBlob
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # Sentiment score between -1 and 1
    
    return word_count, sentiment

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.json  # Get data from the request body
    user_input = data.get('text', '')
    
    # Perform analysis
    word_count, sentiment = preprocess_and_analyze(user_input)
    
    # Return the analysis results as JSON
    return jsonify({'word_count': word_count, 'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
