"""import tkinter as tk
from PIL import Image

window = tk.Tk()
window.geometry("200x300+1300+0")
window.title("MPA")
window.configure(bg="white")
file = 'speaker.gif'

info = Image.open(file)
frames = info.n_frames
sub_gif = [tk.PhotoImage(file=file, format=f'gif -index {i}').subsample(5, 5) for i in range(frames)]
count = 0
anim = None

def animation(count):
    #global anim
    gif = sub_gif[count]
    gif_label.configure(image=gif)

    count += 1
    if count == frames:
        count = 0

    anim = window.after(100, lambda: animation(count))

def stop_animation():
    #global anim
    window.after_cancel(anim)

gif_label = tk.Label(window, image="")
gif_label.pack()

start = tk.Button(window, text='start', command=lambda: animation(count))
start.pack()

stop = tk.Button(window, text='stop', command=stop_animation)
stop.pack()


window.mainloop()"""

import tkinter as tk
import os
from PIL import Image, ImageTk

sub_gif = []
count = 0
anime = None
images = ["recipes", "alarm", "forecast", "google", "maps", "time", "translator", "wikipedia", "youtube"]


def get_image_list():
    global sub_gif
    file = "../Main/speaker.gif"
    info = Image.open(file)
    frames = info.n_frames
    sub_gif = [tk.PhotoImage(file=file, format=f'gif -index {i}').subsample(5, 5) for i in range(frames)]


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


class SpeakerView(tk.Tk):

    def __init__(self):

        tk.Tk.__init__(self)
        self.title("MPA")
        self.geometry("200x200+1300+0")
        self.configure(bg="white")
        get_image_list()

        self.gif_label = tk.Label(self)
        self.gif_label.pack()
        self.after(100, move_images(self))
        move_images(self)
        self.mainloop()

    def stop(self):
        stop_animation(self)

    def move(self):
        move_images(self)