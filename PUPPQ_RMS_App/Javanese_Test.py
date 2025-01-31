import tkinter as tk
#import ttkbootstrap as ttk
import customtkinter as ttk

def frames():
    lol = entry2.get()
    if lol:
        button.configure(text = "lol", fg_color = '#800000', hover_color='#800000')


def change():
    replace1 = entry.get()
    if replace1 == "Lol":
        frame2.grid()
        frame.grid_forget()



#Window
balls =ttk.CTk()

balls.title("Lmao")
balls.geometry("1920x1080") 
#Title (Stuff inside the window)

#makes the logo of the app visible on the taskbar
import ctypes
myappid ='mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
balls.iconbitmap('C:/Users/Windows 10/Documents/Python/1_Final Projects/PUPlogo.ico')

balls.after(0, lambda:balls.state('zoomed'))


frame = ttk.CTkFrame(master = balls)
content = ttk.CTkLabel(master = frame, 
                    text = "Lamao", 
                    )
ligma = tk.StringVar()
button2 = ttk.CTkButton(master = frame,
                     text = "Switch window",
                     command = change).grid()

entry2 = ttk.CTkEntry(master = frame)
entry2.grid()

content.grid()
#Input buttons and spaces
entry = ttk.CTkEntry(master = frame)
button = ttk.CTkButton(master = frame, 
                    text = "gigger lmao",
                    command = frames
                    )



button.grid()
entry.grid()

frame.grid()

#padx moves ig into the x axis by pixels while pady moves it on the y axis by pixels\

#The grid()commands are basically call functions


outputstr = tk.StringVar()
shit = ttk.CTkLabel (master = frame,
                  text = "Stuff: "
                  )
output = ttk.CTkLabel (master = frame, 
                    text = "Released?", 
                    textvariable = outputstr)
shit.grid()
output.grid()

frame.grid()

frame2 = ttk.CTkFrame(master = balls)
content1 = ttk.CTkLabel(master = frame2, 
                     text = "It worked lmao").grid()


balls.mainloop() #this calls the entire thing



