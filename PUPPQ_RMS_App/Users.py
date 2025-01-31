import json
from Accs import Accounts
Accounts1 = '''[
    {
        'User':"Dabu, Shervan Nickolai Y.",
        'Name': "shervannickolaiydabu@iskolarngbayan.pup.edu.ph",
        'Password': '1010',
        'State': 1,
        'Rep':'mailto:noeneilicalpito@iskolarngbayan.pup.edu.ph?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out',
        'Repmail':'noeneilicalpito@iskolarngbayan.pup.edu.ph'
    },
    {
        'User':"Jimenez, James B.",
        'Name': "jamesbjimenez@iskolarngbayan.pup.edu.ph",
        'Password': "2020",
        'State': 0,
        'Rep':'mailto:noeneilicalpito@iskolarngbayan.pup.edu.ph?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out',
        'Repmail':'noeneilicalpito@iskolarngbayan.pup.edu.ph'
    },
    {
        'User':"Berry, Christopher P.",
        'Name': "christopherpberry@iskolarngbayan.pup.edu.ph",
        'Password': "3030",
        'State': 1,
        'Rep':'mailto:noeneilicalpito@iskolarngbayan.pup.edu.ph?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out',
        'Repmail':'noeneilicalpito@iskolarngbayan.pup.edu.ph'
    },
    {
        'User':"Abena, Victoriano B. III",
        'Name': "victorianobabenaiii@iskolarngbayan.pup.edu.ph",
        'Password': "4040",
        'State': 0,
        'Rep':'mailto:noeneilicalpito@iskolarngbayan.pup.edu.ph?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out',
        'Repmail':'noeneilicalpito@iskolarngbayan.pup.edu.ph'
    },
    {
        'User':"De leon, John Menard H.",
        'Name': "johnmenardhdeleon@iskolarngbayan.pup.edu.ph",
        'Password': "5050",
        'State': 1,
        'Rep':'mailto:noeneilicalpito@iskolarngbayan.pup.edu.ph?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out',
        'Repmail':'noeneilicalpito@iskolarngbayan.pup.edu.ph'
    },
    {
        'User':"Pueyo, Francesca Danielle T.",
        'Name': "francescadanielletpueyo@iskolarngbayan.pup.edu.ph",
        'Password': "6060",
        'State': 1,
        'Rep':'mailto:noeneilicalpito@iskolarngbayan.pup.edu.ph?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out',
        'Repmail':'noeneilicalpito@iskolarngbayan.pup.edu.ph'
    },
    {
        'User':"Yap, Rechmiale Eel M jr.", 
        'Name': "rechmialeelmyapjr@iskolarngbayan.pup.edu.ph",
        'Password': "7070",
        'State': 0,
        'Rep':'mailto:noeneilicalpito@iskolarngbayan.pup.edu.ph?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out',
        'Repmail':'noeneilicalpito@iskolarngbayan.pup.edu.ph'
    },
    {
        'User':"Calpito, Noeniel I.",
        'Name': "noeneilicalpito@iskolarngbayan.pup.edu.ph",
        'Password': "1111",
        'State': 1,
        'Rep':'mailto:noeneilicalpito@iskolarngbayan.pup.edu.ph?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out',
        'Repmail':'noeneilicalpito@iskolarngbayan.pup.edu.ph'
    },
    {
        'User':"Valdez, John Ray R.",
        'Name': "johnrayrvaldez@iskolarngbayan.pup.edu.ph",
        'Password': "2222",
        'State': 1,
        'Rep':'mailto:johnrayrvaldez@iskolarngbayan.pup.edu.ph?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out',
        'Repmail':'johnrayrvaldez@iskolarngbayan.pup.edu.ph'
    },
    {
        'User':"Admin",
        'Name': "test",
        'Password': "0000",
        'State': 1,
        'Rep':'mailto:shervannickolaiydabu@iskolarngbayan.pup.edu.ph?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out',
        'Repmail':'noeneilicalpito@iskolarngbayan.pup.edu.ph'
    },
    {   
        'User':"Admin1",
        'Name': "test1",
        'Password': "9999",
        'State': 0,
        'Rep':'mailto:shervannickolaiydabu@iskolarngbayan.pup.edu.ph?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out',
        'Repmail':'johnrayrvaldez@iskolarngbayan.pup.edu.ph'
    },
    {   
        'User':"Admin2",
        'Name': "test2",
        'Password': "1234",
        'State': 1,
        'Rep':'mailto:shervannickolaiydabu@iskolarngbayan.pup.edu.ph?subject=Test%20Subject&body=Hello%20there,%0D%0A%0D%0AI%20wanted%20to%20reach%20out',
        'Repmail':'johnrayrvaldez@iskolarngbayan.pup.edu.ph'
    }
    ]'''




def test(m, x):
    with open('Users.json', 'r') as json_file:
        info = json.load(json_file)

    lols = cha(m, x, info)
    
    if lols:
        n = input("New pass: ")
        lols["Password"] = n
        with open('Users.json', 'w') as json_file:
            json.dump(info, json_file, indent= 4)

        print(f"Password of {lols["Name"]} has been changed to {lols["Password"]}")
    


def cha(user, passw, person):
    for i in person:
        if i['Name'] == user and i['Password'] == passw:
            return i
    return None
    
def log():
    no = input()
    no2 = input()
    with open('Users.json', 'r') as json_file:
        info = json.load(json_file)
    
    lol = cha(no, no2, info)

    if lol:
        test(no, no2)
    else:
        print('Bruh')


            
log()