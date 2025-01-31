import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import pywinstyles
import webbrowser
from Accs import Accounts
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme( "dark-blue")

window = ctk.CTk()
window.geometry('1920x1080')
window.title('pupq rms')

def accounts(inf, pas):
    inf = entry.get()
    pas = pswrd.get()
    for i in Accounts:
        if inf == i['Name'] and pas == i['Password']:
            return i
    else:
        return None
    
def log():
    inf = entry.get()
    pas = pswrd.get()
    lol = accounts(inf, pas)
    if lol:
        frame1.pack_forget()
        frame2.pack()
        
    else:
        print("fuck you")
    
frame1= ctk.CTkFrame(window,corner_radius=0,fg_color='#701D25', height=1080,width=500)
frame1.pack(side='right',fill='y',padx=0)
pywinstyles.set_opacity(frame1, value=0.7)
lbl = ctk.CTkLabel(frame1, text="WELCOME TO ROOM MANAGEMENT SYSTEM",font=ctk.CTkFont(family="Times New Roman",size=26))
lbl.pack(anchor='n',pady=10,padx=90)




##########################################################
error1 = Label(master = frame1, 
                   text = "Incorrect Username or Password", 
                   font = "Arial 10 bold")

head1 = ctk.CTkLabel(master = frame1, text = "Webmail:",font=ctk.CTkFont(family='Arial', size=15)).pack(pady=20)
entry = ctk.CTkEntry(master = frame1, width=500,placeholder_text="Enter your Webmail")
entry.pack(pady=20)

lbl1 = ctk.CTkLabel(frame1, text="Password:", font=ctk.CTkFont(family='Arial',size=15))
lbl1.pack(pady=20, anchor='n')

pswrd = ctk.CTkEntry(frame1, placeholder_text="Enter your password", show="*",width=500)
pswrd.pack(pady=20, anchor='n')


login_button = ctk.CTkButton(frame1, text="Login", fg_color='green', command= log)
login_button.pack(pady=20)

close = ctk.CTkButton(master = frame1, text = "Close", command = window.destroy,corner_radius=0,fg_color='red')
close.pack(pady = 10)

prep = ctk.CTkLabel(master = frame1, text='Prepared by: Javanese', font=ctk.CTkFont(family="Arial",size=15))
prep.pack(pady = 20, anchor = "n")

frame1.pack(fill='y', expand='False', side='right')

frame2 = ctk.CTkFrame(window,corner_radius=0,fg_color='green', height=1080,width=500)
lol = Label(frame2, text = 'fuck you')
lol.pack()

window.mainloop()