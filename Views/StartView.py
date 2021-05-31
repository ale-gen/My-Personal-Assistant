import tkinter as tk
from PIL import Image, ImageTk


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

    anime = self.after(100, lambda: move_images(self))


def stop_animation(self):
    global anime
    self.after_cancel(anime)


class StartView(tk.Tk):

    def __init__(self):

        tk.Tk.__init__(self)
        self.title("MPA")
        self.geometry("300x300+575+250")
        self.configure(bg="white")
        get_image_list()

        self.gif_label = tk.Button(self, command=self.push_button)
        self.gif_label.pack()
        self.configure_label()
        self.after(100, move_images(self))
        move_images(self)
        self.mainloop()

    def stop(self):
        stop_animation(self)

    def move(self):
        move_images(self)

    def configure_label(self):
        intro_label = tk.Label(
            self,
            text="If you would like to start, press the microphone button. Window disappear, but assistant will run "
                 "in background.",
            bg="white",
            wraplength=200
        )
        intro_label.pack()

    def push_button(self):
        self.after(100, self.destroy())

