#activity: my profile card

#import tinkter and open the window
from tkinter import*

window=Tk()
window.title('my profile')
window.geometry('400x300')


title = Label(window,text='my profile card',Fg='white',Bg='purple',width=40)
title.grid(row=0,collum=0,columnspan=2,padx=10,pady=10)

name_label= Label(window,text='name',fg='black',bg='white')
name_label.grid(row=1,column=0,padx=10,pady=5)

name_entry= Label(window,fg='blue',bg='lightyellow',width=25)
name_entry.grid(row=1,column=1,padx=10,pady=5)

