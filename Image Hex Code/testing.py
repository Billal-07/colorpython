import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from collections import Counter

class ImageUploaderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Uploader")

        self.image_label = tk.Label(self.master, text="Uploaded Image will be displayed here.")
        self.image_label.pack(pady=10)

        self.color_label = tk.Label(self.master, text="Hex Codes of Colors in Image:")
        self.color_label.pack(pady=5)

        self.upload_button = tk.Button(self.master, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.show_colors_button = tk.Button(self.master, text="Show Colors", command=self.show_all_colors)
        self.show_colors_button.pack(pady=10)

        self.prominent_color_window = None
        self.dominant_color_window = None

    def upload_image(self):
        # Destroy existing color windows
        if self.prominent_color_window:
            self.prominent_color_window.destroy()
        if self.dominant_color_window:
            self.dominant_color_window.destroy()

        file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            # Display the selected image
            image = Image.open(file_path)
            image = image.resize((600, 500))  # Adjust size as needed
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo)
            self.image_label.image = photo

            # Extract hex codes and frequencies
            hex_codes, frequencies = self.get_hex_codes(image)

            # Save hex codes and frequencies to a text file
            self.save_to_file(hex_codes, frequencies)

            # Display information about prominent and dominant colors
            self.show_color_info(hex_codes, frequencies)

    def get_hex_codes(self, image):
        rgb_image = image.convert("RGB")
        width, height = rgb_image.size

        hex_codes = []
        frequencies = Counter()

        for x in range(width):
            for y in range(height):
                r, g, b = rgb_image.getpixel((x, y))
                hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
                hex_codes.append(hex_code)
                frequencies[hex_code] += 1

        return hex_codes, frequencies

    def save_to_file(self, hex_codes, frequencies):
        with open("colors.txt", "w") as file:
            file.write("\n".join(hex_codes))

    def show_color_info(self, hex_codes, frequencies):
        threshold = 100  # Adjust the threshold as needed
        prominent_colors = [color for color, count in frequencies.items() if count > threshold] # Select all prominent colors

        # Group similar colors (shades of white) together
        grouped_colors = self.group_similar_colors(frequencies)

        dominant_colors = [color for color, count in grouped_colors.items() if count > 50]  # Adjust the threshold as needed

        self.prominent_color_window = self.show_colors_window("Prominent Colors", prominent_colors)
        self.dominant_color_window = self.show_colors_window("Dominant Colors", dominant_colors)

        print(prominent_colors)
        print(dominant_colors)

    def group_similar_colors(self, frequencies):
        # Create a mapping to group similar colors
        color_groups = {
            "#ffffff": "#ffffff",  # White
            "#fffffe": "#ffffff",  # Off-white
            "#fefefe": "#ffffff",  # Off-white
            "#fdfdfd": "#ffffff",  # Off-white
            # Add more shades of white as needed
        }

        grouped_colors = Counter()

        for color, count in frequencies.items():
            grouped_color = color_groups.get(color, color)
            grouped_colors[grouped_color] += count

        return grouped_colors

    def show_colors_window(self, title, colors):
        color_window = tk.Toplevel(self.master)
        color_window.title(title)

        canvas = tk.Canvas(color_window)
        scrollbar = tk.Scrollbar(color_window, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        for hex_code in colors:
            color_label = tk.Label(frame, text=hex_code, bg=hex_code, padx=20, pady=10)
            color_label.pack()

        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        return color_window

    def show_all_colors(self):
        color_window = tk.Toplevel(self.master)
        color_window.title("All Colors")

        canvas = tk.Canvas(color_window)
        scrollbar = tk.Scrollbar(color_window, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        with open("colors.txt", "r") as file:
            hex_codes = file.read().splitlines()

        for hex_code in hex_codes:
            color_label = tk.Label(frame, text=hex_code, bg=hex_code, padx=20, pady=10)
            color_label.pack()

        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

if __name__ == "__main__":
    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 800
    window_height = 600
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    app = ImageUploaderApp(root)
    root.mainloop()
