from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox
logs=Tk()
logs.title("Vienādie attēli")

bgimg=ImageTk.PhotoImage(Image.open("77.jpg"))


img1=ImageTk.PhotoImage(Image.open("1.png"))
img2=ImageTk.PhotoImage(Image.open("2.png"))
img3=ImageTk.PhotoImage(Image.open("3.png"))
img4=ImageTk.PhotoImage(Image.open("4.png"))
img5=ImageTk.PhotoImage(Image.open("5.png"))
img6=ImageTk.PhotoImage(Image.open("6.png"))

imglist=[img1, img2, img3, img4, img5, img6, img1, img2, img3, img4, img5, img6]
random.shuffle(imglist)

count = 0
correct = 0
answers=[]
answersD={} #kad piespiests, salīdzināt ar attēliem no saraksta

#
#
#
#
#
#

def click(btn, number):
    global count, correct, answers, answersD
    if btn["image"] == "77.jpg" and count<2:
        btn["image"] == imglist[number]
        count+=1
        answers.append(number)
        answersD[btn]=imglist[number]
    if len(answers)==2:
        if imglist[answers[0]]==imglist[answers[1]]: #salīdzina attēlus, kas saglabāts vārdnīcā ar attēl sarakstu
            for key in answersD:
                 key["state"]=DISABLED
            if correct==2:
                messagebox.showinfo("uzminēji")
    else:
        #messagebox.showinfo("neuzminēji")
        for key in answersD:
            key["image"]="77.jpg"
        count=0
        answers=[]
        answersD={}
    return 0


btn0=Button(width=200, height = 200, image = bgimg, bg=("salmon"), command=lambda:click(btn0, 0))
btn1=Button(width=200, height = 200, image = bgimg, bg=("salmon"), command=lambda:click(btn1, 1))
btn2=Button(width=200, height = 200, image = bgimg, bg=("salmon"), command=lambda:click(btn2, 2))
btn3=Button(width=200, height = 200, image = bgimg, bg=("salmon"), command=lambda:click(btn3, 3))
btn4=Button(width=200, height = 200, image = bgimg, bg=("salmon"), command=lambda:click(btn4, 4))
btn5=Button(width=200, height = 200, image = bgimg, bg=("salmon"), command=lambda:click(btn5, 5))
btn6=Button(width=200, height = 200, image = bgimg, bg=("salmon"), command=lambda:click(btn6, 6))
btn7=Button(width=200, height = 200, image = bgimg, bg=("salmon"), command=lambda:click(btn7, 7))
btn8=Button(width=200, height = 200, image = bgimg, bg=("salmon"), command=lambda:click(btn8, 8))
btn9=Button(width=200, height = 200, image = bgimg, bg=("salmon"), command=lambda:click(btn9, 9))
btn10=Button(width=200, height =200, image = bgimg, bg=("salmon"), command=lambda:click(btn10, 10))
btn11=Button(width=200, height = 200, image = bgimg, bg=("salmon"), command=lambda:click(btn11, 11))



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