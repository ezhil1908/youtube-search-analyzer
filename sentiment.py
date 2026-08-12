from textblob import TextBlob


def analyze_sentiment(text):
    """
    Analyze the sentiment of a text.

    Returns:
        Positive, Negative, or Neutral
    """
    if not text:
        return "Neutral"

    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0.05:
        return "Positive"
    elif polarity < -0.05:
        return "Negative"
    else:
        return "Neutral"


def add_sentiment(df, text_column="title"):
    """
    Add a sentiment column to a DataFrame.
    """
    df = df.copy()

    df["sentiment"] = df[text_column].apply(analyze_sentiment)

    return df