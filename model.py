import os
import tensorflow_hub as hub # type: ignore
import tensorflow as tf
import numpy as np
import cv2

# Suppress TensorFlow logs (set logging level to show only warnings and errors)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load the pre-trained MobileNet model from TensorFlow Hub
model_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
model = hub.load(model_url)

# Load labels for classification (ImageNet labels)
labels_path = tf.keras.utils.get_file(
    'ImageNetLabels.txt',
    'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt'
)
with open(labels_path) as f:
    labels = f.read().splitlines()

# Function to preprocess the image (resize, normalize)
def preprocess_image(image):
    image = cv2.resize(image, (224, 224))  # MobileNet expects 224x224 images
    image = np.array(image, dtype=np.float32) / 255.0  # Normalize pixel values to [0,1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image
