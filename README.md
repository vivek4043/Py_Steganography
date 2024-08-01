# Py_Steganography
This Python script creates a graphical user interface (GUI) for embedding and extracting messages in images using the Tkinter library. The script includes functions for selecting files, embedding messages into images, and extracting messages from images. The GUI allows users to interact with these functions easily. 

Key Components:
Libraries Used:
os: For interacting with the operating system.
tkinter: For creating the GUI.
PIL (Pillow): For image processing.
numpy: For numerical operations on image data.
specutils: Placeholder for spectrum-related operations (not used in the current logic).

Functions:
embed_message(image_path, key, scalar, message, output_path): Embeds a message into an image.
Converts the image to grayscale and a NumPy array.
Placeholder logic for embedding the message.
Saves the modified image.
Displays a success message.
extract_message(image_path, key): Extracts a message from an image.
Converts the image to grayscale and a NumPy array.
Placeholder logic for extracting the message.
Updates the GUI with the extracted message.
select_file(): Opens a file dialog to select an image file.
save_file(): Opens a file dialog to save the modified image.
GUI Components:
Labels and Entry widgets for user inputs (key, scalar, message).
Buttons for embedding and extracting messages.
A Label to display the extracted message.
Workflow:
The user selects an image file and provides a key, scalar, and message.
The embed_gui() function calls embed_message() to embed the message into the selected image and save it.
The extract_gui() function calls extract_message() to extract the message from the selected image and display it in the GUI.
Usage:
Embedding a Message:
Enter the key, scalar, and message in the respective fields.
Click the “Embed” button.
Select the image file to embed the message into.
Choose the location to save the modified image.
Extracting a Message:
Enter the key in the respective field.
Click the “Extract” button.
Select the image file to extract the message from.
The extracted message will be displayed in the GUI.
