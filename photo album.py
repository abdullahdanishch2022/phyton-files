from tkinter import *
from tkinter import messagebox
from PIL import image, imagetk
window = Tk()
window.title('my photo album')
window.geometry('400x420')

title = Label(window, text='my photo album',fg='white', bg='purple', width=40)
title.pack(pady=10)
img_file = image.open('img.jfif')
img_file = img_file.resize((300,180))
photo= imagetk.photoimage(img_file)
pic = Label(window,image=photo)
pic.pack(pady=5)

window.mainloop()