import tkinter as tk
from tcs import printfunction
import os

r = tk.Tk() 
r.title('Crowd Prediction')
r.geometry('800x500') 
p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20 = printfunction()

def run():
	os.system('python heatmap.py')

#p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20 = [0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1]

head = tk.Label(r,text = 'Crowd Prediction',font = ('Arial',20),fg ="Black")
head.pack()
head.place(x=300,y=30)

head2 = tk.Label(r,text = 'Regions 1-20',font = ('Arial',14),fg ="Black")
head2.pack()
head2.place(x=10,y=70)

if p1[len(p1)-1] == 0:
	r1 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r1.pack()
	r1.place(x=30,y=120)
elif p1[len(p1)-1] == 1:
	r1 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r1.pack()
	r1.place(x=30,y=120)
else:
	r1 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r1.pack()
	r1.place(x=30,y=120)

if p2[len(p2)-1] == 0:
	r2 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r2.pack()
	r2.place(x=180,y=120)
elif p2[len(p2)-1] == 1:
	r2 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r2.pack()
	r2.place(x=180,y=120)
else:
	r2 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r2.pack()
	r2.place(x=180,y=120)

if p3[len(p3)-1] == 0:
	r3 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r3.pack()
	r3.place(x=330,y=120)
elif p3[len(p3)-1] == 1:
	r3 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r3.pack()
	r3.place(x=330,y=120)
else:
	r3 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r3.pack()
	r3.place(x=330,y=120)

if p4[len(p4)-1] == 0:
	r4 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r4.pack()
	r4.place(x=480,y=120)
elif p4[len(p4)-1] == 1:
	r4 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r4.pack()
	r4.place(x=480,y=120)
else:
	r4 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r4.pack()
	r4.place(x=480,y=120)

if p5[len(p5)-1] == 0:
	r5 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r5.pack()
	r5.place(x=630,y=120)
elif p5[len(p5)-1] == 1:
	r5 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r5.pack()
	r5.place(x=630,y=120)
else:
	r5 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r5.pack()
	r5.place(x=630,y=120)

if p6[len(p6)-1] == 0:
	r6 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r6.pack()
	r6.place(x=30,y=170)
elif p6[len(p6)-1] == 1:
	r6 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r6.pack()
	r6.place(x=30,y=170)
else:
	r6 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r6.pack()
	r6.place(x=30,y=170)

if p7[len(p7)-1] == 0:
	r7 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r7.pack()
	r7.place(x=180,y=170)
elif p7[len(p7)-1] == 1:
	r7 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r7.pack()
	r7.place(x=180,y=170)
else:
	r7 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r7.pack()
	r7.place(x=180,y=170)

if p8[len(p8)-1] == 0:
	r8 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r8.pack()
	r8.place(x=330,y=170)
elif p8[len(p8)-1] == 1:
	r8 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r8.pack()
	r8.place(x=330,y=170)
else:
	r8 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r8.pack()
	r8.place(x=330,y=170)

if p9[len(p9)-1] == 0:
	r9 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r9.pack()
	r9.place(x=480,y=170)
elif p9[len(p9)-1] == 1:
	r9 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r9.pack()
	r9.place(x=480,y=170)
else:
	r9 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r9.pack()
	r9.place(x=480,y=170)

if p10[len(p10)-1] == 0:
	r10 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r10.pack()
	r10.place(x=630,y=170)
elif p10[len(p10)-1] == 1:
	r10 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r10.pack()
	r10.place(x=630,y=170)
else:
	r10 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r10.pack()
	r10.place(x=630,y=170)

if p11[len(p11)-1] == 0:
	r11 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r11.pack()
	r11.place(x=30,y=220)
elif p11[len(p11)-1] == 1:
	r11 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r11.pack()
	r11.place(x=30,y=220)
else:
	r11 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r11.pack()
	r11.place(x=30,y=220)

if p12[len(p12)-1] == 0:
	r12 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r12.pack()
	r12.place(x=180,y=220)
elif p12[len(p12)-1] == 1:
	r12 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r12.pack()
	r12.place(x=180,y=220)
else:
	r12 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r12.pack()
	r12.place(x=180,y=220)

if p13[len(p13)-1] == 0:
	r13 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r13.pack()
	r13.place(x=330,y=220)
elif p13[len(p13)-1] == 1:
	r13 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r13.pack()
	r13.place(x=330,y=220)
else:
	r13 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r13.pack()
	r13.place(x=330,y=220)

if p14[len(p14)-1]== 0:
	r14 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r14.pack()
	r14.place(x=480,y=220)
elif p14[len(p14)-1] == 1:
	r14 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r14.pack()
	r14.place(x=480,y=220)
else:
	r14 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r14.pack()
	r14.place(x=480,y=220)

if p15[len(p15)-1] == 0:
	r15 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r15.pack()
	r15.place(x=630,y=220)
elif p15[len(p15)-1] == 1:
	r15 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r15.pack()
	r15.place(x=630,y=220)
else:
	r15 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r15.pack()
	r15.place(x=630,y=220)

if p16[len(p16)-1] == 0:
	r16 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r16.pack()
	r16.place(x=30,y=270)
elif p16[len(p16)-1] == 1:
	r16 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r16.pack()
	r16.place(x=30,y=270)
else:
	r16 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r16.pack()
	r16.place(x=30,y=270)

if p17[len(p17)-1] == 0:
	r17 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r17.pack()
	r17.place(x=180,y=270)
elif p17[len(p17)-1] == 1:
	r17 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r17.pack()
	r17.place(x=180,y=270)
else:
	r17 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r17.pack()
	r17.place(x=180,y=270)

if p18[len(p18)-1] == 0:
	r18 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r18.pack()
	r18.place(x=330,y=270)
elif p18[len(p18)-1] == 1:
	r18 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r18.pack()
	r18.place(x=330,y=270)
else:
	r18 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r18.pack()
	r18.place(x=330,y=270)

if p19[len(p19)-1] == 0:
	r19 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r19.pack()
	r19.place(x=480,y=270)
elif p19[len(p19)-1] == 1:
	r19 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r19.pack()
	r19.place(x=480,y=270)
else:
	r19 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r19.pack()
	r19.place(x=480,y=270)

if p20[len(p20)-1] == 0:
	r20 = tk.Label(r,text = 'High',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r20.pack()
	r20.place(x=630,y=270)
elif p20[len(p20)-1] == 1:
	r20 = tk.Label(r,text = 'Medium',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r20.pack()
	r20.place(x=630,y=270)
else:
	r20 = tk.Label(r,text = 'Low',font = ('Arial',10),fg ="Black",width = 10,bg = "white")
	r20.pack()
	r20.place(x=630,y=270)

button = tk.Button(r, text='Virtualize', width=25, command=run)
button.place(x=300, y=450)

r.mainloop() 