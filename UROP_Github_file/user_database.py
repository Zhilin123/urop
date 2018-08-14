# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:09:32 2018

@author: Zhou Renjie
"""
import datetime
import sqlite3
conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
c = conn.cursor() #this is where the current cursor is at in the database

def create_table(): 
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("CREATE TABLE IF NOT EXISTS users(email TEXT, psw TEXT, age INTEGER, bc TEXT, rc TEXT, user_input TEXT)") 
    #use SQL query language to create a database table called uname_psw
    #the CURSOR, c! does all the SQL queries
    
def data_entry(email, password, age, birth_country, residence_country, town, mother_tongue, other_language, in_school_since):
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("INSERT INTO users (email, psw, age, bc, rc,town, mothertongue,otherlanguage,inschoolsince) VALUES(?, ?, ?, ?, ?, ?, ? ,? ,?)", 
    (email, password, age, birth_country, residence_country, town, mother_tongue, other_language, in_school_since)) #follow the same order as attributes when building the database table
    conn.commit() #always commit when making modifications, eg. inputing data
    c.close()
    conn.close()
    
def psw_retrieval(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT psw FROM users WHERE email = ?", (username, ))
    psw = c.fetchone()
    return psw

def add_column():
    c.execute("ALTER TABLE users ADD COLUMN inschoolsince INTEGER")
    conn.commit()
    c.close()
    conn.close()
    
def drop_table():
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor()
    c.execute("DROP TABLE users")
    c.close()
    conn.close()
    
def inser_user_input(task):
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor()
    c.execute("UPDATE users SET user_input=?, user_input2=?, user_input3=?, user_input4=?, user_input5=?, user_input6=?, user_input7=?, user_input8=?, user_input9=? WHERE email=?", task)
    conn.commit() 
    c.close()
    conn.close()
    
def create_attempts_table(): 
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("CREATE TABLE IF NOT EXISTS attempts(id INTEGER PRIMARY KEY ASC, email TEXT, user_input TEXT, user_input2 TEXT, user_input3 TEXT, user_input4 TEXT, user_input5 TEXT, user_input6 TEXT, user_input7 TEXT, user_input8 TEXT, user_input9 TEXT)") 
    #use SQL query language to create a database table called uname_psw
    #the CURSOR, c! does all the SQL queries

def inser_input_attempts(task):
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor()
    task += (datetime.datetime.now(),)
    c.execute("INSERT INTO attempts (user_input, user_input2, user_input3, user_input4, user_input5, user_input6, user_input7, user_input8, user_input9, hint1, hint2,hint3,hint4,hint5,hint6,hint7,hint8,hint9,translate1,translate2,translate3,translate4,translate5,translate6,translate7,translate8,translate9, definition1, definition2, definition3, definition4, definition5, definition6, definition7, definition8, definition9, email, datetime) VALUES(?, ?, ?, ?, ?, ?, ? ,? ,?, ?, ?, ?, ?, ?, ?, ? ,? ,?,?, ?, ?, ?, ?, ?, ? ,? ,?,?, ?, ?, ?, ?, ?, ? ,? ,?, ?,?)", task)
    #c.execute("UPDATE attempts SET user_input=?, user_input2=?, user_input3=?, user_input4=?, user_input5=?, user_input6=?, user_input7=?, user_input8=?, user_input9=?, email=?", task)
    conn.commit() 
    c.close()
    conn.close()

def add_column_attempts(number):
    c.execute("ALTER TABLE attempts ADD COLUMN definition"+ str(number) + " TEXT")
    conn.commit()
       
    
''' 
print(psw_retrieval("asd"))
print(psw_retrieval("a@c.com"))
for i in range(1,10):
    add_column_attempts(i)
'''
