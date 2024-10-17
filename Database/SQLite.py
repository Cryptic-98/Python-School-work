import sqlite3
# we need to create a database
con = sqlite3.connect('student.db')
# create the database
# con.execute(""" create table studenttb
#             (id int primary key not null,
#             name text not null,
#             email text not null,
#             password text not null);
# """)

con.execute("""insert into studenttb (id,name,email,password)"
            "values(1234, 'Royal Goronga', 'royalg@richfield.ac.za', '12345');""")
con.execute("""insert into studenttb (id,name,email,password)"
            "values(8845, 'Henry Cane', 'henrycane@gmail.com', 'drowsapp');""")


con.commit()

con.execute("""SELECT name from studenttb where username = 'Royal'""").fetchone()
con.execute("""SELECT password from studenttb where username = 'Royal'""").fetchone()





