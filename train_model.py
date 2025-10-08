# train_model.py - Text Classification Model Training
import pandas as pd
import string
import nltk
import pickle
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

print("📚 Downloading NLTK data...")
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))
print("✅ NLTK data ready")

# Load datasets
print("📊 Loading datasets...")
try:
    fake = pd.read_csv("Fake.csv")
    real = pd.read_csv("True.csv")
    print(f"✅ Loaded {len(fake)} fake news samples and {len(real)} real news samples")
except FileNotFoundError as e:
    print(f"❌ Error: Could not find CSV files. {e}")
    exit(1)

# Label and merge
fake['label'] = 0  # Fake news
real['label'] = 1  # Real news
data = pd.concat([fake, real], axis=0).sample(frac=1, random_state=42).reset_index(drop=True)
print(f"📈 Combined dataset size: {len(data)} samples")

# Text cleaning with better preprocessing
def clean_text(text):
    if pd.isna(text) or text == '':
        return ''
    
    # Convert to lowercase
    text = str(text).lower()
    
    # Keep only alphabetic characters and spaces
    text = ''.join([c if c.isalpha() or c.isspace() else ' ' for c in text])
    
    # Split into words
    words = text.split()
    
    # Remove stopwords and very short words
    cleaned_words = [word for word in words if word not in stop_words and len(word) > 2]
    
    return ' '.join(cleaned_words)

print("🧹 Cleaning text data...")
data['text'] = data['text'].apply(clean_text)

# Remove any empty texts
data = data[data['text'].str.len() > 10].reset_index(drop=True)
print(f"✅ Cleaned data: {len(data)} samples remaining")

# Balance the dataset
fake_count = len(data[data['label'] == 0])
real_count = len(data[data['label'] == 1])
print(f"📊 Data distribution: {fake_count} fake, {real_count} real")

# Balance the classes by undersampling the majority class
min_count = min(fake_count, real_count)
fake_data = data[data['label'] == 0].sample(n=min_count, random_state=42)
real_data = data[data['label'] == 1].sample(n=min_count, random_state=42)
balanced_data = pd.concat([fake_data, real_data]).sample(frac=1, random_state=42).reset_index(drop=True)

print(f"⚖️ Balanced dataset: {len(balanced_data)} samples ({min_count} fake, {min_count} real)")

# Vectorization and model training
X = balanced_data['text']
y = balanced_data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("🔤 Creating TF-IDF vectors...")
vectorizer = TfidfVectorizer(
    max_features=10000,
    min_df=2,
    max_df=0.8,
    ngram_range=(1, 2),
    stop_words='english'
)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print("🤖 Training model...")
model = LogisticRegression(
    random_state=42,
    max_iter=1000,
    class_weight='balanced'
)
model.fit(X_train_vec, y_train)

# Evaluation
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
print(f"🎯 Model Accuracy: {accuracy:.4f}")
print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Fake', 'Real']))

# Test with specific examples
print("\n🧪 Testing with examples:")
test_examples = [
    "The President announced new economic policies in today's press conference",
    "Scientists discover breakthrough in renewable energy technology", 
    "Aliens invaded Earth yesterday and took over the government",
    "Celebrities caught in secret alien conspiracy to control media"
]

for i, text in enumerate(test_examples):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    prob = model.predict_proba(vec)[0]
    pred = model.predict(vec)[0]
    
    print(f"Example {i+1}: {'REAL' if pred == 1 else 'FAKE'} (Real: {prob[1]:.3f}, Fake: {prob[0]:.3f})")
    print(f"  Text: {text[:60]}...")
    print()

# Save model and vectorizer
print("💾 Saving models...")
try:
    pickle.dump(model, open("model.pkl", "wb"))
    pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
    print("✅ Text classification model and vectorizer saved successfully!")
except Exception as e:
    print(f"❌ Error saving models: {e}")
