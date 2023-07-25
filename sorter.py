import os, math
from PIL import Image

import tkinter as tk
from tkinter import filedialog



path = ""

# look for dir
def select_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

# what to do when submit button
def submit_directory():
    selected_directory = directory_entry.get()
    print("Selected Directory:", selected_directory)
    global path
    path = selected_directory + "/"

    #close window
    window.destroy()

window = tk.Tk()
window.title("Directory Locator")
window.eval('tk::PlaceWindow . center')

# Directory Entry
directory_label = tk.Label(window, text="Directory:")
directory_label.pack()

directory_entry = tk.Entry(window, width=40)
directory_entry.pack()

# Directory Locator Button
locator_button = tk.Button(window, text="Select Directory", command=select_directory)
locator_button.pack()

# Submit Button
submit_button = tk.Button(window, text="Submit", command=submit_directory)
submit_button.pack()

window.mainloop()


i = 2


for x in sorted(os.listdir(path)):
    save = x
    if x.endswith('.jpg'):
        if i % 2 != 0:
            os.rename(path + x, path + str(math.floor(i/2)) + " front" + ".jpg")
        else:
            os.rename(path + x, path + str(math.floor(i/2)) + " back" + ".jpg")
        print("Successfully renamed " + save + " to " + str(i) + ".jpg")
        i += 1

os.mkdir(os.path.relpath(path) + ' combined')

for x in range(1, math.floor(len(os.listdir(path))/2) + 1):
    image1 = Image.open(path + str(x) + ' back.jpg')
    image2 = Image.open(path + str(x) + ' front.jpg')

    combined_image = Image.new('RGB', (image1.width + image2.width, image1.height))

    combined_image.paste(image1, (0, 0))

    combined_image.paste(image2, (image1.width, 0))

    combined_image.save(os.getcwd() + '/'  + os.path.relpath(path) + ' combined'  + '/' + str(x) + ' combined' + '.jpg')
