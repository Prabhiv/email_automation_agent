import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from parse_email import parse_email

def classify_email(parsed_email):
    classified_email = parsed_email.copy()

    types = classified_email.get('email_types', [])
    classified_email['classified_type'] = types[0] if types else 'unknown'

    try:
        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        nltk.download('stopwords', quiet=True)

        text = classified_email.get('subject', '') + ' ' + classified_email.get('message_body', '')
        tokens = word_tokenize(text)

        stop_words = set(stopwords.words('english'))
        filtered = [
            w.lower() for w in tokens
            if w.isalpha() and w.lower() not in stop_words
        ]

        freq = Counter(filtered)
        classified_email['keywords'] = [w for w, _ in freq.most_common(5)]
    except Exception:
        classified_email['keywords'] = []

    return classified_email

if __name__ == "__main__":
    import pandas as pd

    df = pd.read_csv("dataset.csv")
    print("Classifying sample emails...\n")
    for _, row in df.head(5).iterrows():
        parsed = parse_email(row)
        classified = classify_email(parsed)
        print("Classified Email:")
        for k, v in classified.items():
            print(f"{k}: {v}")
        print("-" * 40)