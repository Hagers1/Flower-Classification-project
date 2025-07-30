## 🌸 Flower Classification Project

This project is a deep learning-based flower classification system that recognizes images of flowers and predicts their correct category.

## 🧠 Model Overview

We trained a Convolutional Neural Network (CNN) model to classify images into *5 flower categories*:

- 🌺 *Lily*
- 🌸 *Lotus*
- 🌼 *Orchid*
- 🌻 *Sunflower*
- 🌷 *Tulip*

The model was trained on a custom dataset and saved as a .h5 file (Keras model format).

## 🖼️ Sample Images

You can test the model using sample images located in the sample_test_images/ folder.  
Each subfolder inside represents one of the flower categories listed above.

## 📁 Project Structure

Flower-Classification-project/
├── Flower-Classification.ipynb     # Main notebook for training and evaluation (runs on Google Colab).
├── flowers_ui.py                   # Python script for the GUI script built using Tkinter.
├── sample_test_images/            # Contains test images organized in subfolders by category.
├── README.md                      # Full project description, usage guide, and model link.
## 📥 Trained Model File (model.h5)

Due to GitHub's file size limitations, the trained model file is not uploaded here.

👉 Download the trained model from this link:  
[ Download model.h5](https://drive.google.com/drive/folders/17saIZwLaDdLKU2ZJgLp5qn80Ne6Dl6di?usp=drive_link)

🟡 *Important:*  
1. Place the downloaded model.h5 file *directly* in the root directory of the project or Colab environment.  
   Do NOT place it inside any subfolder.
2. Make sure Python and the required libraries (tensorflow, pillow, numpy) are installed.


## 🚀 How to Run the Project

### ▶️ On Google Colab

1. Open Flower-Classification.ipynb in Google Colab.
2. Upload the model.h5 file to the root directory of your Colab environment.
3. Run all cells step-by-step.
4. Upload an image from the sample_test_images folder.

### 🖥️ Locally with GUI (Tkinter)

1. Make sure you have Python installed.
2. Install required libraries (only once):
   ```bash
   pip install tensorflow pillow numpy

3. Download the model.h5 file and place it in the same folder as flowers_ui.py.

4. 4. Run the GUI script using:
   ```bash
   python flowers_ui.py

5. A window will open where you can upload an image and view the prediction result.

[GUI Screenshot] (https://github.com/Hagers1/Flower-Classification-project/blob/main/Screenshot.jpeg?raw=true)   
