import tkinter as tk
import tensorflow as tf
import numpy as np
from tkinter import filedialog
from PIL import Image, ImageTk

# ========== تحميل الموديل ==========
model = tf.keras.models.load_model("FinalFlowerModel.h5")
class_names = ['Tulip', 'Sunflower', 'Orchid', 'Lotus', 'Lilly']

# ========== إعداد النافذة ==========
root = tk.Tk()
root.title("Flower Classifier")
root.geometry("600x700")
root.configure(bg="#fff0f5")

# ========== تحميل صورة الشعار ==========
try:
    flower_icon = Image.open("flower_icon.png")
    flower_icon = flower_icon.resize((60, 60))
    flower_icon_tk = ImageTk.PhotoImage(flower_icon)
except:
    flower_icon_tk = None

# ========== عرض الشعار ==========
if flower_icon_tk:
    icon_label = tk.Label(root, image=flower_icon_tk, bg="#fff0f5")
    icon_label.pack(pady=(15, 5))

# ========== عنوان التطبيق ==========
title_label = tk.Label(
    root,
    text="Welcome to our Flower Classifier!",
    font=("Georgia", 20, "bold"),
    bg="#fff0f5",
    fg="#880e4f"
)
title_label.pack(pady=(0, 15))

# ========== نتيجة التنبؤ ==========
result_label = tk.Label(
    root,
    text="Prediction will appear here.",
    font=("Arial", 14),
    bg="#fff0f5",
    fg="#6a1b9a",
    width=40,
    height=2
)
result_label.pack(pady=1)

# ========== متغيرات ==========
selected_image_path = None
img_frame = None
img_label = None

# ========== دالة اختيار صورة ==========
def select_image():
    global selected_image_path, img_frame, img_label
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")]
    )
    if file_path:
        selected_image_path = file_path
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(img)

        if img_frame is None:
            # إنشاء الإطار والصورة أول مرة فقط
            img_frame = tk.Frame(root, bd=0, bg="#fff0f5", highlightthickness=0)  # شفافية في الإطار
            img_label = tk.Label(img_frame, bg="#fff0f5")  # الخلفية أيضًا شفافة
            img_label.pack()
            # إدراج الإطار فوق زر اختيار الصورة
            img_frame.pack(pady=20, before=select_btn)

        img_label.config(image=img_tk)
        img_label.image = img_tk
        result_label.config(text="Image selected. Ready to predict.")

# ========== دالة التنبؤ ==========
def predict_image():
    if selected_image_path:
        img = tf.keras.preprocessing.image.load_img(selected_image_path, target_size=(150, 150))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        prediction = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction)]

        result_label.config(text=f"Prediction: {predicted_class}")
    else:
        result_label.config(text="Please select an image first.")

# ========== زر اختيار صورة ==========
select_btn = tk.Button(
    root,
    text="Select Image",
    command=select_image,
    font=("Arial", 12),
    bg="#e91e63",
    fg="white",
    width=20,
    height=2,
    bd=0,
    relief="flat",
    activebackground="#f06292",
    activeforeground="white"
)
select_btn.pack(pady=5)

# ========== زر التنبؤ ===
predict_btn = tk.Button(
    root,
    text="Predict",
    command=predict_image,
    font=("Arial", 12),
    bg="#e91e63",
    fg="white",
    width=20,
    height=2,
    bd=0,
    relief="flat",
    activebackground="#f06292",
    activeforeground="white"
)
predict_btn.pack(pady=10)

# ========== تشغيل التطبيق ==========
root.mainloop()
