import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("menu")
main_menu = tk.Menu(win)
def func():
    print("hello")
file_menu = tk.Menu(main_menu,tearoff = 0)
file_menu.add_command(label = "save",command = func)
file_menu.add_command(label = "save as",command = func)
file_menu.add_separator()
file_menu.add_command(label = "open",command = func)
edit_menu = tk.Menu(main_menu,tearoff = 0)
edit_menu.add_command(label = "undu",command = func)
edit_menu.add_command(label = "redo",command = func)

# main_menu.add_command(label = "file",command = func)
main_menu.add_cascade(label = "file",menu = file_menu)
main_menu.add_cascade(label = "edit",menu = edit_menu)
win.config(menu = main_menu)
win.mainloop()
