from tkinter import *
import random



def ran_num():
	num = random.randint(1,6)
	answer["text"] = num

window = Tk()
window.geometry("500x300")

btn = Button(window,text="click here",command=ran_num)
btn.place(x=10,y=20)

answer = Message(text="")
answer.place(x=50,y=50)

window.mainloop()