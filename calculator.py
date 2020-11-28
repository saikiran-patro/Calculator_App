from tkinter import *

#intializing window
root=Tk()
root.title("Prince Calculator    V1.0")

###creating widgets
#creating input

i=Entry(root,width=50,borderwidth=5,bg="white")
i.grid(row=0,column=0,columnspan=3)
j=0
def on_click(num):
    global j
    i.insert(j,num)
    j+=1

def clear():
    global j
    i.delete(0,END)
    j=0

##check operations
check_add=0
check_sub=0
check_mul=0
check_div=0

n=0

def add():
    global number1
    global check_add,check_sub,check_mul,check_div
    if i.get()!='':
        number1=i.get()
    i.delete(0,END)
    check_add+=1
    check_sub=0
    check_mul=0
    check_div=0
    
def sub():
    global number1
    global check_sub,check_add,check_mul,check_div
    if i.get()!='':
        number1=i.get()
    i.delete(0,END)
    check_sub+=1
    check_add=check_mul=check_div=0
    
    
def mul():
    global number1
    global check_mul,check_sub,check_add,check_div
    if i.get()!='':
        number1=i.get()
    i.delete(0,END)
    check_mul+=1
    check_add=check_sub=check_div=0
def div():
    global number1
    global check_div,check_add,check_mul,check_sub
    if i.get()!='':
        number1=i.get()
    i.delete(0,END)
    check_div+=1
    check_mul=check_sub=check_add=0
    
total=0    

def equal():
    number2=i.get()
    i.delete(0,END)
    
    global check_add,check_sub,check_mul,check_div,total
    if check_add==1:
        total=int(number1)+int(number2)
        check_add=0
    elif check_sub==1:
        total=int(number1)-int(number2)
        check_sub=0
    elif check_mul==1:
        total=int(number1)*int(number2)
        check_mul=0
    elif check_div==1:
        try:
            total=int(int(number1)/int(number2))
        except:
            pass
        finally:
            check_div=0
        
    i.insert(1,total)
    
        
button_1=Button(root,text="1",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:on_click(1))
button_2=Button(root,text="2",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:on_click(2))
button_3=Button(root,text="3",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:on_click(3))

button_4=Button(root,text="4",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:on_click(4))
button_5=Button(root,text="5",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:on_click(5))
button_6=Button(root,text="6",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:on_click(6))

button_7=Button(root,text="7",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:on_click(7))
button_8=Button(root,text="8",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:on_click(8))
button_9=Button(root,text="9",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:on_click(9))

button_0=Button(root,text="0",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:on_click(0))

#operation buttons
button_plus=Button(root,text="+",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:add())
button_minus=Button(root,text="-",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:sub())
button_multiply=Button(root,text="*",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:mul())
button_divide=Button(root,text="/",padx=40,pady=15,bg="#eeeeee",fg="#120078",command=lambda:div())

button_clear=Button(root,text="clear",padx=30,pady=15,bg="#93abd3",fg="black",command=lambda:clear())
button_equal=Button(root,text="=",padx=40,pady=75,bg="#222831",fg="#93abd3",command=lambda:equal())

#shoving it onto the screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
##operation buttons
button_plus.grid(row=5,column=0)
button_minus.grid(row=5,column=1)
button_multiply.grid(row=6,column=0)
button_divide.grid(row=6,column=1)


button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=2,rowspan=3)
