import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageUploaderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Uploader")

        self.image_label = tk.Label(self.master, text="Uploaded Image will be displayed here.")
        self.image_label.pack(pady=10)

        self.upload_button = tk.Button(self.master, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            # Display the selected image
            image = Image.open(file_path)
            image = image.resize((600, 500))  # Adjust size as needed
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo)
            self.image_label.image = photo

if __name__ == "__main__":
    root = tk.Tk()

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the window size and position it in the center
    window_width = 800
    window_height = 600
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    app = ImageUploaderApp(root)
    root.mainloop()
