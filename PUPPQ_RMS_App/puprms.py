from tkinter import *
from PIL import ImageTk,Image
from tkinter import PhotoImage
root = Tk()
root.title('PUPRMS')
root.iconbitmap('C:/Users/Windows 10/Documents/Python/1_Final Projects/PUPlogo.png')
root.geometry('1920x1080')

img = Image.open("C:/Users/Windows 10/Documents/Python/1_Final Projects/loginbg.png")
resize = img.resize((1920, 1080), Image.LANCZOS)

pic = ImageTk.PhotoImage(resize)

label = Label(root, image=pic)
label.pack(pady=20)
label.place(x=0, y=0, relwidth=1, relheight=1)

txt = Label(root, text="WELCOME TO RMS", font=("Times Newroman", 50),fg="black")
txt.pack(pady=50)





root.mainloop()