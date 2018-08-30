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

def add_column_attempts():
    c.execute("ALTER TABLE single_attempts ADD COLUMN category_id INTEGER")
    conn.commit()

def create_one_attempt_table(): 
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("CREATE TABLE IF NOT EXISTS single_attempts(id INTEGER PRIMARY KEY ASC, email TEXT, qnid TEXT, answer TEXT, correct INTEGER, hint TEXT, translate TEXT, definition TEXT, page TEXT, datetime TIMESTAMP)") 
    #use SQL query language to create a database table called uname_psw
    #the CURSOR, c! does all the SQL queries  

def inser_input_one_attempt(task):
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor()
    task += (datetime.datetime.now(),)
    c.execute("INSERT INTO single_attempts (qnid, category_id, answer,correct, hint, translate, definition, page, one_session_id, email, datetime) VALUES(?,?, ?, ?, ?,?, ?,?, ?, ?, ?)", task)
    #c.execute("UPDATE attempts SET user_input=?, user_input2=?, user_input3=?, user_input4=?, user_input5=?, user_input6=?, user_input7=?, user_input8=?, user_input9=?, email=?", task)
    conn.commit() 
    c.close()
    conn.close()

def create_sessions_table(): 
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("CREATE TABLE IF NOT EXISTS sessions(id INTEGER PRIMARY KEY ASC, email TEXT, datetime TIMESTAMP)") 
    #use SQL query language to create a database table called uname_psw
    #the CURSOR, c! does all the SQL queries  

def insert_one_session(task):
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor()
    task += (datetime.datetime.now(),)
    c.execute("INSERT INTO sessions (email, datetime) VALUES(?, ?)", task)
    conn.commit() 
    c.close()
    conn.close()  

def retrieve_last_session_id(username):
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    #c.execute("SELECT * FROM qns WHERE id = ?", (qnID, )) #in SQL command, you can't just parse in a python variable
    c.execute("SELECT * FROM sessions where email == '" + username +"'ORDER BY id DESC")
    one_question = c.fetchone()
    #print(one_question)
    c.close()
    conn.close()
    one_id = list(one_question)[0]
    return one_id

def retrieve_score_of_last_session(session_id):
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    #c.execute("SELECT * FROM qns WHERE id = ?", (qnID, )) #in SQL command, you can't just parse in a python variable
    c.execute("SELECT qnid,correct FROM single_attempts where one_session_id == '" + session_id +"' ORDER BY datetime DESC")
    all_attempts = c.fetchall()
    all_attempts_with_score = [ i for i in all_attempts if type(i[1]) == int]
    attempted_questions = []
    correct_questions = []
    for i in all_attempts_with_score:
        if i[0] not in attempted_questions:
            attempted_questions.append(i[0])
        if i[1] == 1 and i[0] not in correct_questions:
            correct_questions.append(i[0])
                
    return len(attempted_questions), len(correct_questions)
    

def retrieve_total_attempted_qns_and_correct(username):
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    #c.execute("SELECT * FROM qns WHERE id = ?", (qnID, )) #in SQL command, you can't just parse in a python variable
    c.execute("SELECT qnid,correct FROM single_attempts where email == '" + username +"'ORDER BY id DESC")
    all_attempts = c.fetchall()
    all_attempts_with_score = [ i for i in all_attempts if type(i[1]) == int]
    attempted_questions = []
    correct_questions = []
    for i in all_attempts_with_score:
        if i[0] not in attempted_questions:
            attempted_questions.append(i[0])
        if i[1] == 1 and i[0] not in correct_questions:
            correct_questions.append(i[0])
                
    return len(attempted_questions), len(correct_questions)

def retrieve_last_single_attempt(username):
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("SELECT * FROM single_attempts where email == '" + username +"' ORDER BY datetime DESC")
    all_sessions = c.fetchone()
    c.close()
    conn.close()
    return all_sessions

def create_user_to_correct_table(): 
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("CREATE TABLE IF NOT EXISTS score(email TEXT, score INTEGER)") 
    #use SQL query language to create a database table called uname_psw
    #the CURSOR, c! does all the SQL queries  

def insert_or_update_score(username):
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    #c.execute("SELECT * FROM qns WHERE id = ?", (qnID, )) #in SQL command, you can't just parse in a python variable
    c.execute("SELECT * FROM score where email == '" + username +"'")
    all_sessions = c.fetchone()
    if all_sessions == None:
        #insert score
        total_attempted, total_correct = retrieve_total_attempted_qns_and_correct(username)
        task = (username,total_correct,)
        c.execute("INSERT INTO score (email, score) VALUES(?, ?)", task)
    else:
        total_attempted, total_correct = retrieve_total_attempted_qns_and_correct(username)
        c.execute("UPDATE score SET score = " + str(total_correct) + " WHERE email == '" + username +"'")
        #retrieve score
    conn.commit() 
    c.close()
    conn.close() 
    return "done"

def get_top_5_scores():
    conn = sqlite3.connect('users.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("SELECT * FROM score ORDER BY score DESC LIMIT 5")
    all_scores = c.fetchall()
    c.close()
    conn.close()
    without_email = []
    for i in range(len(all_scores)):
        name = all_scores[i][0].split("@")[0]
        without_email.append([i+1,name,all_scores[i][1]])
    return without_email
    
    
''' 
print(psw_retrieval("asd"))
print(psw_retrieval("a@c.com"))
for i in range(1,10):
    add_column_attempts(i)
'''

#create_one_attempt_table()