import tkinter as ttk
from PIL import ImageTk
from tkinter import PhotoImage
from tkinter import *
from PIL import Image
import tkinter
import tkinter as tk
import pywinstyles


window = tk.Tk()
window.title("PUP RMS")
window.geometry("1920x1080")
window.iconbitmap("C:/Users/Windows 10/Documents/Python/1_Final Projects/PUPlogo.ico")

imgfile = "C:/Users/Windows 10/Documents/Python/1_Final Projects/loginbg.png"
img = Image.open(imgfile)
resize = img.resize((1920, 1080),Image.LANCZOS)

pic = ImageTk.PhotoImage(resize)
nig = Label(master = window, image = pic)
nig.pack(pady=20)
nig.place(x=0, y=0, relwidth = 1, relheight=1)




frame = LabelFrame(window, padx=300, pady=5, width= 700)
frame.configure(bg="#701D25")
frame.pack(fill='y', expand='False', side='right')
pywinstyles.set_opacity(frame, value=0.5)

txt = Label(frame,text="WECOME IN PUPPQ RMS", font=('Arial', 20), fg='black')
txt.place(relx=0.5, rely=0.5)
txt.pack(pady=50)
txt.attributes('-alpha',0.5)

logofile = "C:/Users/Windows 10/Documents/Python/1_Final Projects/PUPlogo.ico"
logo = Image.open(logofile)
golo = ImageTk.PhotoImage(logo)




window.mainloop()