from tkinter import *
import tkinter as tk 
import os
from PIL import Image, ImageDraw, ImageTk, ImageFont

r = tk.Tk() 
r.title('Crowd Estimation')
r.geometry('400x600') 

im = Image.open('bg.jpg')
im = im.resize((400,600))
tkimage = ImageTk.PhotoImage(im)
myvar=tk.Label(r,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)

def run():
	os.system('python crmon1.py')

button1 = tk.Button(r,text='Crowd Monitoring', font = ('Bold',10),width = '25',command = run)
button1.place(x=100, y=200)

button2 = tk.Button(r,text='Crowd Prediction', font = ('Bold',10),width = '25',command = run)
button2.place(x=100, y=300)


r.mainloop()