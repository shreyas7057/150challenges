from tkinter import *

def add_number():
    num = num_box.get()
    if num.isdigit():
        num_list.insert(END,num)
        num_box.delete(0,END)
        num_box.focus()
    else:
        num_box.delete(0,END)
        num_box.focus()

def clear_list():
    num_list.delete(0,END)
    num_box.focus()


window = Tk()
window.title("Number List")
window.geometry("400x200")

lable1 = Label(text="Enter number: ")
lable1.place(x=20,y=20,width=100,height=25)

num_box = Entry(text=0)
num_box.place(x=120,y=20,width=100,height=25)
num_box.focus()

button1 = Button(text="Add to list",command=add_number)
button1.place(x=250,y=20,width=100,height=25)

num_list = Listbox()
num_list.place(x=120,y=50,width=100,height=100)

button2 = Button(text="Clear List",command=clear_list)
button2.place(x=250,y=50,width=100,height=25)

window.mainloop()