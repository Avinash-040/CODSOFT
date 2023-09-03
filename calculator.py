import tkinter
from tkinter import*

root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="black")

equation=""
def show(value):
    global equation
    equation+=value
    lr.config(text=equation)
def clear():
    global equation
    equation=""
    lr.config(text=equation)
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    lr.config(text=result)

lr=Label(root,width=30,height=2,text="",bg="white",font=("calibri",30))
lr.pack()

Button(root,text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="blue",command=lambda:clear()).place(x=10,y=104)
Button(root,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("%")).place(x=150,y=104)
Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("+")).place(x=290,y=104)
Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("-")).place(x=430,y=104)
Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("9")).place(x=10,y=204)
Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("8")).place(x=150,y=204)
Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("7")).place(x=290,y=204)
Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("/")).place(x=430,y=204)
Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("6")).place(x=10,y=304)
Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("5")).place(x=150,y=304)
Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("4")).place(x=290,y=304)
Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("*")).place(x=430,y=304)
Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("3")).place(x=10,y=404)
Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("2")).place(x=150,y=404)
Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("1")).place(x=290,y=404)
Button(root,text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="white",bg="orange",command=lambda:calculate()).place(x=430,y=404)
Button(root,text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show("0")).place(x=10,y=504)
Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="#202020",command=lambda:show(".")).place(x=290,y=504)



root.mainloop()
