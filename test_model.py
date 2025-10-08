import pickle
import string

# Load models
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Test function
def test_news(text):
    # Clean text (match training preprocessing)
    text = text.lower()
    text = ''.join([c if c.isalpha() or c.isspace() else ' ' for c in text])
    words = [w for w in text.split() if len(w) > 2]
    cleaned = ' '.join(words)
    
    vec = vectorizer.transform([cleaned])
    probs = model.predict_proba(vec)[0]
    pred = model.predict(vec)[0]
    
    print(f'Text: {text[:60]}...')
    result = "REAL" if pred == 1 else "FAKE"
    print(f'Prediction: {result} (Real: {probs[1]:.3f}, Fake: {probs[0]:.3f})')
    print()

# Test examples
examples = [
    'WASHINGTON (Reuters) - The President announced new economic policies today during a press conference at the White House, focusing on infrastructure spending and job creation programs.',
    'Breaking: Scientists at MIT discover revolutionary breakthrough in renewable energy technology that could change the world forever.',
    'Local weather report shows temperatures will reach 75 degrees today with partly cloudy skies and light winds from the southwest.',
    'Aliens invaded Earth yesterday and took over all major government buildings while world leaders remained silent about the extraterrestrial threat.',
    'Celebrity gossip reveals shocking secret alien conspiracy involving Hollywood stars and government officials working together.',
    'Stock market closes higher today as investors show confidence in new Federal Reserve policies announced earlier this week.',
    'Donald Trump just could not wish all Americans a Happy New Year and leave it at that. Instead, he had to give a shout out to his enemies and haters.'
]

print("🧪 Testing Model with Various Examples:")
print("=" * 60)

for i, example in enumerate(examples, 1):
    print(f"Example {i}:")
    test_news(example)