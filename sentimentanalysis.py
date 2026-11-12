
from textblob import TextBlob

print("🤖 Sentiment Analysis AI")
print("------------------------")

while True:
    text = input("\nEnter a sentence (or 'exit'): ")

    if text.lower() == "exit":
        break

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    print("Sentiment:", sentiment)
    print("Confidence score:", round(abs(polarity), 2))
