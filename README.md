# 🔍 RealFake AI - Advanced Multi-Modal Fake News Detection System

A modern, responsive web application powered by AI for detecting fake news through text analysis, image processing, and URL validation.

![RealFake AI Banner](https://img.shields.io/badge/RealFake%20AI-v2.0-blue?style=for-the-badge&logo=artificial-intelligence)

## ✨ **Enhanced Features**

### 🎨 **Modern UI/UX Design**
- **Glassmorphism Design**: Beautiful frosted glass effects with backdrop blur
- **Gradient Backgrounds**: Stunning color gradients throughout the interface
- **Smooth Animations**: CSS transitions, hover effects, and loading animations
- **Dark/Light Mode**: Intelligent theme switching with system preference detection
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices

### 🚀 **Advanced Functionality** 
- **Multi-Modal Detection**: Simultaneous analysis of text, images, and URLs
- **Real-time Predictions**: Instant AI-powered fake news detection
- **Interactive Dashboard**: Beautiful analytics with animated statistics
- **Smart Loading States**: Progress indicators and smooth state transitions
- **No Login Required**: Direct access to all features

### 📱 **Responsive Features**
- **Mobile-First Design**: Optimized for all screen sizes
- **Touch-Friendly Interface**: Large buttons and intuitive navigation
- **Adaptive Layouts**: Flexible grid systems and component scaling
- **Cross-Browser Support**: Works seamlessly across all modern browsers

## 🛠️ **Technology Stack**

### **Backend**
- **Flask** - Python web framework
- **TensorFlow/Keras** - Deep learning for image analysis
- **scikit-learn** - Machine learning for text classification
- **NLTK** - Natural language processing
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization

### **Frontend**
- **HTML5/CSS3** - Modern semantic markup and styling
- **Bootstrap 5** - Responsive component framework
- **JavaScript ES6+** - Interactive functionality
- **CSS Grid/Flexbox** - Advanced layout systems
- **Web Fonts** - Inter font family for typography

### **AI Models**
- **Text Classification**: Logistic Regression with TF-IDF vectorization (98.77% accuracy)
- **Image Classification**: MobileNetV2 transfer learning model
- **URL Analysis**: Pattern-based validation (extensible)

## 🌐 **Live Demo & Deployment**

### **Deploy Your Own Instance** 
Choose your preferred hosting platform:

#### 🚀 **Render.com (Recommended - Free Tier Available)**
1. Fork this repository to your GitHub account
2. Sign up at [render.com](https://render.com)
3. Connect your GitHub account
4. Create a new **Web Service** from your forked repository
5. **Environment**: Python 3
6. **Build Command**: `pip install -r requirements.txt`
7. **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`
8. Click **Create Web Service**
9. Your app will be live at: `https://your-app-name.onrender.com`

#### ⚡ **Railway.app (Fast & Simple)**
1. Visit [railway.app](https://railway.app)
2. Connect your GitHub account
3. Click **Deploy from GitHub repo**
4. Select your forked repository
5. Railway will auto-detect the configuration from `railway.json`
6. Your app will be live in minutes!

#### 🔥 **Heroku (Classic Choice)**
1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Deploy: `git push heroku main`
5. Open: `heroku open`

#### ⚙️ **Vercel (Serverless)**
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel --prod`
3. Follow the prompts
4. Your app will be live instantly!

### **One-Click Deploy Buttons**
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Ohdaradi/fake-news-detector)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/Ohdaradi/fake-news-detector)

## 🚀 **Quick Start**

### **Method 1: Windows Batch File**
```bash
# Double-click to run
start_app.bat
```

### **Method 2: Python Script**
```bash
python run_app.py
```

### **Method 3: Direct Flask**
```bash
python app.py
```

## 🌐 **Direct Access**
- **URL**: http://localhost:5000
- **No Login Required**: Start using immediately
- **Instant Access**: Direct access to all features

## 📊 **System Requirements**
- **Python**: 3.8+ (Tested on 3.10.9)
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 2GB free space
- **Browser**: Chrome, Firefox, Safari, Edge (latest versions)

## 🎯 **How to Use**

### **1. Direct Access**
- Open the application and start using immediately
- No authentication barriers - instant access to all features

### **2. Analyze Content**
- **Text Analysis**: Paste news articles, social media posts, or any text
- **Image Upload**: Upload images for deepfake/manipulation detection  
- **URL Validation**: Enter website URLs for credibility analysis
- **Multi-Modal**: Combine multiple inputs for comprehensive analysis

### **3. View Results**
- Get instant predictions with confidence scores
- See color-coded results with intuitive icons
- View detailed breakdown of each analysis type

### **4. Analytics Dashboard**
- Monitor prediction statistics and trends
- View beautiful charts and visualizations
- Track system usage and accuracy metrics

## 🎨 **Design Highlights**

### **Visual Design**
- **Color Palette**: Modern purple-blue gradients with professional accent colors
- **Typography**: Inter font family for optimal readability
- **Iconography**: Emoji-based icons for universal understanding
- **Spacing**: Consistent 8px grid system for perfect alignment

### **Interactive Elements**
- **Hover Effects**: Subtle animations on buttons and cards
- **Loading States**: Smooth spinners and progress indicators
- **Form Validation**: Real-time input validation with visual feedback
- **Theme Toggle**: Smooth dark/light mode transitions

### **Responsive Breakpoints**
- **Desktop**: 1200px+ (Full featured layout)
- **Tablet**: 768px - 1199px (Optimized columns)
- **Mobile**: <768px (Stacked layout with touch optimization)

## 🔧 **Configuration**

### **Model Files Required**
- `model.pkl` - Trained text classification model
- `vectorizer.pkl` - TF-IDF vectorizer for text preprocessing
- `image_model.h5` - CNN model for image analysis

### **Training Data**
- `Fake.csv` - Fake news dataset
- `True.csv` - Real news dataset
- `data/real_and_fake_face/` - Image training data

## 📈 **Performance**

### **Model Accuracy**
- **Text Classification**: ~94% accuracy on test data
- **Image Analysis**: ~89% accuracy on face detection
- **Processing Speed**: <2 seconds average response time

### **System Performance**
- **Load Time**: <3 seconds on modern hardware
- **Memory Usage**: ~500MB RAM during operation
- **Concurrent Users**: Supports 10+ simultaneous users

## 🛡️ **Security Features**
- **Session Management**: Secure Flask sessions
- **Input Validation**: Comprehensive form validation
- **File Upload Security**: Restricted file types and size limits
- **CSRF Protection**: Built-in Flask security measures

## 🔄 **Updates & Maintenance**

### **v2.0 Enhancements**
- ✅ Complete UI/UX redesign with modern glassmorphism
- ✅ Responsive design for all devices
- ✅ Enhanced dashboard with animated statistics
- ✅ Improved error handling and user feedback
- ✅ Dark/light theme switching
- ✅ Better performance optimizations

### **Upcoming Features**
- 🔄 Real-time collaborative analysis
- 🔄 API endpoints for external integration
- 🔄 Advanced ML model ensemble
- 🔄 Multi-language support
- 🔄 Cloud deployment ready

## 🤝 **Contributing**
This project is designed for educational and research purposes. Contributions welcome for:
- Additional ML models and algorithms
- UI/UX improvements and accessibility
- Performance optimizations
- Security enhancements

## 📄 **License**
Educational use only. Please ensure compliance with data usage policies and AI ethics guidelines.

---

**🔍 RealFake AI** - *Powered by Advanced Machine Learning & Modern Web Technologies*

*"Empowering users with AI-driven truth detection in the digital age"*

## � **Installation & Setup**

### **Quick Start**
```bash
# Clone the repository
git clone https://github.com/Ohdaradi/fake-news-detector.git
cd fake-news-detector

# Install dependencies
pip install flask tensorflow scikit-learn pandas matplotlib pillow

# Run the application
python run_app.py
```

### **Access the Application**
- Open your browser and go to: **http://localhost:5000**
- Start analyzing content immediately - no login required!

---

## 📁 **Project Structure**
```
RealFake/
│
├── static/
│   ├── style.css              # Modern glassmorphism CSS
│   └── uploads/               # Uploaded image storage
│
├── templates/
│   ├── index.html             # Main interface
│   └── dashboard.html         # Analytics dashboard
│
├── app.py                     # Flask backend with AI models
├── run_app.py                 # Enhanced startup script
├── train_model.py             # Text model training
├── train_image_model.py       # Image model training
├── test_model.py              # Model validation
├── model.pkl                  # Trained text classifier
├── vectorizer.pkl             # TF-IDF vectorizer
├── image_model.h5             # CNN image classifier
├── Fake.csv / True.csv        # Training datasets
└── README.md                  # This documentation
```
