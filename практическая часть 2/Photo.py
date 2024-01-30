import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Image Editor")

        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.TOP, pady=10)

        
        self.load_button = tk.Button(self.button_frame, text="Load Image", command=self.load_image)
        self.load_button.pack(side=tk.LEFT, padx=5)

        
        self.resize_button = tk.Button(self.button_frame, text="Resize Image", command=self.resize_image)
        self.resize_button.pack(side=tk.LEFT, padx=5)

        
        self.rotate_button = tk.Button(self.button_frame, text="Rotate Image", command=self.rotate_image)
        self.rotate_button.pack(side=tk.LEFT, padx=5)

       
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(side=tk.TOP, pady=10)

        
        self.image = None
        self.tk_image = None
        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.image_label.configure(image=self.tk_image)

    def resize_image(self):
        if self.image:
            new_size = (200, 200)  
            resized_image = self.image.resize(new_size, Image.ANTIALIAS)
            self.tk_image = ImageTk.PhotoImage(resized_image)
            self.image_label.configure(image=self.tk_image)

    def rotate_image(self):
        if self.image:
            rotated_image = self.image.rotate(90)  
            self.tk_image = ImageTk.PhotoImage(rotated_image)
            self.image_label.configure(image=self.tk_image)

if __name__ == "Хлеб":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()