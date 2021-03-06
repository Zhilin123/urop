# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:35:59 2018

@author: Zhou Renjie
"""

import sqlite3
import json

def create_table(): 
    conn = sqlite3.connect('qns.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("CREATE TABLE IF NOT EXISTS qns(id INTEGER PRIMARY KEY ASC, qn TEXT, op1 TEXT, op2 TEXT, op3 TEXT, op4 TEXT, op5 TEXT, hint1 TEXT, correct_ans TEXT, qn_pic TEXT, qn_table TEXT)") 
    #use SQL query language to create a database table called uname_psw
    #the CURSOR, c! does all the SQL queries
    
def data_entry(ID, QN, OP1, OP2, OP3, OP4, OP5, H1, ANS, QN_PIC,QN_TABLE):
    conn = sqlite3.connect('qns.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("INSERT INTO qns (id, qn, op1, op2, op3, op4, op5, hint1, correct_ans, qn_pic,qn_table) VALUES(?, ?, ?, ?, ?, ?, ?, ?,?,?,?)", (ID, QN, OP1, OP2, OP3, OP4, OP5, H1, ANS, QN_PIC, QN_TABLE)) #follow the same order as attributes when building the database table
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
    c.execute("DROP TABLE newqns")
    c.close()
    conn.close()

'''
  
#data_entry(1, "asd", "a", "b", "c", "d")
#data_entry(1, "If Jenna has a dozen apples and she ate two-thirds of it, how many does she have left?", "3", "4", "8", "12","TMubSggUOVE","AsQ_uJDBrIU","9hZkk73nJ_Y","BiCUCqiWOlo","2")
#data_entry(2, "Jenna is twenty one years old now. If she was two-third zhilin’s age 19 years ago, how old is Zhilin now?", "3", "20", "22", "23","TMubSggUOVE","AsQ_uJDBrIU","9hZkk73nJ_Y","BiCUCqiWOlo","2" )
#data_entry(3, "If one apple and 2 pencils cost $1.10 and 2 apples and 1 pencil costs $2.05. Wht is the difference between the cost of an apple and a pencil?", "$0.05", "$0.10", "$0.95", "$1.05", "TMubSggUOVE","AsQ_uJDBrIU","9hZkk73nJ_Y","BiCUCqiWOlo","3")
#print(qn_retrieval(1))

drop_table()  
create_table()  
data_entry(1, "Here is how Nita solves two addition problems. Do you think that the problems are solved correctly? If not, why is Nita wrong in her responses?", "Nita doesn’t know how to add numbers", "Nita doesn’t know place value and carry forward of values", "Nita was not attentive", "I don’t know", "Any other","ayFAh4VNMFA","2","NA","<table> <tr> <td>19</td> <td>17</td> </tr> <tr> <td><u>+13</u></td> <td><u>+9</td> </tr> <tr> <td>212</td> <td>116</td> </tr> </table>")
data_entry(2, "Here is how another child, Iqbal solves two subtraction problems given to him by his teacher. Do you think that the problems are solved correctly? If not, why is Iqbal wrong in his responses?", "Iqbal doesn’t know how to subtract numbers", "Iqbal doesn’t know place value and borrowing of values", "Iqbal was not attentive", "I don’t know", "Any other","ul2ZpZT_byU","2","NA"," <table> <tr> <td>22</td> <td>27</td> </tr> <tr> <td><u>-18</u></td> <td><u>-9</td> </tr> <tr> <td>16</td> <td>22</td> </tr> </table>")
data_entry(3, "Here is a page from Seema’s math notebook. Why does Seema make these mistakes? ", "Seema doesn’t know how to multiply ", "Seema mistook multiplication symbol for addition", "Seema was not attentive", "I don’t know", "Any other","FJ5qLWP3Fqo","2","NA","<table> <tr> <td>5 x 4 = 9</td> </tr> <tr> <td>3 x 2 = 5</td> </tr> <tr> <td>4 x 2 = 6</td> </tr> </table>")
data_entry(4, "Sita stacks the boxes (image 1) in the corner of the room. All boxes are the same size. How many boxes has she used, in total? [Please tick/circle]", "25 ", "19", "18", "13", "NA","VQEm698nOhU","3","wordprob1","")
data_entry(5, "Kerosene comes in 5 litre cans. Ashoka needs 17 litres of kerosene for the household. How many cans must he buy? [Please tick/circle correct answer]", "5 ", "2", "8", "4", "NA","lcFFYzr_SvE","4","NA","")
data_entry(6, "Zarin has these cards (see image 2 below) with numbers on them.What is the smallest three digit number she can show with the cards? She may use each card only once.", "NA ", "NA", "NA", "NA", "NA","T5Qf0qSSJFI","125","NA","<table id='question6'> <tr> <td>1</td> <td>8</td> <td>6</td> <td>5</td> <td>2</td> </tr> </table> <style> #question6 td { border: 1px solid black; padding:15px; } </style>")
data_entry(7, "If the pattern 3, 6, 9, 12 were to be continued, which of the numbers (given below) could be one of the numbers? [Please tick/circle correct answer]", "26 ", "27", "28", "29", "NA","lj_X9JVSF8k","2","NA","")
data_entry(8, "Adil went to buy some apples from the bazaar. The shopkeeper put the apples on the weighing scale to calculate the price. How much do the apples weigh in grams, as shown in the scale (image 3) below?", "NA", "NA", "NA", "NA", "NA","ptaVY3-vRZM","220","wordprob5","")
data_entry(9, "Rahim and Gaurav are playing a game. The object of the game is to get the highest total of points. The chart below shows how many points they scored. Who won and by how many points? (Please tick your answer)", "Gaurav won by 25 points  ", "Gaurav won by 100 points ", "Rahim won by 25 points ", "Rahim won by 175 points", "NA","v9J3VuI8_y0","1","NA","<table id='question9'> <tr> <td>Player</td> <td>Rahim</td> <td>Gaurav</td> </tr> <tr> <td>Round 1</td> <td>125</td> <td>100</td> </tr> <tr> <td>Round 2</td> <td>125</td> <td>125</td> </tr> <tr> <td>Round 3</td> <td>150</td> <td>100</td> </tr> <tr> <td>Round 4</td> <td>50</td> <td>150</td> </tr> </table> <style> #question9 td, #question9 { border: 0.05px solid black; border-spacing: 0px; } #question9 td { padding:5px; } </style>")
'''
def create_new_table(): 
    conn = sqlite3.connect('qns.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("CREATE TABLE IF NOT EXISTS newqns(id INTEGER PRIMARY KEY ASC, qn TEXT, solution TEXT, template TEXT, difficulty INTEGER, qngroup TEXT, hint TEXT)") 
    #use SQL query language to create a database table called uname_psw
    #the CURSOR, c! does all the SQL queries

def data_entry_new_table(QN, SOLUTION, TEMPLATE, DIFFICULTY, QNGROUP, HINT):
    conn = sqlite3.connect('qns.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    c.execute("INSERT INTO newqns (qn, solution, template, difficulty, qngroup, hint) VALUES(?, ?, ?, ?, ?,?)", (QN, SOLUTION, TEMPLATE, DIFFICULTY, QNGROUP, HINT)) #follow the same order as attributes when building the database table
    conn.commit() #always commit when making modifications, eg. inputing data
    c.close()
    conn.close()

def new_qn_retrieval(category_name='not_set'):
    conn = sqlite3.connect('qns.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    #c.execute("SELECT * FROM qns WHERE id = ?", (qnID, )) #in SQL command, you can't just parse in a python variable
    if category_name == 'not_set':
        c.execute("SELECT * FROM newqns ORDER BY difficulty ")
    else:
        c.execute("SELECT * FROM newqns WHERE qngroup = '"+ category_name +"' ORDER BY difficulty ")
    one_question = c.fetchall()
    #print(one_question)
    c.close()
    conn.close()
    return one_question

def accepted_answers(answer_database):
    answer_list = json.loads(answer_database)
    accepted_answers = []
    for i in answer_list:
        accepted_answers.append(i)
    if len(answer_list) == 2:
        accepted_answers.append(int(str(int(answer_list[0]))+str(int(answer_list[1]))))
        accepted_answers.append(int(str(int(answer_list[1]))+str(int(answer_list[0]))))
    return answer_list

def check_if_answer_is_correct(answer_list, user_answer):
    if len(user_answer) == 0:
        return 'please enter an answer'
    try:
        answer = float(user_answer)
        for i in answer_list:
            if abs(i - answer) < 1:
                return True
        return False
    except:
        answer = user_answer.split(",")
        number_of_answers = len(answer)
        number_correct = 0
        for i in answer:
            clean_answer = i.strip()
            for j in clean_answer:
                if j.isdigit() or j == '.':
                    pass
                else:
                    return "invalid response: enter only numbers or a comma to separate numbers"
            clean_answer = float(clean_answer)
            for j in answer_list:
                if abs(clean_answer - j) < 1:
                    number_correct += 1
        if number_correct == 0:
            return False
        elif number_correct == number_of_answers:
            return True
        else:
            return str(number_correct) + " out of " + str( number_of_answers) + " correct"
        
def check_answer_true_false(answer_list,user_answer):
    try:
        answer = float(user_answer)
        for i in answer_list:
            if abs(i - answer) < 1:
                return 1
        return 0
    except:
        answer = user_answer.split(",")
        number_of_answers = len(answer)
        number_correct = 0
        for i in answer:
            clean_answer = i.strip()
            for j in clean_answer:
                if j.isdigit() or j == '.':
                    pass
                else:
                    return 0
            clean_answer = float(clean_answer)
            for j in answer_list:
                if abs(clean_answer - j) < 1:
                    number_correct += 1
        if number_correct == number_of_answers:
            return 1
        else:
            return 0

def check_total_number_of_questions():
    conn = sqlite3.connect('qns.db') #this connects to a database. If the database doesnt exist, it will create a new database and then connects to it from the second time onwards
    c = conn.cursor() #this is where the current cursor is at in the database
    #c.execute("SELECT * FROM qns WHERE id = ?", (qnID, )) #in SQL command, you can't just parse in a python variable
    c.execute("SELECT id FROM newqns ORDER BY id DESC")
    number = c.fetchone()
    #print(one_question)
    c.close()
    conn.close()
    return number[0]

# newqns table should have the following fields --> qn, correct ans, topic

# new table for topics to hints based on templates of questions 

"""
drop_table()
create_new_table()
import json

with open("questions_to_upload.json","r") as f:
  data_to_enter_database = json.load(f)

import nltk.data # $ pip install http://www.nltk.org/nltk3-alpha/nltk-3.0a3.tar.gz
# python -c "import nltk; nltk.download('punkt')"
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
text = 'the sum of a certain number and a second number is -42 . the first number minus the second is 52 . find the numbers .'
counter = 0
for i in data_to_enter_database:
    text = i[0]
    sentences = sent_tokenizer.tokenize(text)
    sentences = [sent.capitalize() for sent in sentences]
    sentences = ' '.join(sentences)
    data_entry_new_table(sentences,str(i[1]),str(i[2]),int(i[3]),i[4],i[5])
    counter += 1
    if counter % 50 == 0:
        print(counter, " / ", 1000)
"""
