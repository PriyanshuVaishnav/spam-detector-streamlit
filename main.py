
import pickle
import string

# Load model and vectorizer
model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

def clean_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    return text

def predict_spam(message):
    cleaned = clean_text(message)
    vect = vectorizer.transform([cleaned])
    result = model.predict(vect)
    return "Spam" if result[0] == 1 else "Not Spam"
