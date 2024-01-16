from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox






logs=Tk()
logs.title("Vienādie attēli")

bgimg=ImageTk.PhotoImage(Image.open("77.jpg"))

galvenaIzvelne=Menu(logs) #izveido izvēlni
logs.config(menu=galvenaIzvelne)






def reset(): #spēles reset funkcija
    global count,correctAnswers,answers,answer_dict
    btn0.config(state=NORMAL) #padara pogas aktīvas/izmantojamas
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn10.config(state=NORMAL)
    btn11.config(state=NORMAL)

    btn0['image']='pyimage1'
    btn1['image']='pyimage1'
    btn2['image']='pyimage1'
    btn3['image']='pyimage1'
    btn4['image']='pyimage1'
    btn5['image']='pyimage1'
    btn6['image']='pyimage1'
    btn7['image']='pyimage1'
    btn8['image']='pyimage1'
    btn9['image']='pyimage1'
    btn10['image']='pyimage1'
    btn11['image']='pyimage1'
    random.shuffle(imglist)
    answers=[]
    answer_dict={}
    count=0
    correctAnswers=0
    return 0

def info():
    logs=Toplevel() #informācijas logs
    logs.title("Informācija")
    desc=Label(logs,text="Mērķis: atrast vienādus attēla pārus.")
    desc.grid(row=0,column=0)
    desc=Label(logs,text="Ir doti 2 gājieni atklāt jebkuru bildi, pēc tam bildes aizklājas atpakaļ un atkal ir doti 2 gājieni.")
    desc.grid(row=1,column=0)
    desc=Label(logs,text="Spēle beidzas, kad visi iespējamie attēlu pāri ir atrasti.")
    desc.grid(row=2,column=0)
    desc=Label(logs,text="Vēlu veiksmi :)", fg=("darkgrey"))
    desc.grid(row=3,column=0)



opcijas=Menu(logs,tearoff=False) #uztaisa izvēlni
galvenaIzvelne.add_cascade(label='Opcijas',menu=opcijas)

opcijas.add_command(label='Jauna spēle',command=reset)
opcijas.add_command(label='Iziet',command=logs.quit)


galvenaIzvelne.add_command(label='Par programmu',command=info) #izmanto funkciju info





def click(btn, number):
    global count, correctA,answers,answerd
    if btn["image"]=="pyimage1" and count<2:
        btn["image"]=imglist[number] #pagriež attēlu
        count+=1
        answers.append(number)
        answerd[btn]=imglist[number]
    if len(answers)==2:
        if imglist[answers[0]]==imglist[answers[1]]: #salīdzina attēlus
            for key in answerd:
                key["state"]=DISABLED #padara pogu neaktīvu/neizmantojamu
            correctA+=2
            if correctA==2:
                messagebox.showinfo("uzminēji")
                correctA=0
        else:
            messagebox.showinfo('neuzminēji')
            for key in answerd:
                key["image"]="pyimage1"
        count = 0
        answers=[]
        answerd={}
    return 0



count = 0
correctA = 0
answers=[]
answerd={} #kad piespiests, salīdzināt ar attēliem no saraksta


img1=ImageTk.PhotoImage(Image.open("1.png"))
img2=ImageTk.PhotoImage(Image.open("2.png"))
img3=ImageTk.PhotoImage(Image.open("3.png"))
img4=ImageTk.PhotoImage(Image.open("4.png"))
img5=ImageTk.PhotoImage(Image.open("5.png"))
img6=ImageTk.PhotoImage(Image.open("6.png"))

imglist=[img1, img1, img2, img2, img3, img3, img4, img4, img5, img5, img6, img6]
random.shuffle(imglist) #'samaisa' fotogrāfijas



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


#
#
#
#
#
#

btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=1, column=3)
btn8.grid(row=2, column=0)
btn9.grid(row=2, column=1)
btn10.grid(row=2, column=2)
btn11.grid(row=2, column=3)

logs.mainloop()