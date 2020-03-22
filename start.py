from tkinter import *
import tkinter as tk 
import os
from PIL import Image, ImageDraw, ImageTk, ImageFont

r = tk.Tk() 
r.title('Crowd Estimation')
r.geometry('400x600') 
r.configure(background='white')
im = Image.open('bg2.PNG')
im = im.resize((400,600))
tkimage = ImageTk.PhotoImage(im)
myvar=tk.Label(r,image = tkimage)
myvar.pack(side = "top",fill = "both",expand = "yes")
myvar.place(x=0, y=0)

def run():
	os.system('python tcs.py')

button1 = tk.Button(r,highlightbackground='black',bg = 'grey',bd = '5',text='Crowd Monitoring', font = ("Allegro", 12, "bold"),width = '25',command = run)
button1.place(x=75, y=200)

button2 = tk.Button(r,text='Crowd Prediction',bg = 'grey',bd = '5', font = ("Allegro", 12, "bold"),width = '25')
button2.place(x=75, y=300)


r.mainloop()