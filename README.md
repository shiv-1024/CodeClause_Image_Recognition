# 📌 CIFAR-10 Image Recognition using Streamlit

## 📝 Overview

This is a simple **CIFAR-10 Image Recognition** web app built using **Streamlit** and a pre-trained **TensorFlow/Keras** model. The app allows users to upload an image, and it predicts the class (e.g., cat, dog, airplane) along with confidence scores.

---

## 🚀 Features

- 📂 Upload an image (JPG, PNG, JPEG)
- 🔍 Predict the class of the image
- 📊 Show **confidence scores** and **top-3 predictions**
- 🖼️ Display the uploaded image with results

---

## 📦 Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/cifar10-streamlit-app.git
cd cifar10-streamlit-app
```

### 2️⃣ Install Dependencies

Make sure you have **Python 3.8+** installed.

```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```sh
streamlit run app.py
```

---

## 📁 Project Structure

```
📂 cifar10-streamlit-app/
│-- 📄 app.py               # Streamlit App
│-- 📄 main.py              # Python_file
│-- 📄 main.ipynb           # Jupyter_File
│-- 📄 cifar_trained.h5     # Pre-trained CIFAR-10 Model
│-- 📄 requirements.txt     # Python dependencies
│-- 📄 README.md            # Project Documentation
```

---

## 🏗️ How It Works

1. The user uploads an image.
2. The image is resized to **32x32** (CIFAR-10 input size).
3. The image is normalized (pixel values between **0 and 1**).
4. The trained **CNN model** predicts the image class.
5. The app displays:
   - The **predicted class** (e.g., "dog").
   - The **confidence score** (e.g., "85.3%").
   - The **top-3 predictions** with probabilities.

---

## 🔬 Model Details

- The model is a **Convolutional Neural Network (CNN)** trained on the **CIFAR-10 dataset**.
- It recognizes **10 object classes**: `airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck`.

---

## 🔥 Future Improvements

- ✅ Improve accuracy with **transfer learning**
- ✅ Add **Grad-CAM visualization** to understand model decisions
- ✅ Deploy to **Streamlit Cloud or Hugging Face Spaces**

---


## 💬 Need Help?

If you have any questions or issues, feel free to reach out!

📧 Email: shivsivarajadurai1024@proton.me
🐙 GitHub: https://github.com/shiv-1024

