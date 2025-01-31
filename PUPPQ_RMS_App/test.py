net = sqlite3.connect("Room_Accounts.db")
cursor = net.cursor()
cursor.execute("""CREATE TABLE Rooms (
               Room_Number integer primary key, 
               Program_Year_Section text, 
               Professor text, 
               Time text, 
               Date text, 
               Activity text, 
               Class_Rep text, 
               User text)""")
