from tkinter import *
from PIL import ImageTk, Image
logs=Tk()
logs.title("Vienādie attēli")

bgimg=ImageTk.PhotoImage(Image.open("77.jpg"))


img1=ImageTk.PhotoImage(Image.open("1.png"))
img2=ImageTk.PhotoImage(Image.open("2.png"))
img3=ImageTk.PhotoImage(Image.open("3.png"))
img4=ImageTk.PhotoImage(Image.open("4.png"))
img5=ImageTk.PhotoImage(Image.open("5.png"))
img6=ImageTk.PhotoImage(Image.open("6.png"))



btn0=Button(width=200, height = 200, image = bgimg, bg=("salmon"))
btn1=Button(width=200, height = 200, image = bgimg, bg=("salmon"))
btn2=Button(width=200, height = 200, image = bgimg, bg=("salmon"))
btn3=Button(width=200, height = 200, image = bgimg, bg=("salmon"))
btn4=Button(width=200, height = 200, image = bgimg, bg=("salmon"))
btn5=Button(width=200, height = 200, image = bgimg, bg=("salmon"))
btn6=Button(width=200, height = 200, image = bgimg, bg=("salmon"))
btn7=Button(width=200, height = 200, image = bgimg, bg=("salmon"))
btn8=Button(width=200, height = 200, image = bgimg, bg=("salmon"))
btn9=Button(width=200, height = 200, image = bgimg, bg=("salmon"))
btn10=Button(width=200, height =200, image = bgimg, bg=("salmon"))
btn11=Button(width=200, height = 200, image = bgimg, bg=("salmon"))



btn0.grid(row=1, column=1)
btn1.grid(row=1, column=2)
btn2.grid(row=1, column=3)
btn3.grid(row=1, column=4)
btn4.grid(row=2, column=1)
btn5.grid(row=2, column=2)
btn6.grid(row=2, column=3)
btn7.grid(row=2, column=4)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)
btn10.grid(row=3, column=3)
btn11.grid(row=3, column=4)

logs.mainloop()