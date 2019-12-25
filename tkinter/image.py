import tkinter as tk
from PIL import ImageTk,Image
import os




root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(r"E:\\wall\photo.jpg"))
# panel = tk.Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
# def func():
#     pass
# tk.Button(root,text = "hello",command = func).grid(row = 0,column = 0)
root.geometry('100x200')
# root.config(Image = img)
tk.Label(root,text = "hello",bg = "black",fg = "white").grid(row = 0, column = 0)
root.mainloop()