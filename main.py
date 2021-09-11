from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width= 25)

#defining respective funtions for functions

def numberclick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        sum = int(f_num)+int(second_number)
        e.insert(0, sum)

    if math == "subtraction":
        difference = int(f_num) - int(second_number)
        e.insert(0, difference)

    if math == "multiplication":
        e.insert(0, int(f_num) * int(second_number))

    if math == "division":
        e.insert(0, int(f_num) / int(second_number))



def button_clear():
    e.delete(0, END)


#defining number buttons
number1 = Button(root, text="1", padx=10, pady=10, command=lambda: numberclick(1))
number2 = Button(root, text="2", padx=10, pady=10, command=lambda: numberclick(2))
number3 = Button(root, text="3", padx=10, pady=10, command=lambda: numberclick(3))
number4 = Button(root, text="4", padx=10, pady=10, command=lambda: numberclick(4))
number5 = Button(root, text="5", padx=10, pady=10, command=lambda: numberclick(5))
number6 = Button(root, text="6", padx=10, pady=10, command=lambda: numberclick(6))
number7 = Button(root, text="7", padx=10, pady=10, command=lambda: numberclick(7))
number8 = Button(root, text="8", padx=10, pady=10, command=lambda: numberclick(8))
number9 = Button(root, text="9", padx=10, pady=10, command=lambda: numberclick(9))

#defining operation buttons
button_ac = Button(root, text="AC", padx=30, pady=10, command=button_clear)
number0 = Button(root, text="0", padx=10, pady=10, command=lambda: numberclick(0))

button_add = Button(root, text="+", padx=10, pady=10, command= button_add)
button_sub = Button(root, text="-", padx=10, pady=10, command= button_sub)
button_mul = Button(root, text="*", padx=10, pady=10, command= button_mul)
button_div = Button(root, text="/", padx=10, pady=10, command= button_div)
button_equal = Button(root, text="=", padx=10, pady=10, command= button_equal)

#positioning the buttons
e.grid(row=0,column=0, columnspan=4)

number1.grid(row=3, column=0)
number2.grid(row=3, column=1)
number3.grid(row=3, column=2)

number4.grid(row=2, column=0)
number5.grid(row=2, column=1)
number6.grid(row=2, column=2)

number7.grid(row=1, column=0)
number8.grid(row=1, column=1)
number9.grid(row=1, column=2)

number0.grid(row=4, column=0)
button_ac.grid(row=4, column=1, columnspan=2)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_equal.grid(row=5, column=0)

root.mainloop()
