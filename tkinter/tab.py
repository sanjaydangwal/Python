import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Game")
nb = ttk.Notebook(win)
page1 = tk.Frame(nb)
page2 = tk.Frame(nb)
nb.add(page1,text = "Standard")
nb.add(page2,text = "scientific")
nb.pack(expand = True , fill = "both")
label1 = ttk.Label(page1,text = "this is label")
label1.config(background = "Blue")
label1.grid(row = 0 ,column = 0)
win.mainloop()