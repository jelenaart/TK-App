from tkinter import *
k=0
def klikker(event):
    global k
    k+=1
    nupp.config(text=k)

def klikker_(event):
    global k
    k-=1
    nupp.config(text=k)
def txt_to_lbl(event):
    t=txt.get()
    lbl.configure(text=t)
    txt.delete(0,END)#start=0, stop=viimane

def valimine():
    valik=var.get()
    lbl.configure(text=valik)
    txt.insert(END,valik)

aken=Tk()
aken.title("Akna nimetus")
aken.geometry("800x500")

nupp=Button(aken,text="Mina olen nupp",font="Arial 20",width=20,bg="#FF6347",fg="#000080",relief=RAISED)
nupp.pack()#place(x=280,y=220)#side=LEFT
nupp.bind("<Button-1>",klikker)
nupp.bind("<Button-3>",klikker_)

lbl=Label(aken,text="...",height=3,width=20,font="Arial 20",fg="green",bg="lightblue",relief="solid")#.pack()
lbl.pack()

txt=Entry(aken,width=20,font="Arial 20",fg="blue",bg="lightblue",justify=CENTER)
txt.pack()
txt.bind("<Return>",txt_to_lbl)#Enter

i1=PhotoImage(file="1.png")
i2=PhotoImage(file="2.png")
i3=PhotoImage(file="3.png")


var=StringVar()
var.set("Uks")
r1=Radiobutton(aken,image=i1,variable=var,value="Uks",command=valimine)
r2=Radiobutton(aken,image=i2,variable=var,value="Kaks",command=valimine)
r3=Radiobutton(aken,image=i3,variable=var,value="Kolm",command=valimine)
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)


aken.mainloop()