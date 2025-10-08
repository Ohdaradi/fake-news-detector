#!/usr/bin/env python3
"""
Startup script for RealFake Detection System
"""
import os
import sys

def main():
    print("🚀 Starting RealFake Detection System...")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ Error: app.py not found. Please run this script from the project directory.")
        sys.exit(1)
    
    # Check if required model files exist
    required_files = ['model.pkl', 'vectorizer.pkl']
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"⚠️ Warning: Missing model files: {', '.join(missing_files)}")
        print("Please run train_model.py first to create the text models.")
    
    # Check for image model
    if not os.path.exists('image_model.h5'):
        print("⚠️ Warning: image_model.h5 not found. Image prediction will be disabled.")
    
    print("\n📊 System Information:")
    print(f"- Python version: {sys.version}")
    print(f"- Working directory: {os.getcwd()}")
    
    print("\n🎉 No Login Required:")
    print("- Direct access to the application")
    print("- Start analyzing content immediately")
    
    print("\n🌐 Starting Flask application...")
    print("📍 Access the application at: http://localhost:5000")
    print("=" * 50)
    
    # Start the Flask app
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user.")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()