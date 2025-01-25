import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.constants import DISABLED, NORMAL 
import ttkbootstrap as ttk
import customtkinter as ctk
import webbrowser
from Accs import Accounts
import json
from PIL import Image, ImageTk
import sqlite3
import pywinstyles

#The admin account in which only I have

Acc =   {
        'Name': "shervan",
        'Password': '1010',
        'State': 1
        }

def chgthm():
    currenttheme.replace("darkly", 'morph')

def details(user, user2):
    with open('C:/Users/Windows 10/Documents/Python/1_Final Projects/Users.json', 'r') as json_file:
        Accs = json.load(json_file)
    for a in Accs:
        a['User']
        a["State"]
        a["Rep"]
        if a["Name"] == user and a["Password"] == user2:
                return a 
    return None

#+++++++++++++++++++++++++++++++++++++++

def chngpswrd(user, pswrd):
    with open('C:/Users/Windows 10/Documents/Python/1_Final Projects/Users.json', 'r') as json_file:
        Accs = json.load(json_file)
    check = pswr(user, pswrd, Accs)
    if check:
        entry1.get()
        entry1.delete(0, 'end')
        new = instpass.get()
        check["Password"] = new
        with open('C:/Users/Windows 10/Documents/Python/1_Final Projects/Users.json', 'w') as json_file:
            json.dump(Accs, json_file, indent= 4)
        entry1.insert(0, new)


def pswr(user, pswrd, ind):
    for i in ind:
        if i["Name"] == user and i["Password"] == pswrd:
            return i
    return None

def look():
    info = (entry.get()).lower()
    psw = entry1.get()
    with open('C:/Users/Windows 10/Documents/Python/1_Final Projects/Users.json', 'r') as json_file:
        Accs = json.load(json_file)
    
    check = pswr(info, psw, Accs)
    if check:
        chngpswrd(info, psw)
        password_changed.pack()

#++++++++++++++++++++++++++++++++++++++
#Function to be able to log in when pressed (Passes bot the password and username arg)
def login():
    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    if account:
        load()
        load1()
        load2()
        load3()
        load4()
        load5()
        load6()
        load7()
        load8()
        load9()
        load10()
        load11()
        load12()
        load13()
        bg1.pack_forget()
        bg1.place_forget()
        bg2.pack(pady=20)
        bg2.place(x=0, y=0, relwidth=1, relheight=1)
        frame2.pack(pady=100,fill="both", expand="True")
        
        
        frame1.pack_forget()
       
        return account
    else:
        error1.pack()
        return None

#Function that exits the main interface when pressed, removing access to room changing if not main account       
def logoff():
    entry.get()
    entry1.get()
    entry.delete(0, 'end')
    entry1.delete(0, 'end')
    
    bg1.pack(pady=20)
    bg1.place(x=0, y=0, relwidth=1, relheight=1)
    frame1.pack(fill='y', expand='False', side='right')
    frame2.pack_forget()
    error1.pack_forget()
    bg2.pack_forget()
    bg2.place_forget()
    password_changed.pack_forget()

def logoff1():
    entry.get()
    entry1.get()
    entry.delete(0, 'end')
    entry1.delete(0, 'end')
    instmail['state'] = 'enabled'
    instmail.delete(0, 'end')
    instpass.delete(0, 'end')
    
    bg1.pack(pady=20)
    bg1.place(x=0, y=0, relwidth=1, relheight=1)
    frame1.pack(fill='y', expand='False', side='right')
    frame2.pack_forget()
    sett.pack_forget()
    error1.pack_forget()
    bg2.pack_forget()
    bg2.place_forget()
    password_changed.pack_forget()

def switch1():
    floor2.pack(pady = 150, anchor = 's', side = 'bottom')
    floor3.pack_forget()

def switch2():
    floor3.pack(pady = 150, anchor = 's', side = 'bottom')
    floor2.pack_forget()

def settings():
    frame2.pack_forget()
    sett.pack(ipadx = 100, ipady = 80, anchor= 'center', pady = 70)
    info = entry.get()
    psw = entry1.get()
    
    if entry.get():
        instmail.insert(0, info)
        instmail['state'] = 'disabled'

        instpass.insert(0, psw)


def settback():
    frame2.pack(pady=100,fill="both", expand="True")
    instmail['state'] = 'enabled'
    instmail.delete(0, 'end')
    instpass.delete(0, 'end')
    sett.pack_forget()

#===================================================================@
def about():
    bg2.pack_forget()
    bg2.place_forget()
    sett.pack_forget()
    meettheteam.pack()

def leaveabout():
    meettheteam.pack_forget()
    bg2.pack(pady=20)
    bg2.place(x=0, y=0, relwidth=1, relheight=1)
    sett.pack(ipadx = 100, ipady = 80, anchor= 'center', pady = 70)

#===================================================================@

#Button that looks like a table, room 201
def Avail():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor1 = net.cursor()
    cursor1.execute('SELECT * FROM Rooms WHERE Room_Number = 201')
    saved = cursor1.fetchone()
    
    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail.pack(ipadx = 100, ipady = 80, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched.cget('text') == 'Reserve!':
            sched.cget('text')
            sched.configure(text = "Reserve!")
            
        elif account['State'] == Acc['State'] and user == saved[7]:
            sched.cget('text')
            sched.configure(text = "Cancel Appointment")

        else:
            sched.cget('text')
            sched.configure(text = "Email President/Rep")

        net.commit()
        net.close()
        
#Room 202
def Avail1():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor2 = net.cursor()
    cursor2.execute('SELECT * FROM Rooms WHERE Room_Number = 202')
    saved1 = cursor2.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)

    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail1.pack(ipadx = 100, ipady = 65, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched1.cget('text') == 'Reserve!':
            sched1.cget('text')
            sched1.configure(text = "Reserve!")

        elif account['State'] == Acc['State'] and user == saved1[7]:
            sched1.cget('text')
            sched1.configure(text = "Cancel Appointment")

        else:
            sched1.cget('text')
            sched1.configure(text = "Email President/Rep")
            
        net.commit()
        net.close()

#Room 203
def Avail2():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor3 = net.cursor()
    cursor3.execute('SELECT * FROM Rooms WHERE Room_Number = 203')
    saved2 = cursor3.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)

    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail2.pack(ipadx = 100, ipady = 65, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched2.cget('text') == 'Reserve!':
            sched2.cget('text')
            sched2.configure(text = "Reserve!")

        elif account['State'] == Acc['State'] and user == saved2[7]:
            sched2.cget('text')
            sched2.configure(text = "Cancel Appointment")

        else:
            sched2.cget('text')
            sched2.configure(text = "Email President/Rep")
            
        net.commit()
        net.close()
        
#Room 204
def Avail3():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor4 = net.cursor()
    cursor4.execute('SELECT * FROM Rooms WHERE Room_Number = 204')
    saved3 = cursor4.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)

    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail3.pack(ipadx = 100, ipady = 65, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched3.cget('text') == 'Reserve!':
            sched3.cget('text')
            sched3.configure(text = "Reserve!")

        elif account['State'] == Acc['State'] and user == saved3[7]:
            sched3.cget('text')
            sched3.configure(text = "Cancel Appointment")

        else:
            sched3.cget('text')
            sched3.configure(text = "Email President/Rep")
            
        net.commit()
        net.close()
            
#Room 206
def Avail4():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor5 = net.cursor()
    cursor5.execute('SELECT * FROM Rooms WHERE Room_Number = 206')
    saved4 = cursor5.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)

    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail4.pack(ipadx = 100, ipady = 65, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched4.cget('text') == 'Reserve!':
            sched4.cget('text')
            sched4.configure(text = "Reserve!")

        elif account['State'] == Acc['State'] and user == saved4[7]:
            sched4.cget('text')
            sched4.configure(text = "Cancel Appointment")

        else:
            sched4.cget('text')
            sched4.configure(text = "Email President/Rep")
            
        net.commit()
        net.close()

#Room 208
def Avail5():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor6 = net.cursor()
    cursor6.execute('SELECT * FROM Rooms WHERE Room_Number = 208')
    saved5 = cursor6.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)

    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail5.pack(ipadx = 100, ipady = 65, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched5.cget('text') == 'Reserve!':
            sched5.cget('text')
            sched5.configure(text = "Reserve!")

        elif account['State'] == Acc['State'] and user == saved5[7]:
            sched5.cget('text')
            sched5.configure(text = "Cancel Appointment")

        else:
            sched5.cget('text')
            sched5.configure(text = "Email President/Rep")
            
        net.commit()
        net.close()

#Room 210
def Avail6():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor7 = net.cursor()
    cursor7.execute('SELECT * FROM Rooms WHERE Room_Number = 210')
    saved6 = cursor7.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)

    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail6.pack(ipadx = 100, ipady = 65, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched6.cget('text') == 'Reserve!':
            sched6.cget('text')
            sched6.configure(text = "Reserve!")

        elif account['State'] == Acc['State'] and user == saved6[7]:
            sched6.cget('text')
            sched6.configure(text = "Cancel Appointment")

        else:
            sched6.cget('text')
            sched6.configure(text = "Email President/Rep")
            
        net.commit()
        net.close()

#Room 301
def Avail7():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor8 = net.cursor()
    cursor8.execute('SELECT * FROM Rooms WHERE Room_Number = 301')
    saved7 = cursor8.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)

    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail7.pack(ipadx = 100, ipady = 65, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched7.cget('text') == 'Reserve!':
            sched7.cget('text')
            sched7.configure(text = "Reserve!")

        elif account['State'] == Acc['State'] and user == saved7[7]:
            sched7.cget('text')
            sched7.configure(text = "Cancel Appointment")

        else:
            sched7.cget('text')
            sched7.configure(text = "Email President/Rep")
            
        net.commit()
        net.close()

#Room 303
def Avail8():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor9 = net.cursor()
    cursor9.execute('SELECT * FROM Rooms WHERE Room_Number = 303')
    saved8 = cursor9.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)

    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail8.pack(ipadx = 100, ipady = 65, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched8.cget('text') == 'Reserve!':
            sched8.cget('text')
            sched8.configure(text = "Reserve!")

        elif account['State'] == Acc['State'] and user == saved8[7]:
            sched8.cget('text')
            sched8.configure(text = "Cancel Appointment")

        else:
            sched8.cget('text')
            sched8.configure(text = "Email President/Rep")
            
        net.commit()
        net.close()

#Room 305
def Avail9():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor10 = net.cursor()
    cursor10.execute('SELECT * FROM Rooms WHERE Room_Number = 305')
    saved9 = cursor10.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)

    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail9.pack(ipadx = 100, ipady = 65, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched9.cget('text') == 'Reserve!':
            sched9.cget('text')
            sched9.configure(text = "Reserve!")

        elif account['State'] == Acc['State'] and user == saved9[7]:
            sched9.cget('text')
            sched9.configure(text = "Cancel Appointment")

        else:
            sched9.cget('text')
            sched9.configure(text = "Email President/Rep")
            
        net.commit()
        net.close()
            
#Room 306
def Avail10():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor11 = net.cursor()
    cursor11.execute('SELECT * FROM Rooms WHERE Room_Number = 306')
    saved10 = cursor11.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)

    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail10.pack(ipadx = 100, ipady = 65, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched10.cget('text') == 'Reserve!':
            sched10.cget('text')
            sched10.configure(text = "Reserve!")

        elif account['State'] == Acc['State'] and user == saved10[7]:
            sched10.cget('text')
            sched10.configure(text = "Cancel Appointment")

        else:
            sched10.cget('text')
            sched10.configure(text = "Email President/Rep")
            
        net.commit()
        net.close()
            
#Room 307
def Avail11():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor12 = net.cursor()
    cursor12.execute('SELECT * FROM Rooms WHERE Room_Number = 307')
    saved11 = cursor12.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)

    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail11.pack(ipadx = 100, ipady = 65, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched11.cget('text') == 'Reserve!':
            sched11.cget('text')
            sched11.configure(text = "Reserve!")

        elif account['State'] == Acc['State'] and user == saved11[7]:
            sched11.cget('text')
            sched11.configure(text = "Cancel Appointment")

        else:
            sched11.cget('text')
            sched11.configure(text = "Email President/Rep")
            
        net.commit()
        net.close()
            
#Room 308
def Avail12():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor13 = net.cursor()
    cursor13.execute('SELECT * FROM Rooms WHERE Room_Number = 308')
    saved12 = cursor13.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)

    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail12.pack(ipadx = 100, ipady = 65, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched12.cget('text') == 'Reserve!':
            sched12.cget('text')
            sched12.configure(text = "Reserve!")

        elif account['State'] == Acc['State'] and user == saved12[7]:
            sched12.cget('text')
            sched12.configure(text = "Cancel Appointment")

        else:
            sched12.cget('text')
            sched12.configure(text = "Email President/Rep")
            
        net.commit()
        net.close()
        
#Room 310
def Avail13():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor14 = net.cursor()
    cursor14.execute('SELECT * FROM Rooms WHERE Room_Number = 310')
    saved13 = cursor14.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)

    mail = account['Rep']
    user = account['Repmail']

    if "Available" in State:
        tableavail13.pack(ipadx = 100, ipady = 65, anchor= 'center', pady = 70)
        frame2.pack_forget()
        if account['State'] == Acc['State'] and sched13.cget('text') == 'Reserve!':
            sched13.cget('text')
            sched13.configure(text = "Reserve!")

        elif account['State'] == Acc['State'] and user == saved13[7]:
            sched13.cget('text')
            sched13.configure(text = "Cancel Appointment")

        else:
            sched13.cget('text')
            sched13.configure(text = "Email President/Rep")
            
        net.commit()
        net.close()
        
###############################################################################
#Exit 201
def back():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail.pack_forget()

#Exit 202
def back1():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail1.pack_forget()

#Exit 203
def back2():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail2.pack_forget()

#Exit 204
def back3():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail3.pack_forget()

#Exit 206
def back4():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail4.pack_forget()

#Exit 208
def back5():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail5.pack_forget()

#Exit 210
def back6():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail6.pack_forget()

#Exit 301
def back7():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail7.pack_forget()

#Exit 303
def back8():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail8.pack_forget()

#Exit 305
def back9():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail9.pack_forget()

#Exit 306
def back10():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail10.pack_forget()

#Exit 307
def back11():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail11.pack_forget()

#Exit 308
def back12():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail12.pack_forget()

#Exit 310
def back13():
    frame2.pack(pady=100,fill="both", expand="True")
    tableavail13.pack_forget()

###############################################################################

#Reserve the 201 room
def rsrv():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor1 = net.cursor()
    cursor1.execute('SELECT * FROM Rooms WHERE Room_Number = 201')
    saved = cursor1.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input1.get()
    con2 = input2.get()
    con3 = input3.get()
    con4 = input4.get()
    con5 = input5.get()
    con6 = input6.get()
    
    but = sched.cget("text")

