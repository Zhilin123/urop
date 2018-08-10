# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:09:32 2018

@author: Zhou Renjie
"""

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
    
''' 
print(psw_retrieval("asd"))
print(psw_retrieval("a@c.com"))
'''


