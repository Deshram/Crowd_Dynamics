import tkinter as tk 
import os
r = tk.Tk() 
r.title('Crowd Estimation')
r.geometry('400x600') 

def run():
	os.system('python basemap.py')

button = tk.Button(r, text='Crowd Monitoring', width=25, command=run)
button.place(x=100, y=200)

r.mainloop() 
