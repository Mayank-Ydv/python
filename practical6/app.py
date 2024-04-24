from textblob import TextBlob

# Define some text
text = "I love coding and eating! I love coding and eating!I love coding and eating!I love coding and eating!"

# Create a TextBlob object
blob = TextBlob(text)

# Perform sentiment analysis
sentiment_score = blob.sentiment.polarity

# Print the sentiment score
print("Sentiment Score:", sentiment_score)

# Print the sentiment interpretation
if sentiment_score > 0:
    print("This text is positive.")
elif sentiment_score < 0:
    print("This text is negative.")
else:
    print("This text is neutral.")
