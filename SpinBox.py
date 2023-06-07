from tkinter import *
import ttkbootstrap as ttk

root=Tk()
def display():
    var1=spn.get()
    var2=spn1.get()
    lbl3.config(text=str(var1) +" :  " +  var2)


lbl1=Label(root,text="Choose QTY ").grid(row=0,column=1)
spn=ttk.Spinbox(root,bootstyle = "success",from_=1,to=100)
spn.grid(row=1,column=1)
spn.set(10)

lbl2=Label(root,text="Choose QTY ").grid(row=2,column=1)

city=["Ahmedabad","Bahrain","Prague","USA","UK"]
spn1=ttk.Spinbox(root,bootstyle= "danger",values=city)
spn1.grid(row=3,column=1)
spn1.set("Ahmedabad")

btn=Button(root,text="Print Data",command=display)
btn.grid(row=4,column=1)

lbl3=ttk.Label(root,text="-",bootstyle="info")
lbl3.grid(row=5,column=1)

root.mainloop()