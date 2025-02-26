import streamlit as st 
import tensorflow as tf 
import numpy as np 
from  PIL import Image 

model = tf.keras.models.load_model('cifar10_trained.h5')

classes = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

st.title('CIFAR-10 Image Recognition')
st.write("Upload an image, and the model will predict its class with confidence scores.")

uploaded_file = st.file_uploader("📂 Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).resize((32, 32)) 
    img_array = np.array(image) / 255.0  
    img_array = np.expand_dims(img_array, axis=0)  

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    confidence = predictions[0][predicted_class] * 100

    st.image(uploaded_file, caption=f"Predicted: **{classes[predicted_class]}** ({confidence:.2f}%)", use_column_width=True)

    top_3_indices = np.argsort(predictions[0])[-3:][::-1]  
    top_3_scores = [predictions[0][i] * 100 for i in top_3_indices] 

    st.write("### 🔍 Top-3 Predictions:")
    for i in range(3):
        st.write(f"**{classes[top_3_indices[i]]}**: {top_3_scores[i]:.2f}%")