#account checking to see if you can cancel appointments
#When button is pressed, the entry keys will be disabled if you have placed stuff in them.
#configure basically just changes the attribute of stuff (Such as button text)

    if account['State'] == Acc['State'] and not saved:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input1['state'] = 'disabled'
                input2['state'] = 'disabled'
                input3['state'] = 'disabled'
                input4['state'] = 'disabled'
                input5['state'] = 'disabled'
                input6['state'] = 'disabled'
                cursor1.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (201, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched.configure(text = "Cancel Appointment")
                sched.configure(hover_color = "red", fg_color = "dark red")
                table1.configure(text = f"""
*Room 201
*{con1}
*{con3}
        """)
                table1.configure(hover_color = "red", fg_color = "dark red")
#Make the entry widgets  modifyable when button is pressed   (IF ADMIN ACC)   
        else:
            cursor1.execute('DELETE FROM Rooms WHERE Room_Number = 201')
            input1['state'] = 'enabled'
            input2['state'] = 'enabled'
            input3['state'] = 'enabled'
            input4['state'] = 'enabled'
            input5['state'] = 'enabled'
            input6['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched.configure(text = 'Reserve!')
            sched.configure(hover_color = "green", fg_color = "dark green")
            table1.configure(text = """
*Room 201
*Available
                    """)
            table1.configure(hover_color = "green", fg_color = "dark green")
            
    elif account['State'] == Acc['State'] and user == saved[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input1['state'] = 'disabled'
                input2['state'] = 'disabled'
                input3['state'] = 'disabled'
                input4['state'] = 'disabled'
                input5['state'] = 'disabled'
                input6['state'] = 'disabled'
                cursor1.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (201, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched.configure(text = "Cancel Appointment")
                sched.configure(hover_color = "red", fg_color = "dark red")
                table1.configure(text = f"""
*Room 201
*{con1}
*{con3}
        """)
                table1.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor1.execute('DELETE FROM Rooms WHERE Room_Number = 201')
            input1['state'] = 'enabled'
            input2['state'] = 'enabled'
            input3['state'] = 'enabled'
            input4['state'] = 'enabled'
            input5['state'] = 'enabled'
            input6['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched.configure(text = 'Reserve!')
            sched.configure(hover_color = "green", fg_color = "dark green")
            table1.configure(text = """
*Room 201
*Available
                    """)
            table1.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved[7] :
        dbmail = saved[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table1.configure(text = f"""
*Room 201
*{con1}
*{con3}
        """)
            net.commit()
            net.close()

        #If button pressed saying 'Email' then instead of scheduling, you would be
        #prompted to a website to be able to contact the admin for resched 
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table1.configure(text = f"""
*Room 201
*{con1}
*{con3}
        """)
        #If button pressed saying 'Email' then instead of scheduling, you would be
        #prompted to a website to be able to contact the admin for resched 
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)
        else:
            webbrowser.open_new(mail)

def wipe():
    input1.delete(0, 'end')
    input2.delete(0, 'end')
    input3.delete(0, 'end')
    input4.delete(0, 'end')
    input5.delete(0, 'end')
    input6.delete(0, 'end')
    
def load():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor1 = net.cursor()
    cursor1.execute('SELECT * FROM Rooms WHERE Room_Number = 201')
    saved = cursor1.fetchone()
    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input1.get()
    con2 = input2.get()
    con3 = input3.get()
    con4 = input4.get()
    con5 = input5.get()
    con6 = input6.get()

    but = sched.cget("text")
    tab = table1.cget('text')
    
    if account['State'] == Acc['State'] and not saved:
        if saved:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor:
                input1['state'] = 'disabled'
                input2['state'] = 'disabled'
                input3['state'] = 'disabled'
                input4['state'] = 'disabled'
                input5['state'] = 'disabled'
                input6['state'] = 'disabled'
                                
                sched.configure(text = "Cancel Appointment")
                sched.configure(hover_color = "red", fg_color = "dark red")
                table1.configure(text = f"""
*Room 201
*{con1}
*{con3}
        """)
                table1.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input1['state'] = 'enabled'
            input2['state'] = 'enabled'
            input3['state'] = 'enabled'
            input4['state'] = 'enabled'
            input5['state'] = 'enabled'
            input6['state'] = 'enabled'

            sched.configure(text = 'Reserve!')
            sched.configure(hover_color = "green", fg_color = "dark green")
            table1.configure(text = """
*Room 201
*Available
                    """)
            table1.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved[7]:
        if saved:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor1:
                input1['state'] = 'disabled'
                input2['state'] = 'disabled'
                input3['state'] = 'disabled'
                input4['state'] = 'disabled'
                input5['state'] = 'disabled'
                input6['state'] = 'disabled'
                                
                sched.configure(text = "Cancel Appointment")
                sched.configure(hover_color = "red", fg_color = "dark red")
                table1.configure(text = f"""
*Room 201
*{con1}
*{con3}
        """)
                table1.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input1['state'] = 'enabled'
            input2['state'] = 'enabled'
            input3['state'] = 'enabled'
            input4['state'] = 'enabled'
            input5['state'] = 'enabled'
            input6['state'] = 'enabled'

            sched.configure(text = 'Reserve!')
            sched.configure(hover_color = "green", fg_color = "dark green")
            table1.configure(text = """
*Room 201
*Available
                    """)
            table1.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input1['state'] = 'disabled'
                input2['state'] = 'disabled'
                input3['state'] = 'disabled'
                input4['state'] = 'disabled'
                input5['state'] = 'disabled'
                input6['state'] = 'disabled'
                sched.configure(hover_color = "red", fg_color = "dark red")
                sched.configure(text = "Email President/Rep")
                table1.configure(text = f"""
*Room 201
*{con1}
*{con3}
        """)
                table1.configure(hover_color = "red", fg_color = "dark red")

        else:

                input1['state'] = 'disabled'
                input2['state'] = 'disabled'
                input3['state'] = 'disabled'
                input4['state'] = 'disabled'
                input5['state'] = 'disabled'
                input6['state'] = 'disabled'


#============================================================================================================#

#same thing but in room 202
def rsrv1():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor2 = net.cursor()
    cursor2.execute('SELECT * FROM Rooms WHERE Room_Number = 202')
    saved1 = cursor2.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    name = Acc['Name']
    mail = account['Rep']
    user = account['Repmail']

    con1 = input11.get()
    con2 = input21.get()
    con3 = input31.get()
    con4 = input41.get()
    con5 = input51.get()
    con6 = input61.get()

    but = sched1.cget("text")

    if account['State'] == Acc['State'] and not saved1:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input11['state'] = 'disabled'
                input21['state'] = 'disabled'
                input31['state'] = 'disabled'
                input41['state'] = 'disabled'
                input51['state'] = 'disabled'
                input61['state'] = 'disabled'
                cursor2.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (202, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()

                sched1.configure(text = "Cancel Appointment")
                sched1.configure(hover_color = "red", fg_color = "dark red")
                table2.configure(text = f"""
*Room 202
*{con1}
*{con3}
        """)
                table2.configure(hover_color = "red", fg_color = "dark red")
               
        else:
            cursor2.execute('DELETE FROM Rooms WHERE Room_Number = 202')
            input11['state'] = 'enabled'
            input21['state'] = 'enabled'
            input31['state'] = 'enabled'
            input41['state'] = 'enabled'
            input51['state'] = 'enabled'
            input61['state'] = 'enabled'
            net.commit()
            net.close()

            sched1.configure(text = 'Reserve!')
            sched1.configure(hover_color = "green", fg_color = "dark green")
            table2.configure(text = """
*Room 202
*Available
                    """)
            table2.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved1[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input11['state'] = 'disabled'
                input21['state'] = 'disabled'
                input31['state'] = 'disabled'
                input41['state'] = 'disabled'
                input51['state'] = 'disabled'
                input61['state'] = 'disabled'
                cursor2.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (202, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched1.configure(text = "Cancel Appointment")
                sched1.configure(hover_color = "red", fg_color = "dark red")
                table2.configure(text = f"""
*Room 202
*{con1}
*{con3}
        """)
                table2.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor2.execute('DELETE FROM Rooms WHERE Room_Number = 202')
            input11['state'] = 'enabled'
            input21['state'] = 'enabled'
            input31['state'] = 'enabled'
            input41['state'] = 'enabled'
            input51['state'] = 'enabled'
            input61['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched1.configure(text = 'Reserve!')
            sched1.configure(hover_color = "green", fg_color = "dark green")
            table2.configure(text = """
*Room 202
*Available
                    """)
            table2.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved1[7]:
        dbmail = saved1[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table2.configure(text = f"""
*Room 202
*{con1}
*{con3}
        """)
            net.commit()
            net.close()
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table2.configure(text = f"""
*Room 202
*{con1}
*{con3}
        """)
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved1[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)

        else:

            webbrowser.open_new(mail)
    
def wipe1():
    input11.delete(0, 'end')
    input21.delete(0, 'end')
    input31.delete(0, 'end')
    input41.delete(0, 'end')
    input51.delete(0, 'end')
    input61.delete(0, 'end')

def load1():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor2 = net.cursor()
    cursor2 = cursor2.execute('SELECT * FROM Rooms WHERE Room_Number = 202')
    saved1 = cursor2.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input11.get()
    con2 = input21.get()
    con3 = input31.get()
    con4 = input41.get()
    con5 = input51.get()
    con6 = input61.get()

    if account['State'] == Acc['State'] and not saved1:
        if saved1:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor2:
                input11['state'] = 'disabled'
                input21['state'] = 'disabled'
                input31['state'] = 'disabled'
                input41['state'] = 'disabled'
                input51['state'] = 'disabled'
                input61['state'] = 'disabled'
                                
                sched1.configure(text = "Cancel Appointment")
                sched1.configure(hover_color = "red", fg_color = "dark red")
                table2.configure(text = f"""
*Room 202
*{con1}
*{con3}
        """)
                table2.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input11['state'] = 'enabled'
            input21['state'] = 'enabled'
            input31['state'] = 'enabled'
            input41['state'] = 'enabled'
            input51['state'] = 'enabled'
            input61['state'] = 'enabled'

            sched1.configure(text = 'Reserve!')
            sched1.configure(hover_color = "green", fg_color = "dark green")
            table2.configure(text = """
*Room 202
*Available
                    """)
            table2.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved1[7]:
        if saved1:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor2:
                input11['state'] = 'disabled'
                input21['state'] = 'disabled'
                input31['state'] = 'disabled'
                input41['state'] = 'disabled'
                input51['state'] = 'disabled'
                input61['state'] = 'disabled'
                                
                sched1.configure(text = "Cancel Appointment")
                sched1.configure(hover_color = "red", fg_color = "dark red")
                table2.configure(text = f"""
*Room 202
*{con1}
*{con3}
        """)
                table2.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input11['state'] = 'enabled'
            input21['state'] = 'enabled'
            input31['state'] = 'enabled'
            input41['state'] = 'enabled'
            input51['state'] = 'enabled'
            input61['state'] = 'enabled'

            sched1.configure(text = 'Reserve!')
            sched1.configure(hover_color = "green", fg_color = "dark green")
            table2.configure(text = """
*Room 202
*Available
                    """)
            table2.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved1:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input11['state'] = 'disabled'
                input21['state'] = 'disabled'
                input31['state'] = 'disabled'
                input41['state'] = 'disabled'
                input51['state'] = 'disabled'
                input61['state'] = 'disabled'
                sched1.configure(hover_color = "red", fg_color = "dark red")
                sched1.configure(text = "Email President/Rep")
                table2.configure(text = f"""
*Room 202
*{con1}
*{con3}
        """)
                table2.configure(hover_color = "red", fg_color = "dark red")

        else:
                input11['state'] = 'disabled'
                input21['state'] = 'disabled'
                input31['state'] = 'disabled'
                input41['state'] = 'disabled'
                input51['state'] = 'disabled'
                input61['state'] = 'disabled'
                
            
#=============================================================================================================================================================================================================#

def rsrv2():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor3 = net.cursor()
    cursor3.execute('SELECT * FROM Rooms WHERE Room_Number = 203')
    saved2 = cursor3.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    name = Acc['Name']
    mail = account['Rep']
    user = account['Repmail']

    con1 = input12.get()
    con2 = input22.get()
    con3 = input32.get()
    con4 = input42.get()
    con5 = input52.get()
    con6 = input62.get()

    but = sched2.cget("text")

    if account['State'] == Acc['State'] and not saved2:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input12['state'] = 'disabled'
                input22['state'] = 'disabled'
                input32['state'] = 'disabled'
                input42['state'] = 'disabled'
                input52['state'] = 'disabled'
                input62['state'] = 'disabled'
                cursor3.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (203, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()

                sched2.configure(text = "Cancel Appointment")
                sched2.configure(hover_color = "red", fg_color = "dark red")
                table3.configure(text = f"""
*Room 203
*{con1}
*{con3}
        """)
                table3.configure(hover_color = "red", fg_color = "dark red")
               
        else:
            cursor3.execute('DELETE FROM Rooms WHERE Room_Number = 203')
            input12['state'] = 'enabled'
            input22['state'] = 'enabled'
            input32['state'] = 'enabled'
            input42['state'] = 'enabled'
            input52['state'] = 'enabled'
            input62['state'] = 'enabled'
            net.commit()
            net.close()

            sched2.configure(text = 'Reserve!')
            sched2.configure(hover_color = "green", fg_color = "dark green")
            table3.configure(text = """
*Room 203
*Available
                    """)
            table3.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved2[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input12['state'] = 'disabled'
                input22['state'] = 'disabled'
                input32['state'] = 'disabled'
                input42['state'] = 'disabled'
                input52['state'] = 'disabled'
                input62['state'] = 'disabled'
                cursor3.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (203, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched2.configure(text = "Cancel Appointment")
                sched2.configure(hover_color = "red", fg_color = "dark red")
                table3.configure(text = f"""
*Room 203
*{con1}
*{con3}
        """)
                table3.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor3.execute('DELETE FROM Rooms WHERE Room_Number = 203')
            input12['state'] = 'enabled'
            input22['state'] = 'enabled'
            input32['state'] = 'enabled'
            input42['state'] = 'enabled'
            input52['state'] = 'enabled'
            input62['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched2.configure(text = 'Reserve!')
            sched2.configure(hover_color = "green", fg_color = "dark green")
            table3.configure(text = """
*Room 203
*Available
                    """)
            table3.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved2[7]:
        dbmail = saved2[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table3.configure(text = f"""
*Room 203
*{con1}
*{con3}
        """)
            net.commit()
            net.close()
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table3.configure(text = f"""
*Room 203
*{con1}
*{con3}
        """)
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved2[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)

        else:

            webbrowser.open_new(mail)

def wipe2():
    input12.delete(0, 'end')
    input22.delete(0, 'end')
    input32.delete(0, 'end')
    input42.delete(0, 'end')
    input52.delete(0, 'end')
    input62.delete(0, 'end')

def load2():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor3 = net.cursor()
    cursor3 = cursor3.execute('SELECT * FROM Rooms WHERE Room_Number = 203')
    saved2 = cursor3.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input12.get()
    con2 = input22.get()
    con3 = input32.get()
    con4 = input42.get()
    con5 = input52.get()
    con6 = input62.get()

    if account['State'] == Acc['State'] and not saved2:
        if saved2:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor3:
                input12['state'] = 'disabled'
                input22['state'] = 'disabled'
                input32['state'] = 'disabled'
                input42['state'] = 'disabled'
                input52['state'] = 'disabled'
                input62['state'] = 'disabled'
                                
                sched2.configure(text = "Cancel Appointment")
                sched2.configure(hover_color = "red", fg_color = "dark red")
                table3.configure(text = f"""
*Room 203
*{con1}
*{con3}
        """)
                table3.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input12['state'] = 'enabled'
            input22['state'] = 'enabled'
            input32['state'] = 'enabled'
            input42['state'] = 'enabled'
            input52['state'] = 'enabled'
            input62['state'] = 'enabled'

            sched2.configure(text = 'Reserve!')
            sched2.configure(hover_color = "green", fg_color = "dark green")
            table3.configure(text = """
*Room 203
*Available
                    """)
            table3.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved2[7]:
        if saved2:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor3:
                input12['state'] = 'disabled'
                input22['state'] = 'disabled'
                input32['state'] = 'disabled'
                input42['state'] = 'disabled'
                input52['state'] = 'disabled'
                input62['state'] = 'disabled'
                                
                sched2.configure(text = "Cancel Appointment")
                sched2.configure(hover_color = "red", fg_color = "dark red")
                table3.configure(text = f"""
*Room 203
*{con1}
*{con3}
        """)
                table3.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input12['state'] = 'enabled'
            input22['state'] = 'enabled'
            input32['state'] = 'enabled'
            input42['state'] = 'enabled'
            input52['state'] = 'enabled'
            input62['state'] = 'enabled'

            sched2.configure(text = 'Reserve!')
            sched2.configure(hover_color = "green", fg_color = "dark green")
            table3.configure(text = """
*Room 203
*Available
                    """)
            table3.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved2:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input12['state'] = 'disabled'
                input22['state'] = 'disabled'
                input32['state'] = 'disabled'
                input42['state'] = 'disabled'
                input52['state'] = 'disabled'
                input62['state'] = 'disabled'
                sched2.configure(hover_color = "red", fg_color = "dark red")
                sched2.configure(text = "Email President/Rep")
                table3.configure(text = f"""
*Room 203
*{con1}
*{con3}
        """)
                table3.configure(hover_color = "red", fg_color = "dark red")

        else:
                input12['state'] = 'disabled'
                input22['state'] = 'disabled'
                input32['state'] = 'disabled'
                input42['state'] = 'disabled'
                input52['state'] = 'disabled'
                input62['state'] = 'disabled'
                
            
#=============================================================================================================================================================================================================#

def rsrv3():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor4 = net.cursor()
    cursor4.execute('SELECT * FROM Rooms WHERE Room_Number = 204')
    saved3 = cursor4.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    name = Acc['Name']
    mail = account['Rep']
    user = account['Repmail']

    con1 = input13.get()
    con2 = input23.get()
    con3 = input33.get()
    con4 = input43.get()
    con5 = input53.get()
    con6 = input63.get()

    but = sched3.cget("text")

    if account['State'] == Acc['State'] and not saved3:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input13['state'] = 'disabled'
                input23['state'] = 'disabled'
                input33['state'] = 'disabled'
                input43['state'] = 'disabled'
                input53['state'] = 'disabled'
                input63['state'] = 'disabled'
                cursor4.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (204, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()

                sched3.configure(text = "Cancel Appointment")
                sched3.configure(hover_color = "red", fg_color = "dark red")
                table4.configure(text = f"""
*Room 204
*{con1}
*{con3}
        """)
                table4.configure(hover_color = "red", fg_color = "dark red")
               
        else:
            cursor4.execute('DELETE FROM Rooms WHERE Room_Number = 204')
            input13['state'] = 'enabled'
            input23['state'] = 'enabled'
            input33['state'] = 'enabled'
            input43['state'] = 'enabled'
            input53['state'] = 'enabled'
            input63['state'] = 'enabled'
            net.commit()
            net.close()

            sched3.configure(text = 'Reserve!')
            sched3.configure(hover_color = "green", fg_color = "dark green")
            table4.configure(text = """
*Room 204
*Available
                    """)
            table4.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved3[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input13['state'] = 'disabled'
                input23['state'] = 'disabled'
                input33['state'] = 'disabled'
                input43['state'] = 'disabled'
                input53['state'] = 'disabled'
                input63['state'] = 'disabled'
                cursor4.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (204, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched3.configure(text = "Cancel Appointment")
                sched3.configure(hover_color = "red", fg_color = "dark red")
                table4.configure(text = f"""
*Room 204
*{con1}
*{con3}
        """)
                table4.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor4.execute('DELETE FROM Rooms WHERE Room_Number = 204')
            input13['state'] = 'enabled'
            input23['state'] = 'enabled'
            input33['state'] = 'enabled'
            input43['state'] = 'enabled'
            input53['state'] = 'enabled'
            input63['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched3.configure(text = 'Reserve!')
            sched3.configure(hover_color = "green", fg_color = "dark green")
            table4.configure(text = """
*Room 204
*Available
                    """)
            table4.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved3[7]:
        dbmail = saved3[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table4.configure(text = f"""
*Room 204
*{con1}
*{con3}
        """)
            net.commit()
            net.close()
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table4.configure(text = f"""
*Room 204
*{con1}
*{con3}
        """)
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved3[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)

        else:

            webbrowser.open_new(mail)

def wipe3():
    input13.delete(0, 'end')
    input23.delete(0, 'end')
    input33.delete(0, 'end')
    input43.delete(0, 'end')
    input53.delete(0, 'end')
    input63.delete(0, 'end')

def load3():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor4 = net.cursor()
    cursor4 = cursor4.execute('SELECT * FROM Rooms WHERE Room_Number = 204')
    saved3 = cursor4.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input13.get()
    con2 = input23.get()
    con3 = input33.get()
    con4 = input43.get()
    con5 = input53.get()
    con6 = input63.get()

    if account['State'] == Acc['State'] and not saved3:
        if saved3:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor4:
                input13['state'] = 'disabled'
                input23['state'] = 'disabled'
                input33['state'] = 'disabled'
                input43['state'] = 'disabled'
                input53['state'] = 'disabled'
                input63['state'] = 'disabled'
                                
                sched3.configure(text = "Cancel Appointment")
                sched3.configure(hover_color = "red", fg_color = "dark red")
                table4.configure(text = f"""
*Room 204
*{con1}
*{con3}
        """)
                table4.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input13['state'] = 'enabled'
            input23['state'] = 'enabled'
            input33['state'] = 'enabled'
            input43['state'] = 'enabled'
            input53['state'] = 'enabled'
            input63['state'] = 'enabled'

            sched3.configure(text = 'Reserve!')
            sched3.configure(hover_color = "green", fg_color = "dark green")
            table4.configure(text = """
*Room 204
*Available
                    """)
            table4.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved3[7]:
        if saved3:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor4:
                input13['state'] = 'disabled'
                input23['state'] = 'disabled'
                input33['state'] = 'disabled'
                input43['state'] = 'disabled'
                input53['state'] = 'disabled'
                input63['state'] = 'disabled'
                                
                sched3.configure(text = "Cancel Appointment")
                sched3.configure(hover_color = "red", fg_color = "dark red")
                table4.configure(text = f"""
*Room 204
*{con1}
*{con3}
        """)
                table4.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input13['state'] = 'enabled'
            input23['state'] = 'enabled'
            input33['state'] = 'enabled'
            input43['state'] = 'enabled'
            input53['state'] = 'enabled'
            input63['state'] = 'enabled'

            sched3.configure(text = 'Reserve!')
            sched3.configure(hover_color = "green", fg_color = "dark green")
            table4.configure(text = """
*Room 204
*Available
                    """)
            table4.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved3:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input13['state'] = 'disabled'
                input23['state'] = 'disabled'
                input33['state'] = 'disabled'
                input43['state'] = 'disabled'
                input53['state'] = 'disabled'
                input63['state'] = 'disabled'
                sched3.configure(hover_color = "red", fg_color = "dark red")
                sched3.configure(text = "Email President/Rep")
                table4.configure(text = f"""
*Room 204
*{con1}
*{con3}
        """)
                table4.configure(hover_color = "red", fg_color = "dark red")

        else:
                input13['state'] = 'disabled'
                input23['state'] = 'disabled'
                input33['state'] = 'disabled'
                input43['state'] = 'disabled'
                input53['state'] = 'disabled'
                input63['state'] = 'disabled'
                
            
#=============================================================================================================================================================================================================#


def rsrv4():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor5 = net.cursor()
    cursor5.execute('SELECT * FROM Rooms WHERE Room_Number = 206')
    saved4 = cursor5.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    name = Acc['Name']
    mail = account['Rep']
    user = account['Repmail']

    con1 = input14.get()
    con2 = input24.get()
    con3 = input34.get()
    con4 = input44.get()
    con5 = input54.get()
    con6 = input64.get()

    but = sched4.cget("text")

    if account['State'] == Acc['State'] and not saved4:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input14['state'] = 'disabled'
                input24['state'] = 'disabled'
                input34['state'] = 'disabled'
                input44['state'] = 'disabled'
                input54['state'] = 'disabled'
                input64['state'] = 'disabled'
                cursor5.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (206, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()

                sched4.configure(text = "Cancel Appointment")
                sched4.configure(hover_color = "red", fg_color = "dark red")
                table5.configure(text = f"""
*Room 206
*{con1}
*{con3}
        """)
                table5.configure(hover_color = "red", fg_color = "dark red")
               
        else:
            cursor5.execute('DELETE FROM Rooms WHERE Room_Number = 206')
            input14['state'] = 'enabled'
            input24['state'] = 'enabled'
            input34['state'] = 'enabled'
            input44['state'] = 'enabled'
            input54['state'] = 'enabled'
            input64['state'] = 'enabled'
            net.commit()
            net.close()

            sched4.configure(text = 'Reserve!')
            sched4.configure(hover_color = "green", fg_color = "dark green")
            table5.configure(text = """
*Room 206
*Available
                    """)
            table5.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved4[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input14['state'] = 'disabled'
                input24['state'] = 'disabled'
                input34['state'] = 'disabled'
                input44['state'] = 'disabled'
                input54['state'] = 'disabled'
                input64['state'] = 'disabled'
                cursor5.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (206, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched4.configure(text = "Cancel Appointment")
                sched4.configure(hover_color = "red", fg_color = "dark red")
                table5.configure(text = f"""
*Room 206
*{con1}
*{con3}
        """)
                table5.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor5.execute('DELETE FROM Rooms WHERE Room_Number = 206')
            input14['state'] = 'enabled'
            input24['state'] = 'enabled'
            input34['state'] = 'enabled'
            input44['state'] = 'enabled'
            input54['state'] = 'enabled'
            input64['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched4.configure(text = 'Reserve!')
            sched4.configure(hover_color = "green", fg_color = "dark green")
            table5.configure(text = """
*Room 206
*Available
                    """)
            table5.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved4[7]:
        dbmail = saved4[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table5.configure(text = f"""
*Room 206
*{con1}
*{con3}
        """)
            net.commit()
            net.close()
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table5.configure(text = f"""
*Room 206
*{con1}
*{con3}
        """)
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved4[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)

        else:

            webbrowser.open_new(mail)

def wipe4():
    input14.delete(0, 'end')
    input24.delete(0, 'end')
    input34.delete(0, 'end')
    input44.delete(0, 'end')
    input54.delete(0, 'end')
    input64.delete(0, 'end')

def load4():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor5 = net.cursor()
    cursor5 = cursor5.execute('SELECT * FROM Rooms WHERE Room_Number = 206')
    saved4 = cursor5.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input14.get()
    con2 = input24.get()
    con3 = input34.get()
    con4 = input44.get()
    con5 = input54.get()
    con6 = input64.get()

    if account['State'] == Acc['State'] and not saved4:
        if saved4:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor5:
                input14['state'] = 'disabled'
                input24['state'] = 'disabled'
                input34['state'] = 'disabled'
                input44['state'] = 'disabled'
                input54['state'] = 'disabled'
                input64['state'] = 'disabled'
                                
                sched4.configure(text = "Cancel Appointment")
                sched4.configure(hover_color = "red", fg_color = "dark red")
                table5.configure(text = f"""
*Room 206
*{con1}
*{con3}
        """)
                table5.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input14['state'] = 'enabled'
            input24['state'] = 'enabled'
            input34['state'] = 'enabled'
            input44['state'] = 'enabled'
            input54['state'] = 'enabled'
            input64['state'] = 'enabled'

            sched4.configure(text = 'Reserve!')
            sched4.configure(hover_color = "green", fg_color = "dark green")
            table5.configure(text = """
*Room 206
*Available
                    """)
            table5.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved4[7]:
        if saved4:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor5:
                input14['state'] = 'disabled'
                input24['state'] = 'disabled'
                input34['state'] = 'disabled'
                input44['state'] = 'disabled'
                input54['state'] = 'disabled'
                input64['state'] = 'disabled'
                                
                sched4.configure(text = "Cancel Appointment")
                sched4.configure(hover_color = "red", fg_color = "dark red")
                table5.configure(text = f"""
*Room 206
*{con1}
*{con3}
        """)
                table5.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input14['state'] = 'enabled'
            input24['state'] = 'enabled'
            input34['state'] = 'enabled'
            input44['state'] = 'enabled'
            input54['state'] = 'enabled'
            input64['state'] = 'enabled'

            sched4.configure(text = 'Reserve!')
            sched4.configure(hover_color = "green", fg_color = "dark green")
            table5.configure(text = """
*Room 206
*Available
                    """)
            table5.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved4:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input14['state'] = 'disabled'
                input24['state'] = 'disabled'
                input34['state'] = 'disabled'
                input44['state'] = 'disabled'
                input54['state'] = 'disabled'
                input64['state'] = 'disabled'
                sched4.configure(hover_color = "red", fg_color = "dark red")
                sched4.configure(text = "Email President/Rep")
                table5.configure(text = f"""
*Room 206
*{con1}
*{con3}
        """)
                table5.configure(hover_color = "red", fg_color = "dark red")

        else:
                input14['state'] = 'disabled'
                input24['state'] = 'disabled'
                input34['state'] = 'disabled'
                input44['state'] = 'disabled'
                input54['state'] = 'disabled'
                input64['state'] = 'disabled'
                
            
#=============================================================================================================================================================================================================#

def rsrv5():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor6 = net.cursor()
    cursor6.execute('SELECT * FROM Rooms WHERE Room_Number = 208')
    saved5 = cursor6.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    name = Acc['Name']
    mail = account['Rep']
    user = account['Repmail']

    con1 = input15.get()
    con2 = input25.get()
    con3 = input35.get()
    con4 = input45.get()
    con5 = input55.get()
    con6 = input65.get()

    but = sched5.cget("text")

    if account['State'] == Acc['State'] and not saved5:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input15['state'] = 'disabled'
                input25['state'] = 'disabled'
                input35['state'] = 'disabled'
                input45['state'] = 'disabled'
                input55['state'] = 'disabled'
                input65['state'] = 'disabled'
                cursor6.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (208, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()

                sched5.configure(text = "Cancel Appointment")
                sched5.configure(hover_color = "red", fg_color = "dark red")
                table6.configure(text = f"""
*Room 208
*{con1}
*{con3}
        """)
                table6.configure(hover_color = "red", fg_color = "dark red")
               
        else:
            cursor6.execute('DELETE FROM Rooms WHERE Room_Number = 208')
            input15['state'] = 'enabled'
            input25['state'] = 'enabled'
            input35['state'] = 'enabled'
            input45['state'] = 'enabled'
            input55['state'] = 'enabled'
            input65['state'] = 'enabled'
            net.commit()
            net.close()

            sched5.configure(text = 'Reserve!')
            sched5.configure(hover_color = "green", fg_color = "dark green")
            table6.configure(text = """
*Room 208
*Available
                    """)
            table6.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved5[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input15['state'] = 'disabled'
                input25['state'] = 'disabled'
                input35['state'] = 'disabled'
                input45['state'] = 'disabled'
                input55['state'] = 'disabled'
                input65['state'] = 'disabled'
                cursor6.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (208, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched5.configure(text = "Cancel Appointment")
                sched5.configure(hover_color = "red", fg_color = "dark red")
                table6.configure(text = f"""
*Room 208
*{con1}
*{con3}
        """)
                table6.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor6.execute('DELETE FROM Rooms WHERE Room_Number = 208')
            input15['state'] = 'enabled'
            input25['state'] = 'enabled'
            input35['state'] = 'enabled'
            input45['state'] = 'enabled'
            input55['state'] = 'enabled'
            input65['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched5.configure(text = 'Reserve!')
            sched5.configure(hover_color = "green", fg_color = "dark green")
            table6.configure(text = """
*Room 208
*Available
                    """)
            table6.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved5[7]:
        dbmail = saved5[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table6.configure(text = f"""
*Room 208
*{con1}
*{con3}
        """)
            net.commit()
            net.close()
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table6.configure(text = f"""
*Room 208
*{con1}
*{con3}
        """)
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved5[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)

        else:

            webbrowser.open_new(mail)

def wipe5():
    input15.delete(0, 'end')
    input25.delete(0, 'end')
    input35.delete(0, 'end')
    input45.delete(0, 'end')
    input55.delete(0, 'end')
    input65.delete(0, 'end')

def load5():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor6 = net.cursor()
    cursor6 = cursor6.execute('SELECT * FROM Rooms WHERE Room_Number = 208')
    saved5 = cursor6.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input15.get()
    con2 = input25.get()
    con3 = input35.get()
    con4 = input45.get()
    con5 = input55.get()
    con6 = input65.get()

    if account['State'] == Acc['State'] and not saved5:
        if saved5:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor5:
                input15['state'] = 'disabled'
                input25['state'] = 'disabled'
                input35['state'] = 'disabled'
                input45['state'] = 'disabled'
                input45['state'] = 'disabled'
                input65['state'] = 'disabled'
                                
                sched5.configure(text = "Cancel Appointment")
                sched5.configure(hover_color = "red", fg_color = "dark red")
                table6.configure(text = f"""
*Room 208
*{con1}
*{con3}
        """)
                table6.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input15['state'] = 'enabled'
            input25['state'] = 'enabled'
            input35['state'] = 'enabled'
            input45['state'] = 'enabled'
            input55['state'] = 'enabled'
            input65['state'] = 'enabled'

            sched5.configure(text = 'Reserve!')
            sched5.configure(hover_color = "green", fg_color = "dark green")
            table6.configure(text = """
*Room 208
*Available
                    """)
            table6.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved5[7]:
        if saved5:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor6:
                input15['state'] = 'disabled'
                input25['state'] = 'disabled'
                input35['state'] = 'disabled'
                input45['state'] = 'disabled'
                input55['state'] = 'disabled'
                input65['state'] = 'disabled'
                                
                sched5.configure(text = "Cancel Appointment")
                sched5.configure(hover_color = "red", fg_color = "dark red")
                table6.configure(text = f"""
*Room 208
*{con1}
*{con3}
        """)
                table6.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input15['state'] = 'enabled'
            input25['state'] = 'enabled'
            input35['state'] = 'enabled'
            input45['state'] = 'enabled'
            input55['state'] = 'enabled'
            input65['state'] = 'enabled'

            sched5.configure(text = 'Reserve!')
            sched5.configure(hover_color = "green", fg_color = "dark green")
            table6.configure(text = """
*Room 208
*Available
                    """)
            table6.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved5:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input15['state'] = 'disabled'
                input25['state'] = 'disabled'
                input35['state'] = 'disabled'
                input45['state'] = 'disabled'
                input55['state'] = 'disabled'
                input65['state'] = 'disabled'
                sched5.configure(hover_color = "red", fg_color = "dark red")
                sched5.configure(text = "Email President/Rep")
                table6.configure(text = f"""
*Room 208
*{con1}
*{con3}
        """)
                table6.configure(hover_color = "red", fg_color = "dark red")

        else:
                input15['state'] = 'disabled'
                input25['state'] = 'disabled'
                input35['state'] = 'disabled'
                input45['state'] = 'disabled'
                input55['state'] = 'disabled'
                input65['state'] = 'disabled'

#=============================================================================================================================================================================================================#

def rsrv6():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor7 = net.cursor()
    cursor7.execute('SELECT * FROM Rooms WHERE Room_Number = 210')
    saved6 = cursor7.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    name = Acc['Name']
    mail = account['Rep']
    user = account['Repmail']

    con1 = input16.get()
    con2 = input26.get()
    con3 = input36.get()
    con4 = input46.get()
    con5 = input56.get()
    con6 = input66.get()

    but = sched6.cget("text")

    if account['State'] == Acc['State'] and not saved6:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input16['state'] = 'disabled'
                input26['state'] = 'disabled'
                input36['state'] = 'disabled'
                input46['state'] = 'disabled'
                input56['state'] = 'disabled'
                input66['state'] = 'disabled'
                cursor7.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (210, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()

                sched6.configure(text = "Cancel Appointment")
                sched6.configure(hover_color = "red", fg_color = "dark red")
                table7.configure(text = f"""
*Room 210
*{con1}
*{con3}
        """)
                table7.configure(hover_color = "red", fg_color = "dark red")
               
        else:
            cursor7.execute('DELETE FROM Rooms WHERE Room_Number = 210')
            input16['state'] = 'enabled'
            input26['state'] = 'enabled'
            input36['state'] = 'enabled'
            input46['state'] = 'enabled'
            input56['state'] = 'enabled'
            input66['state'] = 'enabled'
            net.commit()
            net.close()

            sched6.configure(text = 'Reserve!')
            sched6.configure(hover_color = "green", fg_color = "dark green")
            table7.configure(text = """
*Room 210
*Available
                    """)
            table7.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved6[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input16['state'] = 'disabled'
                input26['state'] = 'disabled'
                input36['state'] = 'disabled'
                input46['state'] = 'disabled'
                input56['state'] = 'disabled'
                input66['state'] = 'disabled'
                cursor7.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (210, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched6.configure(text = "Cancel Appointment")
                sched6.configure(hover_color = "red", fg_color = "dark red")
                table7.configure(text = f"""
*Room 210
*{con1}
*{con3}
        """)
                table7.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor7.execute('DELETE FROM Rooms WHERE Room_Number = 210')
            input16['state'] = 'enabled'
            input26['state'] = 'enabled'
            input36['state'] = 'enabled'
            input46['state'] = 'enabled'
            input56['state'] = 'enabled'
            input66['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched6.configure(text = 'Reserve!')
            sched6.configure(hover_color = "green", fg_color = "dark green")
            table7.configure(text = """
*Room 210
*Available
                    """)
            table7.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved6[7]:
        dbmail = saved6[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table7.configure(text = f"""
*Room 210
*{con1}
*{con3}
        """)
            net.commit()
            net.close()
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table7.configure(text = f"""
*Room 210
*{con1}
*{con3}
        """)
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved6[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)

        else:

            webbrowser.open_new(mail)

def wipe6():
    input16.delete(0, 'end')
    input26.delete(0, 'end')
    input36.delete(0, 'end')
    input46.delete(0, 'end')
    input56.delete(0, 'end')
    input66.delete(0, 'end')

def load6():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor7 = net.cursor()
    cursor7 = cursor7.execute('SELECT * FROM Rooms WHERE Room_Number = 210')
    saved6 = cursor7.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input16.get()
    con2 = input26.get()
    con3 = input36.get()
    con4 = input46.get()
    con5 = input56.get()
    con6 = input66.get()

    if account['State'] == Acc['State'] and not saved6:
        if saved6:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor7:
                input16['state'] = 'disabled'
                input26['state'] = 'disabled'
                input36['state'] = 'disabled'
                input46['state'] = 'disabled'
                input56['state'] = 'disabled'
                input66['state'] = 'disabled'
                                
                sched6.configure(text = "Cancel Appointment")
                sched6.configure(hover_color = "red", fg_color = "dark red")
                table7.configure(text = f"""
*Room 210
*{con1}
*{con3}
        """)
                table7.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input16['state'] = 'enabled'
            input26['state'] = 'enabled'
            input36['state'] = 'enabled'
            input46['state'] = 'enabled'
            input56['state'] = 'enabled'
            input66['state'] = 'enabled'

            sched6.configure(text = 'Reserve!')
            sched6.configure(hover_color = "green", fg_color = "dark green")
            table7.configure(text = """
*Room 210
*Available
                    """)
            table7.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved6[7]:
        if saved6:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor7:
                input16['state'] = 'disabled'
                input26['state'] = 'disabled'
                input36['state'] = 'disabled'
                input46['state'] = 'disabled'
                input56['state'] = 'disabled'
                input66['state'] = 'disabled'
                                
                sched6.configure(text = "Cancel Appointment")
                sched6.configure(hover_color = "red", fg_color = "dark red")
                table7.configure(text = f"""
*Room 210
*{con1}
*{con3}
        """)
                table7.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input16['state'] = 'enabled'
            input26['state'] = 'enabled'
            input36['state'] = 'enabled'
            input46['state'] = 'enabled'
            input56['state'] = 'enabled'
            input66['state'] = 'enabled'

            sched6.configure(text = 'Reserve!')
            sched6.configure(hover_color = "green", fg_color = "dark green")
            table7.configure(text = """
*Room 210
*Available
                    """)
            table7.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved6:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input16['state'] = 'disabled'
                input26['state'] = 'disabled'
                input36['state'] = 'disabled'
                input46['state'] = 'disabled'
                input56['state'] = 'disabled'
                input66['state'] = 'disabled'
                sched6.configure(hover_color = "red", fg_color = "dark red")
                sched6.configure(text = "Email President/Rep")
                table7.configure(text = f"""
*Room 210
*{con1}
*{con3}
        """)
                table7.configure(hover_color = "red", fg_color = "dark red")

        else:
                input16['state'] = 'disabled'
                input26['state'] = 'disabled'
                input36['state'] = 'disabled'
                input46['state'] = 'disabled'
                input56['state'] = 'disabled'
                input66['state'] = 'disabled'
                

#=============================================================================================================================================================================================================#

def rsrv7():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor8 = net.cursor()
    cursor8.execute('SELECT * FROM Rooms WHERE Room_Number = 301')
    saved7 = cursor8.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    name = Acc['Name']
    mail = account['Rep']
    user = account['Repmail']

    con1 = input17.get()
    con2 = input27.get()
    con3 = input37.get()
    con4 = input47.get()
    con5 = input57.get()
    con6 = input67.get()

    but = sched7.cget("text")

    if account['State'] == Acc['State'] and not saved7:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input17['state'] = 'disabled'
                input27['state'] = 'disabled'
                input37['state'] = 'disabled'
                input47['state'] = 'disabled'
                input57['state'] = 'disabled'
                input67['state'] = 'disabled'
                cursor8.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (301, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()

                sched7.configure(text = "Cancel Appointment")
                sched7.configure(hover_color = "red", fg_color = "dark red")
                table8.configure(text = f"""
*Room 301
*{con1}
*{con3}
        """)
                table8.configure(hover_color = "red", fg_color = "dark red")
               
        else:
            cursor8.execute('DELETE FROM Rooms WHERE Room_Number = 301')
            input17['state'] = 'enabled'
            input27['state'] = 'enabled'
            input37['state'] = 'enabled'
            input47['state'] = 'enabled'
            input57['state'] = 'enabled'
            input67['state'] = 'enabled'
            net.commit()
            net.close()

            sched7.configure(text = 'Reserve!')
            sched7.configure(hover_color = "green", fg_color = "dark green")
            table8.configure(text = """
*Room 301
*Available
                    """)
            table8.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved7[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input17['state'] = 'disabled'
                input27['state'] = 'disabled'
                input37['state'] = 'disabled'
                input47['state'] = 'disabled'
                input57['state'] = 'disabled'
                input67['state'] = 'disabled'
                cursor8.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (301, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched7.configure(text = "Cancel Appointment")
                sched7.configure(hover_color = "red", fg_color = "dark red")
                table8.configure(text = f"""
*Room 301
*{con1}
*{con3}
        """)
                table8.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor8.execute('DELETE FROM Rooms WHERE Room_Number = 301')
            input17['state'] = 'enabled'
            input27['state'] = 'enabled'
            input37['state'] = 'enabled'
            input47['state'] = 'enabled'
            input57['state'] = 'enabled'
            input67['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched7.configure(text = 'Reserve!')
            sched7.configure(hover_color = "green", fg_color = "dark green")
            table8.configure(text = """
*Room 301
*Available
                    """)
            table8.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved7[7]:
        dbmail = saved7[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table8.configure(text = f"""
*Room 301
*{con1}
*{con3}
        """)
            net.commit()
            net.close()
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table8.configure(text = f"""
*Room 301
*{con1}
*{con3}
        """)
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved7[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)

        else:

            webbrowser.open_new(mail)

def wipe7():
    input17.delete(0, 'end')
    input27.delete(0, 'end')
    input37.delete(0, 'end')
    input47.delete(0, 'end')
    input57.delete(0, 'end')
    input67.delete(0, 'end')

def load7():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor8 = net.cursor()
    cursor8 = cursor8.execute('SELECT * FROM Rooms WHERE Room_Number = 301')
    saved7 = cursor8.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input17.get()
    con2 = input27.get()
    con3 = input37.get()
    con4 = input47.get()
    con5 = input57.get()
    con6 = input67.get()

    if account['State'] == Acc['State'] and not saved7:
        if saved7:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor8:
                input17['state'] = 'disabled'
                input27['state'] = 'disabled'
                input37['state'] = 'disabled'
                input47['state'] = 'disabled'
                input57['state'] = 'disabled'
                input67['state'] = 'disabled'
                                
                sched7.configure(text = "Cancel Appointment")
                sched7.configure(hover_color = "red", fg_color = "dark red")
                table8.configure(text = f"""
*Room 301
*{con1}
*{con3}
        """)
                table8.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input17['state'] = 'enabled'
            input27['state'] = 'enabled'
            input37['state'] = 'enabled'
            input47['state'] = 'enabled'
            input57['state'] = 'enabled'
            input67['state'] = 'enabled'

            sched7.configure(text = 'Reserve!')
            sched7.configure(hover_color = "green", fg_color = "dark green")
            table8.configure(text = """
*Room 301
*Available
                    """)
            table8.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved7[7]:
        if saved7:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor8:
                input17['state'] = 'disabled'
                input27['state'] = 'disabled'
                input37['state'] = 'disabled'
                input47['state'] = 'disabled'
                input57['state'] = 'disabled'
                input67['state'] = 'disabled'
                                
                sched7.configure(text = "Cancel Appointment")
                sched7.configure(hover_color = "red", fg_color = "dark red")
                table8.configure(text = f"""
*Room 301
*{con1}
*{con3}
        """)
                table8.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input17['state'] = 'enabled'
            input27['state'] = 'enabled'
            input37['state'] = 'enabled'
            input47['state'] = 'enabled'
            input57['state'] = 'enabled'
            input67['state'] = 'enabled'

            sched7.configure(text = 'Reserve!')
            sched7.configure(hover_color = "green", fg_color = "dark green")
            table8.configure(text = """
*Room 301
*Available
                    """)
            table8.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved7:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input17['state'] = 'disabled'
                input27['state'] = 'disabled'
                input37['state'] = 'disabled'
                input47['state'] = 'disabled'
                input57['state'] = 'disabled'
                input67['state'] = 'disabled'
                sched7.configure(hover_color = "red", fg_color = "dark red")
                sched7.configure(text = "Email President/Rep")
                table8.configure(text = f"""
*Room 301
*{con1}
*{con3}
        """)
                table8.configure(hover_color = "red", fg_color = "dark red")

        else:
                input17['state'] = 'disabled'
                input27['state'] = 'disabled'
                input37['state'] = 'disabled'
                input47['state'] = 'disabled'
                input57['state'] = 'disabled'
                input67['state'] = 'disabled'
                

#=============================================================================================================================================================================================================#

def rsrv8():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor9 = net.cursor()
    cursor9.execute('SELECT * FROM Rooms WHERE Room_Number = 303')
    saved8 = cursor9.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    name = Acc['Name']
    mail = account['Rep']
    user = account['Repmail']

    con1 = input18.get()
    con2 = input28.get()
    con3 = input38.get()
    con4 = input48.get()
    con5 = input58.get()
    con6 = input68.get()

    but = sched8.cget("text")

    if account['State'] == Acc['State'] and not saved8:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input18['state'] = 'disabled'
                input28['state'] = 'disabled'
                input38['state'] = 'disabled'
                input48['state'] = 'disabled'
                input58['state'] = 'disabled'
                input68['state'] = 'disabled'
                cursor9.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (303, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()

                sched8.configure(text = "Cancel Appointment")
                sched8.configure(hover_color = "red", fg_color = "dark red")
                table9.configure(text = f"""
*Room 303
*{con1}
*{con3}
        """)
                table9.configure(hover_color = "red", fg_color = "dark red")
               
        else:
            cursor9.execute('DELETE FROM Rooms WHERE Room_Number = 303')
            input18['state'] = 'enabled'
            input28['state'] = 'enabled'
            input38['state'] = 'enabled'
            input48['state'] = 'enabled'
            input58['state'] = 'enabled'
            input68['state'] = 'enabled'
            net.commit()
            net.close()

            sched8.configure(text = 'Reserve!')
            sched8.configure(hover_color = "green", fg_color = "dark green")
            table9.configure(text = """
*Room 303
*Available
                    """)
            table9.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved8[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input18['state'] = 'disabled'
                input28['state'] = 'disabled'
                input38['state'] = 'disabled'
                input48['state'] = 'disabled'
                input58['state'] = 'disabled'
                input68['state'] = 'disabled'
                cursor9.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (303, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched8.configure(text = "Cancel Appointment")
                sched8.configure(hover_color = "red", fg_color = "dark red")
                table9.configure(text = f"""
*Room 303
*{con1}
*{con3}
        """)
                table8.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor9.execute('DELETE FROM Rooms WHERE Room_Number = 303')
            input18['state'] = 'enabled'
            input28['state'] = 'enabled'
            input38['state'] = 'enabled'
            input48['state'] = 'enabled'
            input58['state'] = 'enabled'
            input68['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched8.configure(text = 'Reserve!')
            sched8.configure(hover_color = "green", fg_color = "dark green")
            table9.configure(text = """
*Room 303
*Available
                    """)
            table9.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved8[7]:
        dbmail = saved8[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table9.configure(text = f"""
*Room 303
*{con1}
*{con3}
        """)
            net.commit()
            net.close()
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table9.configure(text = f"""
*Room 303
*{con1}
*{con3}
        """)
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved8[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)

        else:

            webbrowser.open_new(mail)

def wipe8():
    input18.delete(0, 'end')
    input28.delete(0, 'end')
    input38.delete(0, 'end')
    input48.delete(0, 'end')
    input58.delete(0, 'end')
    input68.delete(0, 'end')

def load8():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor9 = net.cursor()
    cursor9 = cursor9.execute('SELECT * FROM Rooms WHERE Room_Number = 303')
    saved8 = cursor9.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input18.get()
    con2 = input28.get()
    con3 = input38.get()
    con4 = input48.get()
    con5 = input58.get()
    con6 = input68.get()

    if account['State'] == Acc['State'] and not saved8:
        if saved8:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor9:
                input18['state'] = 'disabled'
                input28['state'] = 'disabled'
                input38['state'] = 'disabled'
                input48['state'] = 'disabled'
                input58['state'] = 'disabled'
                input68['state'] = 'disabled'
                                
                sched8.configure(text = "Cancel Appointment")
                sched8.configure(hover_color = "red", fg_color = "dark red")
                table9.configure(text = f"""
*Room 303
*{con1}
*{con3}
        """)
                table9.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input18['state'] = 'enabled'
            input28['state'] = 'enabled'
            input38['state'] = 'enabled'
            input48['state'] = 'enabled'
            input58['state'] = 'enabled'
            input68['state'] = 'enabled'

            sched8.configure(text = 'Reserve!')
            sched8.configure(hover_color = "green", fg_color = "dark green")
            table9.configure(text = """
*Room 303
*Available
                    """)
            table9.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved8[7]:
        if saved8:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor9:
                input18['state'] = 'disabled'
                input28['state'] = 'disabled'
                input38['state'] = 'disabled'
                input48['state'] = 'disabled'
                input58['state'] = 'disabled'
                input68['state'] = 'disabled'
                                
                sched8.configure(text = "Cancel Appointment")
                sched8.configure(hover_color = "red", fg_color = "dark red")
                table9.configure(text = f"""
*Room 303
*{con1}
*{con3}
        """)
                table9.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input18['state'] = 'enabled'
            input28['state'] = 'enabled'
            input38['state'] = 'enabled'
            input48['state'] = 'enabled'
            input58['state'] = 'enabled'
            input68['state'] = 'enabled'

            sched8.configure(text = 'Reserve!')
            sched8.configure(hover_color = "green", fg_color = "dark green")
            table9.configure(text = """
*Room 303
*Available
                    """)
            table9.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved8:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input18['state'] = 'disabled'
                input28['state'] = 'disabled'
                input38['state'] = 'disabled'
                input48['state'] = 'disabled'
                input58['state'] = 'disabled'
                input68['state'] = 'disabled'
                sched8.configure(hover_color = "red", fg_color = "dark red")
                sched8.configure(text = "Email President/Rep")
                table9.configure(text = f"""
*Room 303
*{con1}
*{con3}
        """)
                table9.configure(hover_color = "red", fg_color = "dark red")

        else:
                input18['state'] = 'disabled'
                input28['state'] = 'disabled'
                input38['state'] = 'disabled'
                input48['state'] = 'disabled'
                input58['state'] = 'disabled'
                input68['state'] = 'disabled'
   

#=============================================================================================================================================================================================================#


def rsrv9():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor10 = net.cursor()
    cursor10.execute('SELECT * FROM Rooms WHERE Room_Number = 305')
    saved9 = cursor10.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    name = Acc['Name']
    mail = account['Rep']
    user = account['Repmail']

    con1 = input19.get()
    con2 = input29.get()
    con3 = input39.get()
    con4 = input49.get()
    con5 = input59.get()
    con6 = input69.get()

    but = sched9.cget("text")

    if account['State'] == Acc['State'] and not saved9:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input19['state'] = 'disabled'
                input29['state'] = 'disabled'
                input39['state'] = 'disabled'
                input49['state'] = 'disabled'
                input59['state'] = 'disabled'
                input69['state'] = 'disabled'
                cursor10.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (305, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()

                sched9.configure(text = "Cancel Appointment")
                sched9.configure(hover_color = "red", fg_color = "dark red")
                table10.configure(text = f"""
*Room 305
*{con1}
*{con3}
        """)
                table10.configure(hover_color = "red", fg_color = "dark red")
               
        else:
            cursor10.execute('DELETE FROM Rooms WHERE Room_Number = 305')
            input19['state'] = 'enabled'
            input29['state'] = 'enabled'
            input39['state'] = 'enabled'
            input49['state'] = 'enabled'
            input59['state'] = 'enabled'
            input69['state'] = 'enabled'
            net.commit()
            net.close()

            sched9.configure(text = 'Reserve!')
            sched9.configure(hover_color = "green", fg_color = "dark green")
            table10.configure(text = """
*Room 305
*Available
                    """)
            table10.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved9[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input19['state'] = 'disabled'
                input29['state'] = 'disabled'
                input39['state'] = 'disabled'
                input49['state'] = 'disabled'
                input59['state'] = 'disabled'
                input69['state'] = 'disabled'
                cursor10.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (305, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched9.configure(text = "Cancel Appointment")
                sched9.configure(hover_color = "red", fg_color = "dark red")
                table10.configure(text = f"""
*Room 305
*{con1}
*{con3}
        """)
                table10.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor10.execute('DELETE FROM Rooms WHERE Room_Number = 305')
            input19['state'] = 'enabled'
            input29['state'] = 'enabled'
            input39['state'] = 'enabled'
            input49['state'] = 'enabled'
            input59['state'] = 'enabled'
            input69['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched9.configure(text = 'Reserve!')
            sched9.configure(hover_color = "green", fg_color = "dark green")
            table10.configure(text = """
*Room 305
*Available
                    """)
            table10.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved9[7]:
        dbmail = saved9[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table10.configure(text = f"""
*Room 305
*{con1}
*{con3}
        """)
            net.commit()
            net.close()
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table10.configure(text = f"""
*Room 305
*{con1}
*{con3}
        """)
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved9[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)

        else:

            webbrowser.open_new(mail)

def wipe9():
    input19.delete(0, 'end')
    input29.delete(0, 'end')
    input39.delete(0, 'end')
    input49.delete(0, 'end')
    input59.delete(0, 'end')
    input69.delete(0, 'end')

def load9():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor10 = net.cursor()
    cursor10 = cursor10.execute('SELECT * FROM Rooms WHERE Room_Number = 305')
    saved9 = cursor10.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input19.get()
    con2 = input29.get()
    con3 = input39.get()
    con4 = input49.get()
    con5 = input59.get()
    con6 = input69.get()

    if account['State'] == Acc['State'] and not saved9:
        if saved9:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor10:
                input19['state'] = 'disabled'
                input29['state'] = 'disabled'
                input39['state'] = 'disabled'
                input49['state'] = 'disabled'
                input59['state'] = 'disabled'
                input69['state'] = 'disabled'
                                
                sched9.configure(text = "Cancel Appointment")
                sched9.configure(hover_color = "red", fg_color = "dark red")
                table10.configure(text = f"""
*Room 305
*{con1}
*{con3}
        """)
                table10.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input19['state'] = 'enabled'
            input29['state'] = 'enabled'
            input39['state'] = 'enabled'
            input49['state'] = 'enabled'
            input59['state'] = 'enabled'
            input69['state'] = 'enabled'

            sched9.configure(text = 'Reserve!')
            sched9.configure(hover_color = "green", fg_color = "dark green")
            table10.configure(text = """
*Room 305
*Available
                    """)
            table10.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved9[7]:
        if saved9:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor10:
                input19['state'] = 'disabled'
                input29['state'] = 'disabled'
                input39['state'] = 'disabled'
                input49['state'] = 'disabled'
                input59['state'] = 'disabled'
                input69['state'] = 'disabled'
                                
                sched9.configure(text = "Cancel Appointment")
                sched9.configure(hover_color = "red", fg_color = "dark red")
                table10.configure(text = f"""
*Room 305
*{con1}
*{con3}
        """)
                table10.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input19['state'] = 'enabled'
            input29['state'] = 'enabled'
            input39['state'] = 'enabled'
            input49['state'] = 'enabled'
            input59['state'] = 'enabled'
            input69['state'] = 'enabled'

            sched9.configure(text = 'Reserve!')
            sched9.configure(hover_color = "green", fg_color = "dark green")
            table10.configure(text = """
*Room 305
*Available
                    """)
            table10.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved9:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input19['state'] = 'disabled'
                input29['state'] = 'disabled'
                input39['state'] = 'disabled'
                input49['state'] = 'disabled'
                input59['state'] = 'disabled'
                input69['state'] = 'disabled'
                sched9.configure(hover_color = "red", fg_color = "dark red")
                sched9.configure(text = "Email President/Rep")
                table10.configure(text = f"""
*Room 305
*{con1}
*{con3}
        """)
                table10.configure(hover_color = "red", fg_color = "dark red")

        else:
                input19['state'] = 'disabled'
                input29['state'] = 'disabled'
                input39['state'] = 'disabled'
                input49['state'] = 'disabled'
                input59['state'] = 'disabled'
                input69['state'] = 'disabled'
                


#=============================================================================================================================================================================================================#

def rsrv10():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor11 = net.cursor()
    cursor11.execute('SELECT * FROM Rooms WHERE Room_Number = 306')
    saved10 = cursor11.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    name = Acc['Name']
    mail = account['Rep']
    user = account['Repmail']

    con1 = input10.get()
    con2 = input20.get()
    con3 = input30.get()
    con4 = input40.get()
    con5 = input50.get()
    con6 = input60.get()

    but = sched10.cget("text")

    if account['State'] == Acc['State'] and not saved10:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input10['state'] = 'disabled'
                input20['state'] = 'disabled'
                input30['state'] = 'disabled'
                input40['state'] = 'disabled'
                input50['state'] = 'disabled'
                input60['state'] = 'disabled'
                cursor11.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (306, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()

                sched10.configure(text = "Cancel Appointment")
                sched10.configure(hover_color = "red", fg_color = "dark red")
                table11.configure(text = f"""
*Room 306
*{con1}
*{con3}
        """)
                table11.configure(hover_color = "red", fg_color = "dark red")
               
        else:
            cursor11.execute('DELETE FROM Rooms WHERE Room_Number = 306')
            input10['state'] = 'enabled'
            input20['state'] = 'enabled'
            input30['state'] = 'enabled'
            input40['state'] = 'enabled'
            input50['state'] = 'enabled'
            input60['state'] = 'enabled'
            net.commit()
            net.close()

            sched10.configure(text = 'Reserve!')
            sched10.configure(hover_color = "green", fg_color = "dark green")
            table11.configure(text = """
*Room 306
*Available
                    """)
            table11.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved10[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input10['state'] = 'disabled'
                input20['state'] = 'disabled'
                input30['state'] = 'disabled'
                input40['state'] = 'disabled'
                input50['state'] = 'disabled'
                input60['state'] = 'disabled'
                cursor11.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (306, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched10.configure(text = "Cancel Appointment")
                sched10.configure(hover_color = "red", fg_color = "dark red")
                table11.configure(text = f"""
*Room 306
*{con1}
*{con3}
        """)
                table11.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor11.execute('DELETE FROM Rooms WHERE Room_Number = 306')
            input10['state'] = 'enabled'
            input20['state'] = 'enabled'
            input30['state'] = 'enabled'
            input40['state'] = 'enabled'
            input50['state'] = 'enabled'
            input60['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched10.configure(text = 'Reserve!')
            sched10.configure(hover_color = "green", fg_color = "dark green")
            table11.configure(text = """
*Room 306
*Available
                    """)
            table11.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved10[7]:
        dbmail = saved10[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table11.configure(text = f"""
*Room 306
*{con1}
*{con3}
        """)
            net.commit()
            net.close()
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table11.configure(text = f"""
*Room 306
*{con1}
*{con3}
        """)
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved10[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)

        else:

            webbrowser.open_new(mail)

def wipe10():
    input10.delete(0, 'end')
    input20.delete(0, 'end')
    input30.delete(0, 'end')
    input40.delete(0, 'end')
    input50.delete(0, 'end')
    input60.delete(0, 'end')

def load10():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor11 = net.cursor()
    cursor11 = cursor11.execute('SELECT * FROM Rooms WHERE Room_Number = 306')
    saved10 = cursor11.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input10.get()
    con2 = input20.get()
    con3 = input30.get()
    con4 = input40.get()
    con5 = input50.get()
    con6 = input60.get()

    if account['State'] == Acc['State'] and not saved10:
        if saved10:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor11:
                input10['state'] = 'disabled'
                input20['state'] = 'disabled'
                input30['state'] = 'disabled'
                input40['state'] = 'disabled'
                input50['state'] = 'disabled'
                input60['state'] = 'disabled'
                                
                sched10.configure(text = "Cancel Appointment")
                sched10.configure(hover_color = "red", fg_color = "dark red")
                table11.configure(text = f"""
*Room 306
*{con1}
*{con3}
        """)
                table11.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input10['state'] = 'enabled'
            input20['state'] = 'enabled'
            input30['state'] = 'enabled'
            input40['state'] = 'enabled'
            input50['state'] = 'enabled'
            input60['state'] = 'enabled'

            sched10.configure(text = 'Reserve!')
            sched10.configure(hover_color = "green", fg_color = "dark green")
            table11.configure(text = """
*Room 306
*Available
                    """)
            table11.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved10[7]:
        if saved10:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor11:
                input10['state'] = 'disabled'
                input20['state'] = 'disabled'
                input30['state'] = 'disabled'
                input40['state'] = 'disabled'
                input50['state'] = 'disabled'
                input60['state'] = 'disabled'
                                
                sched10.configure(text = "Cancel Appointment")
                sched10.configure(hover_color = "red", fg_color = "dark red")
                table11.configure(text = f"""
*Room 306
*{con1}
*{con3}
        """)
                table11.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input10['state'] = 'enabled'
            input20['state'] = 'enabled'
            input30['state'] = 'enabled'
            input40['state'] = 'enabled'
            input50['state'] = 'enabled'
            input60['state'] = 'enabled'

            sched10.configure(text = 'Reserve!')
            sched10.configure(hover_color = "green", fg_color = "dark green")
            table11.configure(text = """
*Room 306
*Available
                    """)
            table11.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved10:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input10['state'] = 'disabled'
                input20['state'] = 'disabled'
                input30['state'] = 'disabled'
                input40['state'] = 'disabled'
                input50['state'] = 'disabled'
                input60['state'] = 'disabled'
                sched10.configure(hover_color = "red", fg_color = "dark red")
                sched10.configure(text = "Email President/Rep")
                table11.configure(text = f"""
*Room 306
*{con1}
*{con3}
        """)
                table11.configure(hover_color = "red", fg_color = "dark red")

        else:
                input10['state'] = 'disabled'
                input20['state'] = 'disabled'
                input30['state'] = 'disabled'
                input40['state'] = 'disabled'
                input50['state'] = 'disabled'
                input60['state'] = 'disabled'
                

#=============================================================================================================================================================================================================#

def rsrv11():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor12 = net.cursor()
    cursor12.execute('SELECT * FROM Rooms WHERE Room_Number = 307')
    saved11 = cursor12.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    name = Acc['Name']
    mail = account['Rep']
    user = account['Repmail']

    con1 = input101.get()
    con2 = input201.get()
    con3 = input301.get()
    con4 = input401.get()
    con5 = input501.get()
    con6 = input601.get()

    but = sched11.cget("text")

    if account['State'] == Acc['State'] and not saved11:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input101['state'] = 'disabled'
                input201['state'] = 'disabled'
                input301['state'] = 'disabled'
                input401['state'] = 'disabled'
                input501['state'] = 'disabled'
                input601['state'] = 'disabled'
                cursor12.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (307, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()

                sched11.configure(text = "Cancel Appointment")
                sched11.configure(hover_color = "red", fg_color = "dark red")
                table12.configure(text = f"""
*Room 307
*{con1}
*{con3}
        """)
                table12.configure(hover_color = "red", fg_color = "dark red")
               
        else:
            cursor12.execute('DELETE FROM Rooms WHERE Room_Number = 307')
            input101['state'] = 'enabled'
            input201['state'] = 'enabled'
            input301['state'] = 'enabled'
            input401['state'] = 'enabled'
            input501['state'] = 'enabled'
            input601['state'] = 'enabled'
            net.commit()
            net.close()

            sched11.configure(text = 'Reserve!')
            sched11.configure(hover_color = "green", fg_color = "dark green")
            table12.configure(text = """
*Room 307
*Available
                    """)
            table12.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved11[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input101['state'] = 'disabled'
                input201['state'] = 'disabled'
                input301['state'] = 'disabled'
                input401['state'] = 'disabled'
                input501['state'] = 'disabled'
                input601['state'] = 'disabled'
                cursor12.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (307, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched11.configure(text = "Cancel Appointment")
                sched11.configure(hover_color = "red", fg_color = "dark red")
                table12.configure(text = f"""
*Room 307
*{con1}
*{con3}
        """)
                table12.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor12.execute('DELETE FROM Rooms WHERE Room_Number = 307')
            input101['state'] = 'enabled'
            input201['state'] = 'enabled'
            input301['state'] = 'enabled'
            input401['state'] = 'enabled'
            input501['state'] = 'enabled'
            input601['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched11.configure(text = 'Reserve!')
            sched11.configure(hover_color = "green", fg_color = "dark green")
            table12.configure(text = """
*Room 307
*Available
                    """)
            table12.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved11[7]:
        dbmail = saved11[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table12.configure(text = f"""
*Room 307
*{con1}
*{con3}
        """)
            net.commit()
            net.close()
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table12.configure(text = f"""
*Room 307
*{con1}
*{con3}
        """)
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved11[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)

        else:

            webbrowser.open_new(mail)

def wipe11():
    input101.delete(0, 'end')
    input201.delete(0, 'end')
    input301.delete(0, 'end')
    input401.delete(0, 'end')
    input501.delete(0, 'end')
    input601.delete(0, 'end')

def load11():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor12 = net.cursor()
    cursor12 = cursor12.execute('SELECT * FROM Rooms WHERE Room_Number = 307')
    saved11 = cursor12.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input101.get()
    con2 = input201.get()
    con3 = input301.get()
    con4 = input401.get()
    con5 = input501.get()
    con6 = input601.get()

    if account['State'] == Acc['State'] and not saved11:
        if saved11:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor12:
                input101['state'] = 'disabled'
                input201['state'] = 'disabled'
                input301['state'] = 'disabled'
                input401['state'] = 'disabled'
                input501['state'] = 'disabled'
                input601['state'] = 'disabled'
                                
                sched11.configure(text = "Cancel Appointment")
                sched11.configure(hover_color = "red", fg_color = "dark red")
                table12.configure(text = f"""
*Room 307
*{con1}
*{con3}
        """)
                table12.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input101['state'] = 'enabled'
            input201['state'] = 'enabled'
            input301['state'] = 'enabled'
            input401['state'] = 'enabled'
            input501['state'] = 'enabled'
            input601['state'] = 'enabled'

            sched11.configure(text = 'Reserve!')
            sched11.configure(hover_color = "green", fg_color = "dark green")
            table12.configure(text = """
*Room 307
*Available
                    """)
            table12.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved11[7]:
        if saved11:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor12:
                input101['state'] = 'disabled'
                input201['state'] = 'disabled'
                input301['state'] = 'disabled'
                input401['state'] = 'disabled'
                input501['state'] = 'disabled'
                input601['state'] = 'disabled'
                                
                sched11.configure(text = "Cancel Appointment")
                sched11.configure(hover_color = "red", fg_color = "dark red")
                table12.configure(text = f"""
*Room 307
*{con1}
*{con3}
        """)
                table12.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input101['state'] = 'enabled'
            input201['state'] = 'enabled'
            input301['state'] = 'enabled'
            input401['state'] = 'enabled'
            input501['state'] = 'enabled'
            input601['state'] = 'enabled'

            sched11.configure(text = 'Reserve!')
            sched11.configure(hover_color = "green", fg_color = "dark green")
            table12.configure(text = """
*Room 307
*Available
                    """)
            table12.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved11:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input101['state'] = 'disabled'
                input201['state'] = 'disabled'
                input301['state'] = 'disabled'
                input401['state'] = 'disabled'
                input501['state'] = 'disabled'
                input601['state'] = 'disabled'
                sched11.configure(hover_color = "red", fg_color = "dark red")
                sched11.configure(text = "Email President/Rep")
                table12.configure(text = f"""
*Room 307
*{con1}
*{con3}
        """)
                table12.configure(hover_color = "red", fg_color = "dark red")

        else:
                input101['state'] = 'disabled'
                input201['state'] = 'disabled'
                input301['state'] = 'disabled'
                input401['state'] = 'disabled'
                input501['state'] = 'disabled'
                input601['state'] = 'disabled'
                

#=============================================================================================================================================================================================================#

def rsrv12():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor13 = net.cursor()
    cursor13.execute('SELECT * FROM Rooms WHERE Room_Number = 308')
    saved12 = cursor13.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    name = Acc['Name']
    mail = account['Rep']
    user = account['Repmail']

    con1 = input102.get()
    con2 = input202.get()
    con3 = input302.get()
    con4 = input402.get()
    con5 = input502.get()
    con6 = input602.get()

    but = sched12.cget("text")

    if account['State'] == Acc['State'] and not saved12:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input102['state'] = 'disabled'
                input202['state'] = 'disabled'
                input302['state'] = 'disabled'
                input402['state'] = 'disabled'
                input502['state'] = 'disabled'
                input602['state'] = 'disabled'
                cursor13.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (308, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()

                sched12.configure(text = "Cancel Appointment")
                sched12.configure(hover_color = "red", fg_color = "dark red")
                table13.configure(text = f"""
*Room 308
*{con1}
*{con3}
        """)
                table13.configure(hover_color = "red", fg_color = "dark red")
               
        else:
            cursor13.execute('DELETE FROM Rooms WHERE Room_Number = 308')
            input102['state'] = 'enabled'
            input202['state'] = 'enabled'
            input302['state'] = 'enabled'
            input402['state'] = 'enabled'
            input502['state'] = 'enabled'
            input602['state'] = 'enabled'
            net.commit()
            net.close()

            sched12.configure(text = 'Reserve!')
            sched12.configure(hover_color = "green", fg_color = "dark green")
            table13.configure(text = """
*Room 308
*Available
                    """)
            table13.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved12[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input102['state'] = 'disabled'
                input202['state'] = 'disabled'
                input302['state'] = 'disabled'
                input402['state'] = 'disabled'
                input502['state'] = 'disabled'
                input602['state'] = 'disabled'
                cursor13.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (308, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched12.configure(text = "Cancel Appointment")
                sched12.configure(hover_color = "red", fg_color = "dark red")
                table13.configure(text = f"""
*Room 308
*{con1}
*{con3}
        """)
                table13.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor13.execute('DELETE FROM Rooms WHERE Room_Number = 308')
            input102['state'] = 'enabled'
            input202['state'] = 'enabled'
            input302['state'] = 'enabled'
            input402['state'] = 'enabled'
            input502['state'] = 'enabled'
            input602['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched12.configure(text = 'Reserve!')
            sched12.configure(hover_color = "green", fg_color = "dark green")
            table13.configure(text = """
*Room 308
*Available
                    """)
            table13.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved12[7]:
        dbmail = saved12[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table13.configure(text = f"""
*Room 308
*{con1}
*{con3}
        """)
            net.commit()
            net.close()
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table13.configure(text = f"""
*Room 308
*{con1}
*{con3}
        """)
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved12[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)

        else:

            webbrowser.open_new(mail)

def wipe12():
    input102.delete(0, 'end')
    input202.delete(0, 'end')
    input302.delete(0, 'end')
    input402.delete(0, 'end')
    input502.delete(0, 'end')
    input602.delete(0, 'end')

def load12():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor13 = net.cursor()
    cursor13 = cursor13.execute('SELECT * FROM Rooms WHERE Room_Number = 308')
    saved12 = cursor13.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input102.get()
    con2 = input202.get()
    con3 = input302.get()
    con4 = input402.get()
    con5 = input502.get()
    con6 = input602.get()

    if account['State'] == Acc['State'] and not saved12:
        if saved12:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor13:
                input102['state'] = 'disabled'
                input202['state'] = 'disabled'
                input302['state'] = 'disabled'
                input402['state'] = 'disabled'
                input502['state'] = 'disabled'
                input602['state'] = 'disabled'
                                
                sched12.configure(text = "Cancel Appointment")
                sched12.configure(hover_color = "red", fg_color = "dark red")
                table13.configure(text = f"""
*Room 308
*{con1}
*{con3}
        """)
                table13.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input102['state'] = 'enabled'
            input202['state'] = 'enabled'
            input302['state'] = 'enabled'
            input402['state'] = 'enabled'
            input502['state'] = 'enabled'
            input602['state'] = 'enabled'

            sched12.configure(text = 'Reserve!')
            sched12.configure(hover_color = "green", fg_color = "dark green")
            table13.configure(text = """
*Room 308
*Available
                    """)
            table13.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved12[7]:
        if saved12:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor13:
                input102['state'] = 'disabled'
                input202['state'] = 'disabled'
                input302['state'] = 'disabled'
                input402['state'] = 'disabled'
                input502['state'] = 'disabled'
                input602['state'] = 'disabled'
                                
                sched12.configure(text = "Cancel Appointment")
                sched12.configure(hover_color = "red", fg_color = "dark red")
                table13.configure(text = f"""
*Room 308
*{con1}
*{con3}
        """)
                table13.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input102['state'] = 'enabled'
            input202['state'] = 'enabled'
            input302['state'] = 'enabled'
            input402['state'] = 'enabled'
            input502['state'] = 'enabled'
            input602['state'] = 'enabled'

            sched12.configure(text = 'Reserve!')
            sched12.configure(hover_color = "green", fg_color = "dark green")
            table13.configure(text = """
*Room 308
*Available
                    """)
            table13.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved12:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input102['state'] = 'disabled'
                input202['state'] = 'disabled'
                input302['state'] = 'disabled'
                input402['state'] = 'disabled'
                input502['state'] = 'disabled'
                input602['state'] = 'disabled'
                sched12.configure(hover_color = "red", fg_color = "dark red")
                sched12.configure(text = "Email President/Rep")
                table13.configure(text = f"""
*Room 308
*{con1}
*{con3}
        """)
                table13.configure(hover_color = "red", fg_color = "dark red")

        else:
                input102['state'] = 'disabled'
                input202['state'] = 'disabled'
                input302['state'] = 'disabled'
                input402['state'] = 'disabled'
                input502['state'] = 'disabled'
                input602['state'] = 'disabled'
                

#=============================================================================================================================================================================================================#

def rsrv13():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor14 = net.cursor()
    cursor14.execute('SELECT * FROM Rooms WHERE Room_Number = 310')
    saved13 = cursor14.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    name = Acc['Name']
    mail = account['Rep']
    user = account['Repmail']

    con1 = input103.get()
    con2 = input203.get()
    con3 = input303.get()
    con4 = input403.get()
    con5 = input503.get()
    con6 = input603.get()

    but = sched13.cget("text")

    if account['State'] == Acc['State'] and not saved13:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input103['state'] = 'disabled'
                input203['state'] = 'disabled'
                input303['state'] = 'disabled'
                input403['state'] = 'disabled'
                input503['state'] = 'disabled'
                input603['state'] = 'disabled'
                cursor14.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (310, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()

                sched13.configure(text = "Cancel Appointment")
                sched13.configure(hover_color = "red", fg_color = "dark red")
                table14.configure(text = f"""
*Room 310
*{con1}
*{con3}
        """)
                table14.configure(hover_color = "red", fg_color = "dark red")
               
        else:
            cursor14.execute('DELETE FROM Rooms WHERE Room_Number = 310')
            input103['state'] = 'enabled'
            input203['state'] = 'enabled'
            input303['state'] = 'enabled'
            input403['state'] = 'enabled'
            input503['state'] = 'enabled'
            input603['state'] = 'enabled'
            net.commit()
            net.close()

            sched13.configure(text = 'Reserve!')
            sched13.configure(hover_color = "green", fg_color = "dark green")
            table14.configure(text = """
*Room 310
*Available
                    """)
            table14.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved13[7]:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                input103['state'] = 'disabled'
                input203['state'] = 'disabled'
                input303['state'] = 'disabled'
                input403['state'] = 'disabled'
                input503['state'] = 'disabled'
                input603['state'] = 'disabled'
                cursor14.execute("""INSERT INTO Rooms (Room_Number, Program_Year_Section, Professor, Time, Date, Activity, Class_Rep, User) VALUES (310, ?, ?, ?, ?, ?, ?, ?)
                               """,(con1,
                                   con2,
                                   con3,
                                   con4,
                                   con5,
                                   con6,
                                   user))
                net.commit()
                net.close()
                
                sched13.configure(text = "Cancel Appointment")
                sched13.configure(hover_color = "red", fg_color = "dark red")
                table14.configure(text = f"""
*Room 310
*{con1}
*{con3}
        """)
                table14.configure(hover_color = "red", fg_color = "dark red") 
        else:
            cursor14.execute('DELETE FROM Rooms WHERE Room_Number = 310')
            input103['state'] = 'enabled'
            input203['state'] = 'enabled'
            input303['state'] = 'enabled'
            input403['state'] = 'enabled'
            input503['state'] = 'enabled'
            input603['state'] = 'enabled'

            net.commit()
            net.close()
            
            sched13.configure(text = 'Reserve!')
            sched13.configure(hover_color = "green", fg_color = "dark green")
            table14.configure(text = """
*Room 310
*Available
                    """)
            table14.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user != saved13[7]:
        dbmail = saved13[7]
        mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"

        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table14.configure(text = f"""
*Room 310
*{con1}
*{con3}
        """)
            net.commit()
            net.close()
        else:
            webbrowser.open_new(mailto)

    else:
        if but == "Reserve!":
            if con1 and con2 and con3 and con4 and con5 and con6:
                table14.configure(text = f"""
*Room 310
*{con1}
*{con3}
        """)
        elif con1 and con2 and con3 and con4 and con5 and con6:
            dbmail = saved13[7]
            mailto = f"mailto:{dbmail}?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out"
            webbrowser.open_new(mailto)

        else:

            webbrowser.open_new(mail)

def wipe13():
    input103.delete(0, 'end')
    input203.delete(0, 'end')
    input303.delete(0, 'end')
    input403.delete(0, 'end')
    input503.delete(0, 'end')
    input603.delete(0, 'end')

def load13():
    net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
    cursor14 = net.cursor()
    cursor14 = cursor14.execute('SELECT * FROM Rooms WHERE Room_Number = 310')
    saved13 = cursor14.fetchone()

    info = (entry.get()).lower()
    psw = entry1.get()
    account = details(info, psw)
    mail = account['Rep']
    user = account['Repmail']

    con1 = input103.get()
    con2 = input203.get()
    con3 = input303.get()
    con4 = input403.get()
    con5 = input503.get()
    con6 = input603.get()

    if account['State'] == Acc['State'] and not saved13:
        if saved13:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor14:
                input103['state'] = 'disabled'
                input203['state'] = 'disabled'
                input303['state'] = 'disabled'
                input403['state'] = 'disabled'
                input503['state'] = 'disabled'
                input603['state'] = 'disabled'
                                
                sched13.configure(text = "Cancel Appointment")
                sched13.configure(hover_color = "red", fg_color = "dark red")
                table14.configure(text = f"""
*Room 310
*{con1}
*{con3}
        """)
                table14.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input103['state'] = 'enabled'
            input203['state'] = 'enabled'
            input303['state'] = 'enabled'
            input403['state'] = 'enabled'
            input503['state'] = 'enabled'
            input603['state'] = 'enabled'

            sched13.configure(text = 'Reserve!')
            sched13.configure(hover_color = "green", fg_color = "dark green")
            table14.configure(text = """
*Room 310
*Available
                    """)
            table14.configure(hover_color = "green", fg_color = "dark green")

    elif account['State'] == Acc['State'] and user == saved13[7]:
        if saved13:
            if con1 and con2 and con3 and con4 and con5 and con6 and cursor14:
                input103['state'] = 'disabled'
                input203['state'] = 'disabled'
                input303['state'] = 'disabled'
                input403['state'] = 'disabled'
                input503['state'] = 'disabled'
                input603['state'] = 'disabled'
                                
                sched13.configure(text = "Cancel Appointment")
                sched13.configure(hover_color = "red", fg_color = "dark red")
                table14.configure(text = f"""
*Room 310
*{con1}
*{con3}
        """)
                table14.configure(hover_color = "red", fg_color = "dark red")
                net.commit()
                net.close()
        else:
            input103['state'] = 'enabled'
            input203['state'] = 'enabled'
            input303['state'] = 'enabled'
            input403['state'] = 'enabled'
            input503['state'] = 'enabled'
            input603['state'] = 'enabled'

            sched13.configure(text = 'Reserve!')
            sched13.configure(hover_color = "green", fg_color = "dark green")
            table14.configure(text = """
*Room 310
*Available
                    """)
            table14.configure(hover_color = "green", fg_color = "dark green")
            
    else:
        if saved13:
            if con1 and con2 and con3 and con4 and con5 and con6:
                input103['state'] = 'disabled'
                input203['state'] = 'disabled'
                input303['state'] = 'disabled'
                input403['state'] = 'disabled'
                input503['state'] = 'disabled'
                input603['state'] = 'disabled'
                sched13.configure(hover_color = "red", fg_color = "dark red")
                sched13.configure(text = "Email President/Rep")
                table14.configure(text = f"""
*Room 310
*{con1}
*{con3}
        """)
                table14.configure(hover_color = "red", fg_color = "dark red")

        else:
                input103['state'] = 'disabled'
                input203['state'] = 'disabled'
                input303['state'] = 'disabled'
                input403['state'] = 'disabled'
                input503['state'] = 'disabled'
                input603['state'] = 'disabled'
                

#=============================================================================================================================================================================================================#

net = sqlite3.connect("C:/Users/Windows 10/Documents/Python/1_Final Projects/Room_Accounts.db")
cursor = net.cursor()


#DATABASE
currenttheme = "darkly"
#main window name is 'window'
window = ttk.Window(themename = currenttheme)
window.title("Room Management System")

#makes the logo of the app visible on the taskbar
import ctypes
myappid ='mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#makes the logo of the app visible on the window
window.iconbitmap('C:/Users/Windows 10/Documents/Python/1_Final Projects/PUPlogo.ico')
window.geometry("1920x1080")#size of the window


#main bg image of the window
bg = Image.open("C:/Users/Windows 10/Documents/Python/1_Final Projects/loginbg.png")
resize = bg.resize((1920, 1080), Image.LANCZOS)
pic = ImageTk.PhotoImage(resize)
bg1 = Label(master = window, image=pic)
bg1.pack(pady=20)
bg1.place(x=0, y=0, relwidth=1, relheight=1)

mainint = Image.open("C:/Users/Windows 10/Documents/Python/1_Final Projects/MainInt.png")
size = mainint.resize((1920, 1000), Image.LANCZOS)
pics = ImageTk.PhotoImage(size)
bg2 = Label(master = window, image=pics)


#PUP logo on the side of the login page

#makes sure that the app is windowed fullscreen
window.state("zoomed")


#colors the login widget look reddish
frame1 = ctk.CTkFrame(window,corner_radius=0,fg_color='#701D25', height=1080,width=500)
pywinstyles.set_opacity(frame1, value=0.9)
#login widgets (master is basically the main grouper of the widgets, usually a frame or window)

lgfile="C:/Users/Windows 10/Documents/Python/1_Final Projects/PUP_re1.png"
loginmainlogo= ctk.CTkImage(dark_image = Image.open("C:/Users/Windows 10/Documents/Python/1_Final Projects/PUP_re1.png"), size = (130, 130))
looogooo = ctk.CTkLabel(master = frame1, image = loginmainlogo, text="")
looogooo.pack(pady=20, anchor='n')

Main = ctk.CTkLabel(frame1, text="""Polytechnic University of the Philippines
Room Management System""",font=ctk.CTkFont(family="Times New Roman",size=20))
Main.pack(anchor='n',pady=30,padx=40)


#label for texts and images
error1 = ctk.CTkLabel(master = frame1, 
                   text = "Incorrect Username or Password", 
                   font = ctk.CTkFont(family='Arial', size=15))

head1 = ctk.CTkLabel(master = frame1, text = "Webmail:",font=ctk.CTkFont(family='Arial', size=15)).pack(pady=10)
entry = ctk.CTkEntry(master = frame1, width=350,placeholder_text="Enter your Webmail")
entry.pack()


#entries are long ahh widgets that users can input data on, functions for them are on top.

head2 = ctk.CTkLabel(frame1, text="Password:", font=ctk.CTkFont(family='Arial',size=15))
head2.pack(pady=5, anchor='n')

entry1 = ctk.CTkEntry(frame1, placeholder_text="Enter your password", show="*",width=350)
entry1.pack(pady = 5, anchor='n')


button = ctk.CTkButton(master = frame1, hover_color = "green", fg_color = "dark green", text = "Login", command = login)
button.pack(pady = 10)

close = ctk.CTkButton(master = frame1, hover_color = "red", fg_color = "dark red", text = "Close", command = window.destroy)
close.pack()


prep = ctk.CTkLabel(master = frame1, text='Prepared by: Javanese', font=ctk.CTkFont(family="Arial",size=15))
prep.pack(pady = 20, anchor = "n")

frame1.pack(fill='y', expand='False', side='right')

#################################################################################################################

frame2 = ttk.Frame()
#0000000000000000000000000000000000000000000000#

sett = ctk.CTkFrame(master = window, height=2000,
                    width=1000, border_color = 'purple',
                    border_width = 3 ,corner_radius = 0)

sidelogo = ctk.CTkImage(dark_image = Image.open("C:/Users/Windows 10/Documents/Python/1_Final Projects/PUP_re1.png"), size = (100, 100))
logo_2 = ctk.CTkLabel(master = sett, image = sidelogo, text="")
logo_2.pack(padx = 10, pady = 10, anchor = 'n', side = 'right')

creds = ctk.CTkFrame(master = sett)

opt_back = ctk.CTkButton(master = creds, text = 'Back', width = 120, command = settback)
opt_back.pack(pady = 10)

About_Us = ctk.CTkButton(master = creds, text = 'About Javanese', width = 120, command = about)
About_Us.pack()

log_out = ctk.CTkButton(master = creds, text = "Sign out", width= 120, hover_color = "red", fg_color = "dark red", command = logoff1)
log_out.pack(pady = 10)

creds.pack(padx = 10, pady = 10, anchor = 'n', side = 'left')

mainwidgetsett = ctk.CTkLabel(master = sett, text = "Options", font = ('Arial', 20))
mainwidgetsett.pack(pady = 10)

account_settings = ttk.Frame(master = sett)

chmail = ttk.Label(master = account_settings, text = "PUP Webmail")
chmail.pack(pady = 10)

instmail = ttk.Entry(master = account_settings, width = 50)
instmail.pack()

chpass = ttk.Label(master = account_settings, text = "Password")
chpass.pack(pady = 10)

instpass = ttk.Entry(master = account_settings, width = 50)
instpass.pack()

change_pass = ctk.CTkButton(master = account_settings, text = 'Change Password', hover_color = "red", fg_color = "dark red", command = look)
change_pass.pack(pady = 10)

password_changed = ctk.CTkLabel(master = account_settings, text = "Password Changed")


account_settings.pack(pady=100, anchor = 'center')

devs = ctk.CTkLabel(master = sett, text = """
Group Javanese, All rights reserved

Team Leader Email: victorianobabenaiii@iskolarngbayan.pup.edu.ph""")
devs.pack(pady = 10, side = 'bottom')

#0000000000000000000000000000000000000000000000#
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

floorswitch = Image.open("C:/Users/Windows 10/Documents/Python/1_Final Projects/floor_switch.png")
floorswitchsize = floorswitch.resize((1920, 784), Image.LANCZOS)
floorpic = ImageTk.PhotoImage(floorswitchsize)
frame2_bg = Label(master = frame2, image=floorpic)
frame2_bg.pack(pady=20)
frame2_bg.place(x=0, y=0, relwidth=1, relheight=1)

Hed = ttk.Label(master = frame2, text = "===Available Rooms===",
                font = "Arial 15 bold")
Hed.pack(anchor = 'center')

floorbuttons = ttk.Frame(master = frame2)
floors = ctk.CTkButton(master = floorbuttons, text = "Floors", width = 80,  hover_color = "#0078d4", fg_color = "#0078d4")
floors.pack(pady = 10)

fl3 = ctk.CTkButton(master = floorbuttons, text = "3", width= 30, command = switch2)
fl3.pack(anchor = 'center', side = 'right', padx = 5)

fl2 = ctk.CTkButton(master = floorbuttons, text = "2",  width= 30, command = switch1)
fl2.pack(anchor = 'center', side = 'right')

floorbuttons.pack(padx = 10, anchor = 'n', side = 'right')

sidelogo1 = Image.open("C:/Users/Windows 10/Documents/Python/1_Final Projects/PUP_re1.png")
sdlg1 = sidelogo1.resize((150, 150), Image.LANCZOS)
logo3 = ImageTk.PhotoImage(sdlg1)
logo_3 = Label(master = frame2, image = logo3)
logo_3.pack(padx = 10, anchor = 'n', side = 'left')

functions = ttk.Frame(master = frame2)

option = ctk.CTkButton(master = functions, text = 'Options', width= 50, command = settings)
option.pack(pady = 10)

button1 = ctk.CTkButton(master = functions, text = "Sign out", width= 50, hover_color = "red", fg_color = "dark red", command = logoff)
button1.pack(pady = 10)

functions.pack(ipadx = 10, anchor = 'n', side = 'left')
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

meettheteam = ctk.CTkScrollableFrame (master = window, 
                                      orientation = "vertical",
                                      width = 1920,
                                      height = 1080)

aboutus1 = Image.open("C:/Users/Windows 10/Documents/Python/1_Final Projects/1.png")
changesize1 = aboutus1.resize((1920, 1080), Image.LANCZOS)
bout = ImageTk.PhotoImage(changesize1)
abtus = Label(master = meettheteam, image=bout)
abtus.pack(pady=20)


aboutus2 = Image.open("C:/Users/Windows 10/Documents/Python/1_Final Projects/2.png")
changesize2 = aboutus2.resize((1920, 1080), Image.LANCZOS)
bout1 = ImageTk.PhotoImage(changesize2)
abtus1 = Label(master = meettheteam, image=bout1)
abtus1.pack(pady=20)


aboutus3 = Image.open("C:/Users/Windows 10/Documents/Python/1_Final Projects/3.png")
changesize3 = aboutus3.resize((1920, 1080), Image.LANCZOS)
bout2 = ImageTk.PhotoImage(changesize3)
abtus2 = Label(master = meettheteam, image=bout2)
abtus2.pack(pady=20)

close_about_us = ctk.CTkButton(master = meettheteam, text = "Return to settings", command = leaveabout)
close_about_us.pack()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++@
floor2 = ttk.Frame(master = frame2)

tab_1 = ttk.Frame(master = floor2)
table1 = ctk.CTkButton(master = tab_1,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 201
*Available
                    """,
                    command = Avail)
table1.pack(ipadx= 20, ipady= 20)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
table2 = ctk.CTkButton(master = tab_1,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 202
*Available
                    """,
                    command = Avail1)
table2.pack(pady = 30, ipadx= 20, ipady= 20)

tab_1.pack(padx = 20, side = 'left')
State = "Available"

#====================================================================#
tab_2 = ttk.Frame(master = floor2)
table3 = ctk.CTkButton(master = tab_2,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 203
*Available
                    """,
                    command = Avail2)
table3.pack(ipadx= 20, ipady= 20)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
table4 = ctk.CTkButton(master = tab_2,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 204
*Available
                    """,
                    command = Avail3)
table4.pack(pady = 30, ipadx= 20, ipady= 20)

tab_2.pack(padx =20, side = 'left')

State = "Available"
#====================================================================#
tab_3 = ttk.Frame(master = floor2)

lib1 = ctk.CTkButton(master = tab_3,
                    hover_color = "dark gray", fg_color = "gray", 
                    text = """
*   Main 
  Library 1
                    """,
                    )
lib1.pack(ipadx= 20, ipady= 20)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
table5 = ctk.CTkButton(master = tab_3,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 206
*Available
                    """,
                    command = Avail4)
table5.pack(pady =30, ipadx= 20, ipady= 20)

tab_3.pack(padx =20, side = 'left')

State = "Available"
#====================================================================#
tab_4 = ttk.Frame(master = floor2)
lib2 = ctk.CTkButton(master = tab_4,
                    hover_color = "dark gray", fg_color = "gray", 
                    text = """
*   Main 
  Library 2
                    """
                    )
lib2.pack(ipadx= 20, ipady= 20)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
table6 = ctk.CTkButton(master = tab_4,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 208
*Available
                    """,
                    command = Avail5)
table6.pack(pady = 30, ipadx= 20, ipady= 20)

tab_4.pack(padx =20, side = 'left')

State = "Available"
#====================================================================#
tab_5 = ttk.Frame(master = floor2)
conf = ctk.CTkButton(master = tab_5,
                    hover_color = "dark gray", fg_color = "gray", 
                    text = """
*   Conference
       Room
                    """
                    )
conf.pack(ipadx= 20, ipady= 20)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
table7 = ctk.CTkButton(master = tab_5,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 210
*Available
                    """,
                    command = Avail6)
table7.pack(pady = 30, ipadx= 20, ipady= 20)

tab_5.pack(padx =20, side = 'left')

State = "Available"
#====================================================================#

floor2.pack(pady = 150, anchor = 's', side = 'bottom')

#?????????????????????????????????????????????????????????????????????#

floor3 = ttk.Frame(master = frame2)

tab_6 = ttk.Frame(master = floor3)
table8 = ctk.CTkButton(master = tab_6,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 301
*Available
                    """,
                    command = Avail7)
table8.pack(ipadx= 20, ipady= 20)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
Lab1 = ctk.CTkButton(master = tab_6,
                    hover_color = "dark gray", fg_color = "gray", 
                    text = """
*   Science
   Laboratory
                    """
                    )
Lab1.pack(pady = 30, ipadx= 20, ipady= 20)

tab_6.pack(padx =20, side = 'left')

State = "Available"
#====================================================================#
tab_7 = ttk.Frame(master = floor3)
table9 = ctk.CTkButton(master = tab_7,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 303
*Available
                    """,
                    command = Avail8)
table9.pack(ipadx= 20, ipady= 20)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
Lab2 = ctk.CTkButton(master = tab_7,
                    hover_color = "dark gray", fg_color = "gray", 
                    text = """
*   Science
  Laboratory II
                    """
                    )
Lab2.pack(pady = 30, ipadx= 20, ipady= 20)

tab_7.pack(padx =20, side = 'left')

State = "Available"
#====================================================================#
tab_8 = ttk.Frame(master = floor3)
table10 = ctk.CTkButton(master = tab_8,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 305
*Available
                    """,
                    command = Avail9)
table10.pack(ipadx= 20, ipady= 20)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
table11 = ctk.CTkButton(master = tab_8,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 306
*Available
                    """,
                    command = Avail10)
table11.pack(pady = 30, ipadx= 20, ipady= 20)

tab_8.pack(padx =20, side = 'left')

State = "Available"
#====================================================================#
tab_9 = ttk.Frame(master = floor3)
table12 = ctk.CTkButton(master = tab_9,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 307
*Available
                    """,
                    command = Avail11)
table12.pack(ipadx= 20, ipady= 20)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
table13 = ctk.CTkButton(master = tab_9,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 308
*Available
                    """,
                    command = Avail12)
table13.pack(pady = 30, ipadx= 20, ipady= 20)

tab_9.pack(padx =20, side = 'left')

State = "Available"
#====================================================================#
tab_10 = ttk.Frame(master = floor3)
keeb = ctk.CTkButton(master = tab_10,
                    hover_color = "dark gray", fg_color = "gray", 
                    text = """
*Keyboarding
 Laboratory
                    """
                    )
keeb.pack(ipadx= 20, ipady= 20)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
table14 = ctk.CTkButton(master = tab_10,
                    hover_color = "green", fg_color = "dark green", 
                    text = """
*Room 310
*Available
                    """,
                    command = Avail13)
table14.pack(pady = 30, ipadx= 20, ipady= 20)

tab_10.pack(padx =20, side = 'left')

State = "Available"
#====================================================================#

tableavail = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail, text = "Return back", command = back)
ret.pack(pady = 10)

# FLOOR 201
cursor1 = net.cursor()
cursor1.execute('SELECT * FROM Rooms WHERE Room_Number = 201')
saved = cursor1.fetchone()

Info = ttk.Label(master = tableavail, text = "Program, Year & Section: ").pack()
input1 = ttk.Entry(master = tableavail, width = 50)
input1.pack(pady = 10)
if saved:
    input1.insert(0, saved[1])

prof = ttk.Label(master = tableavail, text = "Professor: ").pack()
input2 = ttk.Entry(master = tableavail, width = 50)
input2.pack(pady = 10)
if saved:
    input2.insert(0, saved[2])

time = ttk.Label(master = tableavail, text = "Time: ").pack()
input3 = ttk.Entry(master = tableavail, width = 50)
input3.pack(pady = 10)
if saved:
    input3.insert(0, saved[3])

date = ttk.Label(master = tableavail, text = "Date: ").pack()
input4 = ttk.Entry(master = tableavail, width = 50)
input4.pack(pady = 10)
if saved:
    input4.insert(0, saved[4])

Act = ttk.Label(master = tableavail, text = "Activity: ").pack()
input5 = ttk.Entry(master = tableavail, width = 50)
input5.pack(pady = 10)
if saved:
    input5.insert(0, saved[5])

rep = ttk.Label(master = tableavail, text = "Class President/Rep: ").pack()
input6 = ttk.Entry(master = tableavail, width = 50)
input6.pack(pady = 10)
if saved:
    input6.insert(0, saved[6])

sched = ctk.CTkButton(master = tableavail, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv)
sched.pack(pady = 10)

clear = ctk.CTkButton(master = tableavail, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe)
clear.pack(pady = 10)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

cursor2 = net.cursor()
cursor2.execute('SELECT * FROM Rooms WHERE Room_Number = 202')
saved1 = cursor2.fetchone()

tableavail1 = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail1, text = "Return back", command = back1)
ret.pack(pady = 10)

Info = ttk.Label(master = tableavail1, text = "Program, Year & Section: ").pack()
input11 = ttk.Entry(master = tableavail1, width = 50)
input11.pack(pady = 10)
if saved1:
    input11.insert(0, saved1[1])

prof = ttk.Label(master = tableavail1, text = "Professor: ").pack()
input21 = ttk.Entry(master = tableavail1, width = 50)
input21.pack(pady = 10)
if saved1:
    input21.insert(0, saved1[2])

time = ttk.Label(master = tableavail1, text = "Time: ").pack()
input31 = ttk.Entry(master = tableavail1, width = 50)
input31.pack(pady = 10)
if saved1:
    input31.insert(0, saved1[3])

date = ttk.Label(master = tableavail1, text = "Date: ").pack()
input41 = ttk.Entry(master = tableavail1, width = 50)
input41.pack(pady = 10)
if saved1:
    input41.insert(0, saved1[4])

Act = ttk.Label(master = tableavail1, text = "Activity: ").pack()
input51 = ttk.Entry(master = tableavail1, width = 50)
input51.pack(pady = 10)
if saved1:
    input51.insert(0, saved1[5])

rep = ttk.Label(master = tableavail1, text = "Class President/Rep: ").pack()
input61 = ttk.Entry(master = tableavail1, width = 50)
input61.pack(pady = 10)
if saved1:
    input61.insert(0, saved1[6])

sched1 = ctk.CTkButton(master = tableavail1, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv1)
sched1.pack(pady = 10)

clear1 = ctk.CTkButton(master = tableavail1, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe1)
clear1.pack(pady=10)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

cursor3 = net.cursor()
cursor3.execute('SELECT * FROM Rooms WHERE Room_Number = 203')
saved2 = cursor3.fetchone()

tableavail2 = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail2, text = "Return back", command = back2)
ret.pack(pady = 10)

Info = ttk.Label(master = tableavail2, text = "Program, Year & Section: ").pack()
input12 = ttk.Entry(master = tableavail2, width = 50)
input12.pack(pady = 10)
if saved2:
    input12.insert(0, saved2[1])

prof = ttk.Label(master = tableavail2, text = "Professor: ").pack()
input22 = ttk.Entry(master = tableavail2, width = 50)
input22.pack(pady = 10)
if saved2:
    input22.insert(0, saved2[2])

time = ttk.Label(master = tableavail2, text = "Time: ").pack()
input32 = ttk.Entry(master = tableavail2, width = 50)
input32.pack(pady = 10)
if saved2:
    input32.insert(0, saved2[3])

date = ttk.Label(master = tableavail2, text = "Date: ").pack()
input42 = ttk.Entry(master = tableavail2, width = 50)
input42.pack(pady = 10)
if saved2:
    input42.insert(0, saved2[4])

Act = ttk.Label(master = tableavail2, text = "Activity: ").pack()
input52 = ttk.Entry(master = tableavail2, width = 50)
input52.pack(pady = 10)
if saved2:
    input52.insert(0, saved2[5])

rep = ttk.Label(master = tableavail2, text = "Class President/Rep: ").pack()
input62 = ttk.Entry(master = tableavail2, width = 50)
input62.pack(pady = 10)
if saved2:
    input62.insert(0, saved2[6])

sched2 = ctk.CTkButton(master = tableavail2, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv2)
sched2.pack(pady = 10)

clear2 = ctk.CTkButton(master = tableavail2, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe2)
clear2.pack(pady=10)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

cursor4 = net.cursor()
cursor4.execute('SELECT * FROM Rooms WHERE Room_Number = 204')
saved3 = cursor4.fetchone()

tableavail3 = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail3, text = "Return back", command = back3)
ret.pack(pady = 10)

Info = ttk.Label(master = tableavail3, text = "Program, Year & Section: ").pack()
input13 = ttk.Entry(master = tableavail3, width = 50)
input13.pack(pady = 10)
if saved3:
    input13.insert(0, saved3[1])

prof = ttk.Label(master = tableavail3, text = "Professor: ").pack()
input23 = ttk.Entry(master = tableavail3, width = 50)
input23.pack(pady = 10)
if saved3:
    input23.insert(0, saved3[2])

time = ttk.Label(master = tableavail3, text = "Time: ").pack()
input33 = ttk.Entry(master = tableavail3, width = 50)
input33.pack(pady = 10)
if saved3:
    input33.insert(0, saved3[3])

date = ttk.Label(master = tableavail3, text = "Date: ").pack()
input43 = ttk.Entry(master = tableavail3, width = 50)
input43.pack(pady = 10)
if saved3:
    input43.insert(0, saved3[4])

Act = ttk.Label(master = tableavail3, text = "Activity: ").pack()
input53 = ttk.Entry(master = tableavail3, width = 50)
input53.pack(pady = 10)
if saved3:
    input53.insert(0, saved3[5])

rep = ttk.Label(master = tableavail3, text = "Class President/Rep: ").pack()
input63 = ttk.Entry(master = tableavail3, width = 50)
input63.pack(pady = 10)
if saved3:
    input63.insert(0, saved3[6])

sched3 = ctk.CTkButton(master = tableavail3, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv3)
sched3.pack(pady = 10)

clear3 = ctk.CTkButton(master = tableavail3, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe3)
clear3.pack(pady=10) 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

cursor5 = net.cursor()
cursor5.execute('SELECT * FROM Rooms WHERE Room_Number = 206')
saved4 = cursor5.fetchone()

tableavail4 = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail4, text = "Return back", command = back4)
ret.pack(pady = 10)

Info = ttk.Label(master = tableavail4, text = "Program, Year & Section: ").pack()
input14 = ttk.Entry(master = tableavail4, width = 50)
input14.pack(pady = 10)
if saved4:
    input14.insert(0, saved4[1])

prof = ttk.Label(master = tableavail4, text = "Professor: ").pack()
input24 = ttk.Entry(master = tableavail4, width = 50)
input24.pack(pady = 10)
if saved4:
    input24.insert(0, saved4[2])

time = ttk.Label(master = tableavail4, text = "Time: ").pack()
input34 = ttk.Entry(master = tableavail4, width = 50)
input34.pack(pady = 10)
if saved4:
    input34.insert(0, saved4[3])

date = ttk.Label(master = tableavail4, text = "Date: ").pack()
input44 = ttk.Entry(master = tableavail4, width = 50)
input44.pack(pady = 10)
if saved4:
    input44.insert(0, saved4[4])

Act = ttk.Label(master = tableavail4, text = "Activity: ").pack()
input54 = ttk.Entry(master = tableavail4, width = 50)
input54.pack(pady = 10)
if saved4:
    input54.insert(0, saved4[5])

rep = ttk.Label(master = tableavail4, text = "Class President/Rep: ").pack()
input64 = ttk.Entry(master = tableavail4, width = 50)
input64.pack(pady = 10)
if saved4:
    input64.insert(0, saved4[6])

sched4 = ctk.CTkButton(master = tableavail4, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv4)
sched4.pack(pady = 10)

clear4 = ctk.CTkButton(master = tableavail4, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe4)
clear4.pack(pady=10) 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

cursor6 = net.cursor()
cursor6.execute('SELECT * FROM Rooms WHERE Room_Number = 208')
saved5 = cursor6.fetchone()

tableavail5 = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail5, text = "Return back", command = back5)
ret.pack(pady = 10)

Info = ttk.Label(master = tableavail5, text = "Program, Year & Section: ").pack()
input15 = ttk.Entry(master = tableavail5, width = 50)
input15.pack(pady = 10)
if saved5:
    input15.insert(0, saved5[1])

prof = ttk.Label(master = tableavail5, text = "Professor: ").pack()
input25 = ttk.Entry(master = tableavail5, width = 50)
input25.pack(pady = 10)
if saved5:
    input25.insert(0, saved5[2])

time = ttk.Label(master = tableavail5, text = "Time: ").pack()
input35 = ttk.Entry(master = tableavail5, width = 50)
input35.pack(pady = 10)
if saved5:
    input35.insert(0, saved5[3])

date = ttk.Label(master = tableavail5, text = "Date: ").pack()
input45 = ttk.Entry(master = tableavail5, width = 50)
input45.pack(pady = 10)
if saved5:
    input45.insert(0, saved5[4])

Act = ttk.Label(master = tableavail5, text = "Activity: ").pack()
input55 = ttk.Entry(master = tableavail5, width = 50)
input55.pack(pady = 10)
if saved5:
    input55.insert(0, saved5[5])

rep = ttk.Label(master = tableavail5, text = "Class President/Rep: ").pack()
input65 = ttk.Entry(master = tableavail5, width = 50)
input65.pack(pady = 10)
if saved5:
    input65.insert(0, saved5[6])

sched5 = ctk.CTkButton(master = tableavail5, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv5)
sched5.pack(pady = 10)

clear5 = ctk.CTkButton(master = tableavail5, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe5)
clear5.pack(pady=10) 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

cursor7 = net.cursor()
cursor7.execute('SELECT * FROM Rooms WHERE Room_Number = 210')
saved6 = cursor7.fetchone()

tableavail6 = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail6, text = "Return back", command = back6)
ret.pack(pady = 10)

Info = ttk.Label(master = tableavail6, text = "Program, Year & Section: ").pack()
input16 = ttk.Entry(master = tableavail6, width = 50)
input16.pack(pady = 10)
if saved6:
    input16.insert(0, saved6[1])

prof = ttk.Label(master = tableavail6, text = "Professor: ").pack()
input26 = ttk.Entry(master = tableavail6, width = 50)
input26.pack(pady = 10)
if saved6:
    input26.insert(0, saved6[2])

time = ttk.Label(master = tableavail6, text = "Time: ").pack()
input36 = ttk.Entry(master = tableavail6, width = 50)
input36.pack(pady = 10)
if saved6:
    input36.insert(0, saved6[3])

date = ttk.Label(master = tableavail6, text = "Date: ").pack()
input46 = ttk.Entry(master = tableavail6, width = 50)
input46.pack(pady = 10)
if saved6:
    input46.insert(0, saved6[4])

Act = ttk.Label(master = tableavail6, text = "Activity: ").pack()
input56 = ttk.Entry(master = tableavail6, width = 50)
input56.pack(pady = 10)
if saved6:
    input56.insert(0, saved6[5])

rep = ttk.Label(master = tableavail6, text = "Class President/Rep: ").pack()
input66 = ttk.Entry(master = tableavail6, width = 50)
input66.pack(pady = 10)
if saved6:
    input66.insert(0, saved6[6])

sched6 = ctk.CTkButton(master = tableavail6, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv6)
sched6.pack(pady = 10)

clear6 = ctk.CTkButton(master = tableavail6, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe6)
clear6.pack(pady=10) 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#FLOOR 3

cursor8 = net.cursor()
cursor8.execute('SELECT * FROM Rooms WHERE Room_Number = 301')
saved7 = cursor8.fetchone()

tableavail7 = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail7, text = "Return back", command = back7)
ret.pack(pady = 10)

Info = ttk.Label(master = tableavail7, text = "Program, Year & Section: ").pack()
input17 = ttk.Entry(master = tableavail7, width = 50)
input17.pack(pady = 10)
if saved7:
    input17.insert(0, saved7[1])

prof = ttk.Label(master = tableavail7, text = "Professor: ").pack()
input27 = ttk.Entry(master = tableavail7, width = 50)
input27.pack(pady = 10)
if saved7:
    input27.insert(0, saved7[2])

time = ttk.Label(master = tableavail7, text = "Time: ").pack()
input37 = ttk.Entry(master = tableavail7, width = 50)
input37.pack(pady = 10)
if saved7:
    input37.insert(0, saved7[3])

date = ttk.Label(master = tableavail7, text = "Date: ").pack()
input47 = ttk.Entry(master = tableavail7, width = 50)
input47.pack(pady = 10)
if saved7:
    input47.insert(0, saved7[4])

Act = ttk.Label(master = tableavail7, text = "Activity: ").pack()
input57 = ttk.Entry(master = tableavail7, width = 50)
input57.pack(pady = 10)
if saved7:
    input57.insert(0, saved7[5])

rep = ttk.Label(master = tableavail7, text = "Class President/Rep: ").pack()
input67 = ttk.Entry(master = tableavail7, width = 50)
input67.pack(pady = 10)
if saved7:
    input67.insert(0, saved7[6])

sched7 = ctk.CTkButton(master = tableavail7, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv7)
sched7.pack(pady = 10)

clear7 = ctk.CTkButton(master = tableavail7, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe7)
clear7.pack(pady=10) 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

cursor9 = net.cursor()
cursor9.execute('SELECT * FROM Rooms WHERE Room_Number = 303')
saved8 = cursor9.fetchone()

tableavail8 = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail8, text = "Return back", command = back8)
ret.pack(pady = 10)

Info = ttk.Label(master = tableavail8, text = "Program, Year & Section: ").pack()
input18 = ttk.Entry(master = tableavail8, width = 50)
input18.pack(pady = 10)
if saved8:
    input18.insert(0, saved8[1])

prof = ttk.Label(master = tableavail8, text = "Professor: ").pack()
input28 = ttk.Entry(master = tableavail8, width = 50)
input28.pack(pady = 10)
if saved8:
    input28.insert(0, saved8[2])

time = ttk.Label(master = tableavail8, text = "Time: ").pack()
input38 = ttk.Entry(master = tableavail8, width = 50)
input38.pack(pady = 10)
if saved8:
    input38.insert(0, saved8[3])

date = ttk.Label(master = tableavail8, text = "Date: ").pack()
input48 = ttk.Entry(master = tableavail8, width = 50)
input48.pack(pady = 10)
if saved8:
    input48.insert(0, saved8[4])

Act = ttk.Label(master = tableavail8, text = "Activity: ").pack()
input58 = ttk.Entry(master = tableavail8, width = 50)
input58.pack(pady = 10)
if saved8:
    input58.insert(0, saved8[5])

rep = ttk.Label(master = tableavail8, text = "Class President/Rep: ").pack()
input68 = ttk.Entry(master = tableavail8, width = 50)
input68.pack(pady = 10)
if saved8:
    input68.insert(0, saved8[6])

sched8 = ctk.CTkButton(master = tableavail8, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv8)
sched8.pack(pady = 10)

clear8 = ctk.CTkButton(master = tableavail8, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe8)
clear8.pack(pady=10) 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

cursor10 = net.cursor()
cursor10.execute('SELECT * FROM Rooms WHERE Room_Number = 305')
saved9 = cursor10.fetchone()

tableavail9 = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail9, text = "Return back", command = back9)
ret.pack(pady = 10)

Info = ttk.Label(master = tableavail9, text = "Program, Year & Section: ").pack()
input19 = ttk.Entry(master = tableavail9, width = 50)
input19.pack(pady = 10)
if saved9:
    input19.insert(0, saved9[1])

prof = ttk.Label(master = tableavail9, text = "Professor: ").pack()
input29 = ttk.Entry(master = tableavail9, width = 50)
input29.pack(pady = 10)
if saved9:
    input29.insert(0, saved9[2])

time = ttk.Label(master = tableavail9, text = "Time: ").pack()
input39 = ttk.Entry(master = tableavail9, width = 50)
input39.pack(pady = 10)
if saved9:
    input39.insert(0, saved9[3])

date = ttk.Label(master = tableavail9, text = "Date: ").pack()
input49 = ttk.Entry(master = tableavail9, width = 50)
input49.pack(pady = 10)
if saved9:
    input49.insert(0, saved9[4])

Act = ttk.Label(master = tableavail9, text = "Activity: ").pack()
input59 = ttk.Entry(master = tableavail9, width = 50)
input59.pack(pady = 10)
if saved9:
    input59.insert(0, saved9[5])

rep = ttk.Label(master = tableavail9, text = "Class President/Rep: ").pack()
input69 = ttk.Entry(master = tableavail9, width = 50)
input69.pack(pady = 10)
if saved9:
    input69.insert(0, saved9[6])

sched9 = ctk.CTkButton(master = tableavail9, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv9)
sched9.pack(pady = 10)

clear9 = ctk.CTkButton(master = tableavail9, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe9)
clear9.pack(pady=10) 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

cursor11 = net.cursor()
cursor11.execute('SELECT * FROM Rooms WHERE Room_Number = 306')
saved10 = cursor11.fetchone()

tableavail10 = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail10, text = "Return back", command = back10)
ret.pack(pady = 10)

Info = ttk.Label(master = tableavail10, text = "Program, Year & Section: ").pack()
input10 = ttk.Entry(master = tableavail10, width = 50)
input10.pack(pady = 10)
if saved10:
    input10.insert(0, saved10[1])

prof = ttk.Label(master = tableavail10, text = "Professor: ").pack()
input20 = ttk.Entry(master = tableavail10, width = 50)
input20.pack(pady = 10)
if saved10:
    input20.insert(0, saved10[2])

time = ttk.Label(master = tableavail10, text = "Time: ").pack()
input30 = ttk.Entry(master = tableavail10, width = 50)
input30.pack(pady = 10)
if saved10:
    input30.insert(0, saved10[3])

date = ttk.Label(master = tableavail10, text = "Date: ").pack()
input40 = ttk.Entry(master = tableavail10, width = 50)
input40.pack(pady = 10)
if saved10:
    input40.insert(0, saved10[4])

Act = ttk.Label(master = tableavail10, text = "Activity: ").pack()
input50 = ttk.Entry(master = tableavail10, width = 50)
input50.pack(pady = 10)
if saved10:
    input50.insert(0, saved10[5])

rep = ttk.Label(master = tableavail10, text = "Class President/Rep: ").pack()
input60 = ttk.Entry(master = tableavail10, width = 50)
input60.pack(pady = 10)
if saved10:
    input60.insert(0, saved10[6])

sched10 = ctk.CTkButton(master = tableavail10, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv10)
sched10.pack(pady = 10)

clear10 = ctk.CTkButton(master = tableavail10, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe10)
clear10.pack(pady=10) 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

cursor12 = net.cursor()
cursor12.execute('SELECT * FROM Rooms WHERE Room_Number = 307')
saved11 = cursor12.fetchone()

tableavail11 = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail11, text = "Return back", command = back11)
ret.pack(pady = 10)

Info = ttk.Label(master = tableavail11, text = "Program, Year & Section: ").pack()
input101 = ttk.Entry(master = tableavail11, width = 50)
input101.pack(pady = 10)
if saved11:
    input101.insert(0, saved11[1])

prof = ttk.Label(master = tableavail11, text = "Professor: ").pack()
input201 = ttk.Entry(master = tableavail11, width = 50)
input201.pack(pady = 10)
if saved11:
    input201.insert(0, saved11[2])

time = ttk.Label(master = tableavail11, text = "Time: ").pack()
input301 = ttk.Entry(master = tableavail11, width = 50)
input301.pack(pady = 10)
if saved11:
    input301.insert(0, saved11[3])

date = ttk.Label(master = tableavail11, text = "Date: ").pack()
input401 = ttk.Entry(master = tableavail11, width = 50)
input401.pack(pady = 10)
if saved11:
    input401.insert(0, saved11[4])

Act = ttk.Label(master = tableavail11, text = "Activity: ").pack()
input501 = ttk.Entry(master = tableavail11, width = 50)
input501.pack(pady = 10)
if saved11:
    input501.insert(0, saved11[5])

rep = ttk.Label(master = tableavail11, text = "Class President/Rep: ").pack()
input601 = ttk.Entry(master = tableavail11, width = 50)
input601.pack(pady = 10)
if saved11:
    input601.insert(0, saved11[6])

sched11 = ctk.CTkButton(master = tableavail11, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv11)
sched11.pack(pady = 10)

clear11 = ctk.CTkButton(master = tableavail11, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe11)
clear11.pack(pady=10) 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

cursor13 = net.cursor()
cursor13.execute('SELECT * FROM Rooms WHERE Room_Number = 308')
saved12 = cursor13.fetchone()

tableavail12 = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail12, text = "Return back", command = back12)
ret.pack(pady = 10)

Info = ttk.Label(master = tableavail12, text = "Program, Year & Section: ").pack()
input102 = ttk.Entry(master = tableavail12, width = 50)
input102.pack(pady = 10)
if saved12:
    input102.insert(0, saved12[1])

prof = ttk.Label(master = tableavail12, text = "Professor: ").pack()
input202 = ttk.Entry(master = tableavail12, width = 50)
input202.pack(pady = 10)
if saved12:
    input202.insert(0, saved12[2])

time = ttk.Label(master = tableavail12, text = "Time: ").pack()
input302 = ttk.Entry(master = tableavail12, width = 50)
input302.pack(pady = 10)
if saved12:
    input302.insert(0, saved12[3])

date = ttk.Label(master = tableavail12, text = "Date: ").pack()
input402 = ttk.Entry(master = tableavail12, width = 50)
input402.pack(pady = 10)
if saved12:
    input402.insert(0, saved12[4])

Act = ttk.Label(master = tableavail12, text = "Activity: ").pack()
input502 = ttk.Entry(master = tableavail12, width = 50)
input502.pack(pady = 10)
if saved12:
    input502.insert(0, saved12[5])

rep = ttk.Label(master = tableavail12, text = "Class President/Rep: ").pack()
input602 = ttk.Entry(master = tableavail12, width = 50)
input602.pack(pady = 10)
if saved12:
    input602.insert(0, saved12[6])

sched12 = ctk.CTkButton(master = tableavail12, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv12)
sched12.pack(pady = 10)

clear12 = ctk.CTkButton(master = tableavail12, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe12)
clear12.pack(pady=10)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

cursor14 = net.cursor()
cursor14.execute('SELECT * FROM Rooms WHERE Room_Number = 310')
saved13 = cursor14.fetchone()

tableavail13 = ctk.CTkFrame(master = window, height=2000,
                       width=1000, border_color = 'purple',
                       border_width = 3 ,corner_radius = 0)
ret = ctk.CTkButton(master = tableavail13, text = "Return back", command = back13)
ret.pack(pady = 10)

Info = ttk.Label(master = tableavail13, text = "Program, Year & Section: ").pack()
input103 = ttk.Entry(master = tableavail13, width = 50)
input103.pack(pady = 10)
if saved13:
    input103.insert(0, saved13[1])

prof = ttk.Label(master = tableavail13, text = "Professor: ").pack()
input203 = ttk.Entry(master = tableavail13, width = 50)
input203.pack(pady = 10)
if saved13:
    input203.insert(0, saved13[2])

time = ttk.Label(master = tableavail13, text = "Time: ").pack()
input303 = ttk.Entry(master = tableavail13, width = 50)
input303.pack(pady = 10)
if saved13:
    input303.insert(0, saved13[3])

date = ttk.Label(master = tableavail13, text = "Date: ").pack()
input403 = ttk.Entry(master = tableavail13, width = 50)
input403.pack(pady = 10)
if saved13:
    input403.insert(0, saved13[4])

Act = ttk.Label(master = tableavail13, text = "Activity: ").pack()
input503 = ttk.Entry(master = tableavail13, width = 50)
input503.pack(pady = 10)
if saved13:
    input503.insert(0, saved13[5])

rep = ttk.Label(master = tableavail13, text = "Class President/Rep: ").pack()
input603 = ttk.Entry(master = tableavail13, width = 50)
input603.pack(pady = 10)
if saved13:
    input603.insert(0, saved13[6])

sched13 = ctk.CTkButton(master = tableavail13, hover_color = "green", fg_color = "dark green", text = "Reserve!", command = rsrv13)
sched13.pack(pady = 10)

clear13 = ctk.CTkButton(master = tableavail13, hover_color = "red", fg_color = "dark red", text = "Clear Text", command = wipe13)
clear13.pack(pady=10)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


net.commit()
#net.close()
window.mainloop()