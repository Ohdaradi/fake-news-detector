from flask import Flask, request, jsonify, render_template
import os
import urllib.request
import uuid
from werkzeug.utils import secure_filename
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def dummy_image_predict(image_path):
    # Simulate image prediction
    return int(np.random.choice([0, 1]))  # 0 = Fake, 1 = Real

def dummy_text_predict(text):
    # Simulate text prediction
    return int(np.random.choice([0, 1]))  # 0 = Fake, 1 = Real

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    image_path = None
    prediction_sources = []

    # Handle image upload
    if 'image' in request.files:
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(image_path)
            img_result = dummy_image_predict(image_path)
            prediction_sources.append(f"Image: {'Real' if img_result else 'Fake'}")

    # Handle text input
    if 'text' in request.form and request.form['text'].strip() != "":
        text = request.form['text']
        text_result = dummy_text_predict(text)
        prediction_sources.append(f"Text: {'Real' if text_result else 'Fake'}")

    # Handle link input
    if 'link' in request.form and request.form['link'].strip() != "":
        link = request.form['link']
        # Simulate a dummy link-based result (could scrape or check URL domain)
        link_result = dummy_text_predict(link)  # Same function used here
        prediction_sources.append(f"Link: {'Real' if link_result else 'Fake'}")

    if not prediction_sources:
        return jsonify({"error": "No valid input provided."}), 400

    return jsonify({"result": " | ".join(prediction_sources)})

if __name__ == '__main__':
    app.run(debug=True)
