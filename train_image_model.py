# train_image_model.py - Image Classification Model Training
print("🖼️ Starting image model training...")
try:
    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    from tensorflow.keras.applications import MobileNetV2
    from tensorflow.keras.models import Model
    from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
    from tensorflow.keras.optimizers import Adam
    print("✅ TensorFlow imports successful")
except ImportError as e:
    print(f"❌ Error importing TensorFlow: {e}")
    exit(1)

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_data = datagen.flow_from_directory(
    "data/real_and_fake_face",
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

val_data = datagen.flow_from_directory(
    "data/real_and_fake_face",
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224, 224, 3))
x = GlobalAveragePooling2D()(base_model.output)
x = Dense(1, activation='sigmoid')(x)
model = Model(inputs=base_model.input, outputs=x)

for layer in base_model.layers:
    layer.trainable = False

print("🔧 Compiling model...")
model.compile(optimizer=Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])

print("🚀 Starting training...")
history = model.fit(train_data, validation_data=val_data, epochs=5, verbose=1)

print("💾 Saving model...")
try:
    model.save("image_model.h5")
    print("✅ Image classification model saved successfully!")
except Exception as e:
    print(f"❌ Error saving model: {e}")
