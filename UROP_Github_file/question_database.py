# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:35:59 2018

@author: Zhou Renjie
"""

import sqlite3

def create_table(): 
    conn = sqlite3.connect('qns.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("CREATE TABLE IF NOT EXISTS qns(id INTEGER PRIMARY KEY ASC, qn TEXT, op1 TEXT, op2 TEXT, op3 TEXT, op4 TEXT, op5 TEXT, hint1 TEXT, correct_ans TEXT, qn_pic TEXT)") 
    #use SQL query language to create a database table called uname_psw
    #the CURSOR, c! does all the SQL queries
    
def data_entry(ID, QN, OP1, OP2, OP3, OP4, OP5, H1, ANS, QN_PIC):
    conn = sqlite3.connect('qns.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("INSERT INTO qns (id, qn, op1, op2, op3, op4, op5, hint1, correct_ans, qn_pic) VALUES(?, ?, ?, ?, ?, ?, ?, ?,?,?)", (ID, QN, OP1, OP2, OP3, OP4, OP5, H1, ANS, QN_PIC)) #follow the same order as attributes when building the database table
    conn.commit() #always commit when making modifications, eg. inputing data
    c.close()
    conn.close()

def qn_retrieval(qnID):
    conn = sqlite3.connect('qns.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    #c.execute("SELECT * FROM qns WHERE id = ?", (qnID, )) #in SQL command, you can't just parse in a python variable
    c.execute("SELECT * FROM qns")
    one_question = c.fetchall()
    #print(one_question)
    c.close()
    conn.close()
    return one_question

def add_column():
    conn = sqlite3.connect('qns.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("ALTER TABLE qns ADD COLUMN hint2 TEXT hint3 TEXT hint4 TEXT correct_ans TEXT")
    conn.commit()
    c.close()
    conn.close()    
    
def drop_table():
    conn = sqlite3.connect('qns.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor()
    c.execute("DROP TABLE qns")
    c.close()
    conn.close()

'''
drop_table()  
create_table()    
#data_entry(1, "asd", "a", "b", "c", "d")
#data_entry(1, "If Jenna has a dozen apples and she ate two-thirds of it, how many does she have left?", "3", "4", "8", "12","TMubSggUOVE","AsQ_uJDBrIU","9hZkk73nJ_Y","BiCUCqiWOlo","2")
#data_entry(2, "Jenna is twenty one years old now. If she was two-third zhilin’s age 19 years ago, how old is Zhilin now?", "3", "20", "22", "23","TMubSggUOVE","AsQ_uJDBrIU","9hZkk73nJ_Y","BiCUCqiWOlo","2" )
#data_entry(3, "If one apple and 2 pencils cost $1.10 and 2 apples and 1 pencil costs $2.05. Wht is the difference between the cost of an apple and a pencil?", "$0.05", "$0.10", "$0.95", "$1.05", "TMubSggUOVE","AsQ_uJDBrIU","9hZkk73nJ_Y","BiCUCqiWOlo","3")
#print(qn_retrieval(1))

data_entry(1, "Here is how Nita solves two addition problems. Do you think that the problems are solved correctly? If not, why is Nita wrong in her responses?", "Nita doesn’t know how to add numbers", "Nita doesn’t know place value and carry forward of values", "Nita was not attentive", "I don’t know", "Any other","ayFAh4VNMFA","2","metamath1")
data_entry(2, "Here is how another child, Iqbal solves two subtraction problems given to him by his teacher.Do you think that the problems are solved correctly? If not, why is Iqbal wrong in his responses?", "Iqbal doesn’t know how to subtract numbers", "Iqbal doesn’t know place value and borrowing of values", "Iqbal was not attentive", "I don’t know", "Any other","ul2ZpZT_byU","2","metamath2")
data_entry(3, "Here is a page from Seema’s math notebook. Why does Seema make these mistakes? ", "Seema doesn’t know how to multiply ", "Seema mistook multiplication symbol for addition", "Seema was not attentive", "I don’t know", "Any other","FJ5qLWP3Fqo","2","metamath3")
data_entry(4, "Sita stacks the boxes (image 1) in the corner of the room. All boxes are the same size. How many boxes has she used, in total? [Please tick/circle]", "25 ", "19", "18", "13", "NA","VQEm698nOhU","3","wordprob1")
data_entry(5, "Kerosene comes in 5 litre cans. Ashoka needs 17 litres of kerosene for the household. How many cans must he buy? [Please tick/circle correct answer]", "5 ", "2", "8", "4", "NA","lcFFYzr_SvE","4","NA")
data_entry(6, "Zarin has these cards (see image 2 below) with numbers on them. What is the smallest three digit number she can show with the cards? She may use each card only once.", "NA ", "NA", "NA", "NA", "NA","T5Qf0qSSJFI","125","wordprob3")
data_entry(7, "If the pattern 3, 6, 9, 12 were to be continued, which of the numbers (given below) could be one of the numbers? [Please tick/circle correct answer]", "26 ", "27", "28", "29", "NA","lj_X9JVSF8k","2","NA")
data_entry(8, "Adil went to buy some apples from the bazaar. The shopkeeper put the apples on the weighing scale to calculate the price. How much do the apples weigh in grams, as shown in the scale (image 3) below?", "NA", "NA", "NA", "NA", "NA","ptaVY3-vRZM","220","wordprob5")
data_entry(9, "Rahim and Gaurav are playing a game. The object of the game is to get the highest total of points. The chart below shows how many points they scored. Who won and by how many points? (Please tick your answer)", "Gaurav won by 25 points  ", "Gaurav won by 100 points ", "Rahim won by 25 points ", "Rahim won by 175 points", "NA","v9J3VuI8_y0","1","wordprob6")
'''


