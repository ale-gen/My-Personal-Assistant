from tkinter import *
import time
import random

window_width = 700
window_height = 400
window = Tk()
window.title("MPA")
canvas = Canvas(window, width=window_width, height=window_height, bg="black")
canvas.pack()
single_sound_image = PhotoImage(file='sound.png').subsample(10, 10)

image_width = single_sound_image.width()
image_height = single_sound_image.height()
window_vertical_center = (window_height - image_height) / 2
image_coordinates = []
i = 0
while i < window_width:
    image = canvas.create_image(i, window_vertical_center, image=single_sound_image, anchor=NW)
    image_coordinates.append(i)
    i += image_width + 5

columns_number = len(image_coordinates)

image_column = random.randint(0, columns_number)
images = []


def draw_line_up(column, max_height):
    j = window_vertical_center
    j += 5
    if 0 <= column < columns_number:
        while j >= max_height:
            image = canvas.create_image(image_coordinates[column], j - image_height,
                                        image=single_sound_image, anchor=NW)
            images.append((image, column))
            window.update()
            time.sleep(0.00001)
            j -= 10
            j += image_height


def draw_line_down(column, min_height):
    j = window_vertical_center
    j += 5
    if 0 <= column < columns_number:
        while j <= min_height:
            image = canvas.create_image(image_coordinates[column], j + image_height,
                                        image=single_sound_image, anchor=NW)
            images.append((image, column))
            window.update()
            time.sleep(0.00001)
            j += 10
            j -= image_height


def remove_line(column):
    print(images)
    for photo in images:
        print(photo)
        if photo[1] == column:
            canvas.delete(photo[1])
            images.remove(photo)


"""            
for i in range(0, 15):
    j = window_vertical_center
    j += 5
    if 0 <= image_column + i <= columns_number:
        while j > (window_height / 3) + i * image_height:
            image = canvas.create_image(image_coordinates[image_column + i], j - image_height,
                                        image=single_sound_image, anchor=NW)
            images.append(image)
            j -= 10
            j += image_height
    j = window_vertical_center
    j += 5
    if 0 <= image_column - i <= columns_number:
        while j > (window_height / 3) + i * image_height:
            image = canvas.create_image(image_coordinates[image_column - i], j - image_height,
                                        image=single_sound_image, anchor=NW)
            images.append(image)
            window.update()
            time.sleep(0.001)
            j -= 10
            j += image_height

    j = window_vertical_center
    j += 5
    if 0 <= image_column + i <= columns_number:
        while j < (2 * window_height / 3) - i * image_height:
            image = canvas.create_image(image_coordinates[image_column + i], j + image_height,
                                        image=single_sound_image, anchor=NW)
            images.append(image)
            j += 10
            j -= image_height
    j = window_vertical_center
    j += 5
    if 0 <= image_column - i <= columns_number:
        while j < (2 * window_height / 3) - i * image_height:
            image = canvas.create_image(image_coordinates[image_column - i], j + image_height,
                                        image=single_sound_image, anchor=NW)
            images.append(image)
            window.update()
            time.sleep(0.001)
            j += 10
            j -= image_height"""
for i in range(0, 10):
    omit = False
    image_column = random.randint(0, columns_number)
    if len(images) > 0:
        for photo in images:
            if abs(photo[1] - image_column) <= 5:
                omit = True
            else:
                omit = False
    if not omit:
        for x in range(0, 10):
            if 0 <= image_column + x <= columns_number:
                draw_line_up(image_column + x, window_height / 3 + x * image_height)
                draw_line_down(image_column + x, 2 * window_height / 3 - x * image_height)
                if 0 <= image_column - x <= columns_number:
                    remove_line(image_column - x)
            if 0 <= image_column - x <= columns_number:
                draw_line_up(image_column - x, window_height / 3 + x * image_height)
                draw_line_down(image_column - x, 2 * window_height / 3 - x * image_height)
                if 0 <= image_column + x <= columns_number:
                    remove_line(image_column + x)
window.mainloop()

"""from tkinter import *
import time
import random

window_width = 700
window_height = 400
window = Tk()
window.title("MPA")
canvas = Canvas(window, width=window_width, height=window_height, bg="black")
canvas.pack()
single_sound_image = PhotoImage(file='sound.png').subsample(10, 10)

image_width = single_sound_image.width()
image_height = single_sound_image.height()
window_vertical_center = (window_height - image_height) / 2
image_coordinates = []
i = 0
while i < window_width:
    image = canvas.create_image(i, window_vertical_center, image=single_sound_image, anchor=NW)
    image_coordinates.append(i)
    i += image_width + 5

columns_number = len(image_coordinates)

image_column = random.randint(0, columns_number)
print(image_column)
print(columns_number)
images = []

for i in range(0, 15):
    j = window_vertical_center
    j += 5
    if 0 <= image_column + i <= columns_number:
        while j > (window_height / 3) + i * image_height:
            image = canvas.create_image(image_coordinates[image_column + i], j - image_height,
                                        image=single_sound_image, anchor=NW)
            images.append(image)
            j -= 10
            j += image_height
    j = window_vertical_center
    j += 5
    if 0 <= image_column - i <= columns_number:
        while j > (window_height / 3) + i * image_height:
            image = canvas.create_image(image_coordinates[image_column - i], j - image_height,
                                        image=single_sound_image, anchor=NW)
            images.append(image)
            window.update()
            time.sleep(0.001)
            j -= 10
            j += image_height

    j = window_vertical_center
    j += 5
    if 0 <= image_column + i <= columns_number:
        while j < (2 * window_height / 3) - i * image_height:
            image = canvas.create_image(image_coordinates[image_column + i], j + image_height,
                                        image=single_sound_image, anchor=NW)
            images.append(image)
            j += 10
            j -= image_height
    j = window_vertical_center
    j += 5
    if 0 <= image_column - i <= columns_number:
        while j < (2 * window_height / 3) - i * image_height:
            image = canvas.create_image(image_coordinates[image_column - i], j + image_height,
                                        image=single_sound_image, anchor=NW)
            images.append(image)
            window.update()
            time.sleep(0.001)
            j += 10
            j -= image_height

window.mainloop()
"""