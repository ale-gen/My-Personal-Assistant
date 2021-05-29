import tkinter as tk
from PIL import ImageTk, Image


class Recipe_Images_View(object):
    def __init__(self, images, images_titles):
        self.chosen_image = None
        self.images = images
        self.images_titles = images_titles
        self.images_number = len(images)
        self.window = tk.Tk()
        self.window.title("Founded recipes")
        self.photos = self.configure_photos()
        self.configure_layout()
        self.window.mainloop()

    def configure_photos(self):
        photos = []
        for i in range(0, self.images_number):
            image = Image.open(f"{self.images_titles[i]}.jpg")
            image = image.resize((300, 170), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            photos.append(photo)
        return photos

    def push_button(self, chosen_image):
        self.chosen_image = chosen_image
        self.window.after(100, self.close_window())

    def configure_layout(self):
        columns_number = 4
        rows_number = 3
        for row in range(rows_number):
            self.window.columnconfigure(row, weight=1, minsize=75)
            self.window.rowconfigure(row, weight=1, minsize=50)

            for column in range(0, columns_number):
                index = row * columns_number + column
                if index < self.images_number:
                    frame = tk.Frame(
                        master=self.window,
                        relief=tk.RAISED,
                        borderwidth=1
                    )
                    frame.grid(row=row, column=column, padx=5, pady=5)

                    button = tk.Button(
                        frame,
                        image=self.photos[index],
                        bg="white",
                        fg="black",
                        command=lambda x=index: self.push_button(x)
                    )
                    button.pack()
                    label = tk.Label(master=frame, text=f"{self.images_titles[index] }")
                    label.pack(padx=5, pady=5)

    def get_chosen_image(self):
        return self.chosen_image

    def close_window(self):
        self.window.destroy()