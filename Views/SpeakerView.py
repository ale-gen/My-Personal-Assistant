import tkinter as tk
from PIL import ImageTk, Image
import threading


sub_gif = []
count = 0
anime = None


def get_image_list():
    global sub_gif
    file = "../Main/speaker.gif"
    info = Image.open(file)
    frames = info.n_frames
    sub_gif = [tk.PhotoImage(file=file, format=f'gif -index {i}').subsample(4, 4) for i in range(frames)]


def move_images(self):

    global count
    global anime
    global sub_gif
    gif = sub_gif[count]
    self.gif_label.configure(image=gif)

    count += 1
    if count == len(sub_gif) - 1:
        count = 0

    anime = self.window.after(100, lambda: move_images(self))


def stop_animation(self):
    global anime
    self.after_cancel(anime)


class SpeakerView(object):
    def __init__(self, assistant):
        self.assistant = assistant
        self.window = tk.Tk()
        self.window.title("MPA")
        self.window.geometry("+300+150")
        self.window.configure(bg="white")
        self.images_titles = ["Meal", "Alarm", "Weather", "Google", "Maps", "Time", "Translator", "Wikipedia", "YouTube"]
        self.images = self.upload_images()
        self.gif_label = None
        self.configure_layout()
        threading.Thread(target=self.menu).start()
        self.window.mainloop()

    def menu(self):
        self.assistant.respond("I can: "
                               "- search recipe and make a shopping list for you, "
                               "- set alarm, "
                               "- search something in wikipedia and google, "
                               "- open YouTube and search a video, "
                               "- check weather, "
                               "- translate sentences, "
                               "- show maps, "
                               "- and check hour.")

    def upload_images(self):
        photos = []
        for i in range(0, len(self.images_titles)):
            image = Image.open(f"../Views/images/{self.images_titles[i]}.png")
            image = image.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            photos.append(photo)
        return photos

    def configure_layout(self):
        columns_number = 3
        rows_number = 3
        for row in range(rows_number):
            self.window.columnconfigure(row, weight=1, minsize=75)
            self.window.rowconfigure(row, weight=1, minsize=50)

            for column in range(0, columns_number):
                index = row * columns_number + column
                frame = tk.Frame(
                    master=self.window,
                    relief=tk.RAISED,
                    borderwidth=0,
                    bg="white"
                )
                frame.grid(row=row, column=column, padx=5, pady=5)

                image_label = tk.Label(
                    frame,
                    image=self.images[index],
                    bg="white",
                    fg="black",
                )
                image_label.pack()
                label = tk.Label(
                    master=frame,
                    text=f"{self.images_titles[index]}",
                    bg="white"
                )
                label.pack(padx=5, pady=5)

        get_image_list()
        self.window.columnconfigure(1, weight=1, minsize=150)
        frame = tk.Frame(
            master=self.window,
            borderwidth=0,
            bg="white"
        )
        frame.grid(row=1, column=4, padx=5, pady=5)
        self.gif_label = tk.Label(
            frame,
            bg="white"
        )
        self.gif_label.pack()
        move_images(self)

    def close_window(self):
        answer = ""
        while answer == "":
            answer = self.assistant.talk()
            if answer != "close":
                answer = ""
        self.window.destroy()
