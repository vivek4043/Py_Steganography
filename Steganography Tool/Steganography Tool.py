import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from tkinter import ttk  # Importing ttk for the progress bar
from PIL import Image, ImageOps
import numpy as np

def embed_message(image_path, key, scalar, message, output_path, progress):
    try:
        cover = ImageOps.grayscale(Image.open(image_path))
        cover_array = np.array(cover)  # Convert to NumPy array

        # Append delimiter to the message to mark the end
        message += "|||"
        message_binary = ''.join(format(ord(char), '08b') for char in message)
        message_len = len(message_binary)

        if message_len > cover_array.size:
            raise ValueError("Message is too long to be embedded in this image.")

        # Initialize progress bar
        progress['maximum'] = message_len

        # Embed the message in the image
        for i in range(message_len):
            x, y = divmod(i, cover_array.shape[1])
            cover_array[x, y] = (cover_array[x, y] & ~1) | int(message_binary[i])
            progress['value'] = i + 1
            progress.update()

        new_image = Image.fromarray(cover_array)  # Convert back to PIL Image
        new_image.save(output_path)
        progress['value'] = 0
        messagebox.showinfo("Success", "Message embedded successfully!")
    except Exception as e:
        progress['value'] = 0
        messagebox.showerror("Error", str(e))

def extract_message(image_path, key, progress):
    try:
        stego = ImageOps.grayscale(Image.open(image_path))
        stego_array = np.array(stego)  # Convert to NumPy array

        progress['maximum'] = stego_array.size

        # Extract the message from the image
        message_binary = ''
        for i in range(stego_array.size):
            x, y = divmod(i, stego_array.shape[1])
            message_binary += str(stego_array[x, y] & 1)
            progress['value'] = i + 1
            progress.update()

        # Convert binary message to string
        message_chars = [chr(int(message_binary[i:i+8], 2)) for i in range(0, len(message_binary), 8)]
        extracted_message = ''.join(message_chars)

        # Find the delimiter and cut off everything after it
        delimiter_pos = extracted_message.find("|||")
        if delimiter_pos != -1:
            extracted_message = extracted_message[:delimiter_pos]

        progress['value'] = 0
        extracted_message_label.config(text=extracted_message)  # Update the label with the extracted message
        extracted_message_label.update_idletasks()  # Ensure the label is updated
    except Exception as e:
        progress['value'] = 0
        messagebox.showerror("Error", str(e))

def select_file():
    return filedialog.askopenfilename()

def save_file():
    return filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])

def embed_gui():
    image_path = select_file()
    key = input_key.get()
    scalar = int(input_scalar.get())
    message = input_message.get()
    output_path = save_file()
    embed_message(image_path, key, scalar, message, output_path, progress)

def extract_gui():
    image_path = select_file()
    key = input_key.get()
    extract_message(image_path, key, progress)

root = Tk()
root.title("Image Processing GUI")

Label(root, text="Key:").grid(row=0, column=0)
input_key = Entry(root)
input_key.grid(row=0, column=1)

Label(root, text="Scalar (1-255):").grid(row=1, column=0)
input_scalar = Entry(root)
input_scalar.grid(row=1, column=1)

Label(root, text="Message:").grid(row=2, column=0)
input_message = Entry(root)
input_message.grid(row=2, column=1)

Button(root, text="Embed", command=embed_gui).grid(row=3, column=0)
Button(root, text="Extract", command=extract_gui).grid(row=3, column=1)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.grid(row=4, column=0, columnspan=2)

extracted_message_label = Label(root, text="")
extracted_message_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
