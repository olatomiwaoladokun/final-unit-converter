import tkinter as tk
# from .backend import start
import PIL
from PIL import Image,ImageTk
# from PIL import *
import time as tm
import _tkinter
# from tkinter import messagebox as ms
# help(PIL)

win = tk.Tk()
win.title("Welcome")
win.geometry("500x480")
win.config(bg="grey")
win.resizable(width=False, height=False)

welcome = tk.Label(text="Welcome", font=("Romans", 12), bg="grey")
welcome.place(x=220, y=260)
frame = tk.Frame(width=10, height=10)
frame.place(anchor="s", relx=0.5, rely=0.5)
logo = ImageTk.PhotoImage(Image.open("unit converter image.png"))
lb = tk.Label(frame, image=logo)
lb.pack()
def start_key():
    win.destroy()
    import page
    # start()
start_button = tk.Button(text="  Start   ", bg="green",command=start_key)
start_button.place(x=220, y=300)
    


win.mainloop()