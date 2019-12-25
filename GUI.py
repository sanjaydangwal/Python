import tkinter as tk
from tkinter import ttk
from csv import DictWriter
win = tk.Tk()
win.title("GUI")
# label
name_label = ttk.Label(win, text = "What is your name : ")
name_label.grid(row = 0,column = 0,sticky = tk.W)

email_label = ttk.Label(win, text = "What is your email : ")
email_label.grid(row = 1 , column = 0, sticky = tk.W)

age_label = ttk.Label(win,text = "What is your age : ")
age_label.grid(row = 2,column = 0,sticky = tk.W)

gender_label = ttk.Label(win,text = "What is your gender : ")
gender_label.grid(row = 3,column = 0)

# entry box

name_var = tk.StringVar()
name_entry = ttk.Entry(win, width = 18 , textvariable = name_var)
name_entry.grid(row = 0 , column = 1)

email_var = tk.StringVar()
email_entry = ttk.Entry(win, width = 18 , textvariable = email_var)
email_entry.grid(row = 1 , column = 1)

age_var = tk.StringVar()
age_entry = ttk.Entry(win, width = 18 , textvariable = age_var)
age_entry.grid(row = 2 , column = 1)

# Combobox

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width = "16", values = ['Male','Female','Other'], textvariable = gender_var,state = 'readonly' )
gender_combobox.current(0)
gender_combobox.grid(row = 3,column = 1)

# radio button 

type_var = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, value = "Student",text = "Student", variable = type_var)
radiobtn1.grid(row = 4 ,column = 0)
 
radiobtn2 = ttk.Radiobutton(win, value = "Teacher",text = "Techer", variable = type_var)
radiobtn2.grid(row = 4 ,column = 1)

# check box

subscribe = tk.IntVar()
subscribe_box = ttk.Checkbutton(win,text = "Subscribe" , variable = subscribe)
subscribe_box.grid(row= 5,columnspan = 2)

def action():
    user_name = name_var.get()
    user_email = email_var.get()
    user_gender = gender_var.get()
    user_type = type_var.get()
    if subscribe.get() == 0:
        user_subscribe = 'no'
    else:
        user_subscribe = 'yes'
    print(user_name)
    print(user_email)
    print(user_gender)
    print(user_type)
    print(user_subscribe)

submit_button = ttk.Button(win, text = "submit", command = action)
submit_button.grid(row = 6, columnspan = 2)

name_entry.focus()
win.mainloop()