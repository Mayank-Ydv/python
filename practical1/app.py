import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Download NLTK resources
nltk.download('vader_lexicon')

# Function to perform sentiment analysis
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    return sentiment_score

# Function to visualize sentiment analysis results
# Function to visualize sentiment analysis results
def visualize_sentiment(sentiment_score):
    labels = sentiment_score.keys()
    sizes = [sentiment_score[label] for label in labels]
    colors = ['gold', 'lightskyblue']
    
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    st.pyplot()


# Streamlit app
def main():
    st.title("Text Sentiment Analyzer")
    st.write("This app analyzes the sentiment of text.")
    
    # Input text from the user
    text = st.text_area("Enter text here:")
    
    if st.button("Analyze"):
        # Perform sentiment analysis
        sentiment_score = analyze_sentiment(text)
        
        # Visualize sentiment analysis results
        visualize_sentiment(sentiment_score)
        
        # Display sentiment scores
        st.write("Sentiment Scores:")
        st.write(sentiment_score)

if __name__ == "__main__":
    main()
# streamlit run app.py code to start