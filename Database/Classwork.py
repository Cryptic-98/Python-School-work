import sqlite3
def userdb():
    global con
    con = sqlite3.connect('user_db.db')
    global cur
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS usertb
                (Username text not null,
                password text not null);''')

def userChoice():
    userdb()
    print('1. Register')
    print('2. Login')
    print('3. Quit')
    choice = int(input().strip())
    if choice == 1:
        return register()
    elif choice == 2:
        return login()
    elif choice == 3:
        quit
    else:
        print('Invalid entry.')
        userChoice()

def register():
    username = input('Create username: ')
    exists = con.execute("SELECT Username from usertb where Username = '{username}'").fetchone()
    if exists:
        print('Username already exists.')
        userChoice()
    password = input('Create password: ')
    con.execute("INSERT INTO usertb (username, password)"
                "VALUES (username, password);")
    con.commit()
    print("Successful login")
    input()

def login():
    username = input('Enter username: ')
    username_exists = con.execute("SELECT Username from usertb where Username = '{username}'").fetchone()
    if not username_exists:
        print('User does not exist.')
    def password_login():
        