import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = tf.keras.models.load_model("D:\Project\Files\mnist_cnn_model.h5")

def predict_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(initialdir="/", title="Select Image File", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")))
    
    if file_path:
        try:
            # Load and preprocess the image
            img = Image.open(file_path).convert('L').resize((28, 28))
            img_array = np.array(img) / 255.0
            img_array = img_array.reshape((1, 28, 28, 1)).astype('float32')
            
            # Predict the image
            prediction = model.predict(img_array)
            predicted_class = np.argmax(prediction)
            
            # Display the result
            messagebox.showinfo("Prediction", f"The predicted class is: {predicted_class}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
# Create the main application window
root = tk.Tk()
root.title("Image Classifier")

# Create a button to select an image
select_button = tk.Button(root, text="Select Image", command=predict_image)
select_button.pack(pady=10)

# Run the application
root.mainloop()
