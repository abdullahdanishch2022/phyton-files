from tkinter import*
from tkinter import messagebox
from PIL import image, imageTk

root = Tk()
root.title('denomination counter')
root.configure(bg='light blue')
root.geometry('650x400')

upload = image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = imageTk.photoimage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root, text= "hey user!welcome to denomination counter application", bg= 'light blue')
label.place(relex=0.5,y=340, anchor=CENTER)


def msg():
    msgbox = messagebox.showinfo("albert", "do you want to calculate the denomination count")
    if MsgBox == 'ok':
        topwin()
        