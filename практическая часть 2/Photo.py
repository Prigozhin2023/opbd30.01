from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor")

        
        self.image_label = Label(self.root)
        self.image_label.pack(pady=10)

        Button(self.root, text="Загрузить изображение", command=self.load_image).pack(side=LEFT, padx=10)
        Button(self.root, text="Изменить размер", command=self.resize_image).pack(side=LEFT, padx=10)
        Button(self.root, text="Повернуть", command=self.rotate_image).pack(side=LEFT, padx=10)

        self.image = None
        self.tk_image = None

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.tk_image)

    def resize_image(self):
        if self.image:
            width, height = self.image.size
            new_width = int(width * 0.5)
            new_height = int(height * 0.5)
            resized_image = self.image.resize((new_width, new_height))
            self.tk_image = ImageTk.PhotoImage(resized_image)
            self.image_label.config(image=self.tk_image)

    def rotate_image(self):
        if self.image:
            rotated_image = self.image.rotate(90)
            self.tk_image = ImageTk.PhotoImage(rotated_image)
            self.image_label.config(image=self.tk_image)

if __name__ == "__main__":
    root = Tk()
    app = ImageEditorApp(root)
    root.mainloop()