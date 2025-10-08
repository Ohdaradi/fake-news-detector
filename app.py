# === app.py ===
from flask import Flask, request, jsonify, render_template
import os
import pickle
import string
import csv
import pandas as pd
import base64
import numpy as np
from datetime import datetime
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for matplotlib
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename

# Simple text processing without NLTK to avoid dependency issues
NLTK_AVAILABLE = False
print("Using basic text processing (NLTK disabled to avoid dependency conflicts)")

import warnings
warnings.filterwarnings('ignore')

# Set TensorFlow to use less verbose logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

try:
    import tensorflow as tf
    tf.get_logger().setLevel('ERROR')
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing.image import load_img, img_to_array
    TENSORFLOW_AVAILABLE = True
    print("✅ TensorFlow loaded successfully")
except ImportError as e:
    TENSORFLOW_AVAILABLE = False
    print(f"⚠️ TensorFlow not available: {e}")
    load_model = None
    load_img = None
    img_to_array = None

# === Flask App Setup ===
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# === Load Models ===
try:
    with open("model.pkl", "rb") as f:
        text_model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    print("✅ Text models loaded successfully")
except FileNotFoundError as e:
    print(f"❌ Error loading text models: {e}")
    text_model = None
    vectorizer = None

# Load image model only when needed (lazy loading)
image_model = None

def load_image_model():
    global image_model
    if image_model is None and TENSORFLOW_AVAILABLE:
        try:
            image_model = load_model("image_model.h5")
            print("✅ Image model loaded successfully")
        except Exception as e:
            print(f"❌ Error loading image model: {e}")
    return image_model

# Basic stopwords list for text processing
stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'shall', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'not', 'no', 'yes', 'get', 'got', 'go', 'going', 'went', 'come', 'came', 'see', 'saw', 'said', 'say', 'says', 'know', 'knew', 'think', 'thought', 'make', 'made', 'take', 'took', 'give', 'gave', 'put', 'let', 'tell', 'told'}
print("✅ Basic stopwords loaded successfully")

# === Helper Functions ===
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def clean_text(text):
    if not text or text.strip() == '':
        return ''
    
    # Convert to lowercase
    text = str(text).lower()
    
    # Keep only alphabetic characters and spaces (same as training)
    text = ''.join([c if c.isalpha() or c.isspace() else ' ' for c in text])
    
    # Split into words
    words = text.split()
    
    # Remove very short words and basic stopwords if available
    cleaned_words = [word for word in words if len(word) > 2]
    if stop_words:
        cleaned_words = [word for word in cleaned_words if word not in stop_words]
    
    return ' '.join(cleaned_words)

def real_text_predict(text):
    if not text_model or not vectorizer:
        return 'Error', 0, 0
    
    try:
        cleaned = clean_text(text)
        vec = vectorizer.transform([cleaned])
        probs = text_model.predict_proba(vec)[0]
        fake_prob = round(probs[0] * 100, 2)  # Class 0: Fake
        real_prob = round(probs[1] * 100, 2)  # Class 1: Real
        prediction = 'Real' if real_prob > fake_prob else 'Fake'
        return prediction, real_prob, fake_prob
    except Exception as e:
        print(f"Error in text prediction: {e}")
        return 'Error', 0, 0



def real_image_predict(image_path):
    if not TENSORFLOW_AVAILABLE:
        return 0.5  # Default neutral prediction
    
    try:
        model = load_image_model()
        if model is None:
            return 0.5
            
        img = load_img(image_path, target_size=(224, 224))
        img = img_to_array(img) / 255.0
        img = img.reshape(1, 224, 224, 3)
        prediction = model.predict(img, verbose=0)[0][0]
        return round(prediction, 2)
    except Exception as e:
        print(f"Error in image prediction: {e}")
        return 0.5


def dummy_url_predict(url):
    return int(np.random.choice([0, 1]))

def log_to_csv(predictions):
    file_path = "prediction_logs.csv"
    fieldnames = ['timestamp', 'text', 'link', 'image_path', 'result']
    text = request.form.get('text', '')
    link = request.form.get('link', '')
    image = request.files.get('image')
    image_name = image.filename if image else ''
    row = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'text': text.strip()[:150],
        'link': link,
        'image_path': image_name,
        'result': predictions
    }
    file_exists = os.path.exists(file_path)
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

# === Routes ===
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    prediction_sources = []
    image_path = None

    # Handle image
    if 'image' in request.files:
        file = request.files['image']
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(image_path)
            img_result = real_image_predict(image_path)
            prediction_sources.append(f"Image: {'Real' if img_result >= 0.5 else 'Fake'} ({img_result*100:.1f}%)")

    # Handle text
    if 'text' in request.form and request.form['text'].strip():
        text = request.form['text']
        text_label, real_p, fake_p = real_text_predict(text)
        if text_label != 'Error':
            prediction_sources.append(f"Text: {text_label} (Real: {real_p}%, Fake: {fake_p}%)")
        else:
            prediction_sources.append("Text: Error in prediction")

    # Handle link
    if 'link' in request.form and request.form['link'].strip():
        link = request.form['link']
        link_result = dummy_url_predict(link)
        prediction_sources.append(f"Link: {'Real' if link_result else 'Fake'}")

    if not prediction_sources:
        return jsonify({"error": "No valid input provided."}), 400

    result_str = " | ".join(prediction_sources)
    log_to_csv(result_str)

    return jsonify({"result": result_str})

@app.route('/dashboard')
def dashboard():
    try:
        if not os.path.exists('prediction_logs.csv'):
            return render_template("dashboard.html", plot_url=None, message="No prediction logs available yet.")
        
        df = pd.read_csv("prediction_logs.csv")
        if df.empty:
            return render_template("dashboard.html", plot_url=None, message="No prediction data available.")
        
        results = df['result'].value_counts()
        fig, ax = plt.subplots(figsize=(10, 6))
        results.plot(kind='bar', color=['green', 'red'], ax=ax)
        ax.set_title("Fake vs Real Predictions")
        ax.set_ylabel("Count")
        ax.set_xlabel("Prediction Results")
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        buf = BytesIO()
        plt.savefig(buf, format="png", dpi=150)
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode("utf-8")
        plt.close()
        
        return render_template("dashboard.html", plot_url=img_base64, message=None)
    except Exception as e:
        print(f"Error generating dashboard: {e}")
        return render_template("dashboard.html", plot_url=None, message="Error generating dashboard.")



if __name__ == '__main__':
    app.run(debug=True)
