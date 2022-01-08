from tkinter import *
window=Tk()
window.title("interest calculator")
window.geometry("400x400")

window.configure(bg="lightgreen")

username=Entry(window,text="",bd=2,width=22)
username.place(x=150,y=92)

resultframe=LabelFrame(window,text="result",bg="lightblue",font=("calibri",12))
resultframe.pack(padx=20,pady=20)
resultframe.place(x=20,y=300)
resultlabel=Label(resultframe,text="",bg="lightblue",font=("calibri",12),width=33)
resultlabel.place(x=20,y=20)
resultlabel.pack()

princiapllabel=Label(window,text="enter principal(rupees)",fg="black",bg="lightblue",font=("calibri",12))
principallabel.place(x=20,y=140)
principalentry=Entry(window,text="",bd=2,width=15)
principalentry.place(x=150,y=142)

ratelabel=Label(window,text="enter rate(%)",fg="black",bg="lightblue",font=("calibri",12))
ratelabel.place(x=20,y=185)
rateentry=Entry(window,text="",bd=2,width=15)
rateentry.place(x=150,y=187)

timelabel=Label(window,text="enter time(years)",fg="black",bg="lightblue",font=("calibri",12))
timelabel.place(x=20,y=185)
timeentry=Entry(window,text="",bd=2,width=15)
timeentry.place(x=150,y=187)


def calculatesimpleinterest():
    rate=float(ratentry.get())
    principal=float(principalentry*rateentry*timeentry)/100
    interest=round(interest,1)
    name=username.get()

    resultlabel.destroy()
    msg=""

    

outputmessage=Label(resultframe,text=name+" ,your bmi is "+str(simpleinterest)+" and "+msg,bg="lightblue",font=("calibri",12),width=42)
outputmessage.place(x=20,y=40)
outputmessage.pack()

calculatebutton=Button(window,text="calculate",fg="black",bg="blue",bd=4,command=calculatesimpleinterest)
calculatebutton.place(x=20,y=250)


    

         