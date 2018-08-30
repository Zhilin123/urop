# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, flash, render_template, request, redirect, session, url_for
from wtforms import Form, TextField, PasswordField, validators
from wtforms.fields.html5 import IntegerField, EmailField
from passlib.hash import sha256_crypt
import os
import user_database as u_db
import question_database as qn_db
import json

app = Flask(__name__)
app.secret_key = os.urandom(12) #need this for session to work

max_qn = 9
@app.route('/', methods=['POST', 'GET'])
def home(): 
    if 'logged_in' not in session:
       session['logged_in'] = False
    if request.method == 'POST' and session['logged_in'] == True:
       if request.form['logout'] == 'logout':
          session['logged_in'] = False
                #flash('You are logged out now!')
          return redirect(url_for('home'))
    
    try:
        current_user = session['username']
        last_qn_attempted = u_db.retrieve_last_single_attempt(current_user)
        category = last_qn_attempted [-4]
        category_id = last_qn_attempted [-1] +1 
        newquestions = qn_db.new_qn_retrieval(category)
        if category_id > len(newquestions):
            category_id = 1 
        if category == 'none':
            category = 'newquestion'
        last_session_id = str(u_db.retrieve_last_session_id(current_user))
        total_attempted_last_session, number_correct_last_session = u_db.retrieve_score_of_last_session(last_session_id)
        total_number_of_questions = qn_db.check_total_number_of_questions()
        total_attempted,total_correct = u_db.retrieve_total_attempted_qns_and_correct(current_user)
        user_info = [total_attempted_last_session, number_correct_last_session,total_attempted,total_correct,total_number_of_questions]
        u_db.insert_or_update_score(current_user)
        topscore5 =u_db.get_top_5_scores()
        show_results = request.args.get('show_results')
        finished_all = request.args.get('finished_all')
        return render_template('home.html', category=category, category_id =category_id, user_info = user_info,topscore5 = topscore5, show_results=show_results, finished_all = finished_all)
    except:
        topscore5 =u_db.get_top_5_scores()
        return render_template('home.html', category="NA", category_id = "NA", user_info = None,topscore5 = topscore5, show_results=None, finished_all = None)

@app.route('/login', methods=['POST', 'GET'])
def do_admin_login():
   # try:
        error = None
        '''
        if 'logged_in' not in session:
            session['logged_in'] = False
        if request.method == 'POST' and session['logged_in'] == True:
            if request.form['logout'] == 'logout':
                session['logged_in'] = False
                #flash('You are logged out now!')
                return redirect(url_for('home'))
        ''' 
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            #all_users  # this is the encrypted password stored in the database
            #the data retrieved from the database is presented in a tuple, therefore need an index to index the number
            try:
                if sha256_crypt.verify(password, u_db.psw_retrieval(username)[0]): 
                    session['logged_in'] = True;
                    session['username'] = username;
                    return redirect(url_for('home'))
                else:
                    error = "The username or/and password is wrong. Please try again."
            except:
                error = "The username or/and password is wrong. Please try again."
        
        return render_template('login.html', error=error)    
    
   # except Exception as e:
   #     error = "The username or/and password is wrong. Please try again."
   #     return render_template('login.html', error=error)

#Cannot import class from another customised module. Can only use your own module
class RegistrationForm(Form):
    email = EmailField('E-mail Address', [
        validators.Length(min=6, max=50),
        validators.Required(),
        validators.Email(message='Please enter a valid email address')
    ])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Your passwords do not match!')
        ]) #message is printed when the password doesnt not match the confirmation password
    confirm = PasswordField('Confirm Password' )
    age = IntegerField('Age', [validators.NumberRange(min=0, max=100, message='Please enter a valid age')])
    birth_cty = TextField('Country of Birth', [validators.Length(min=1, max=30)])
    res_cty = TextField('Country of Residence', [validators.Length(min=1, max=30)])
    town = TextField('Town/City of Residence', [validators.Length(min=1, max=50)])
    mother_tongue = TextField('Mother Tongue(s)', [validators.Length(min=1, max=50)])
    other_language = TextField('Other language(s) spoken', [validators.Length(min=1, max=50)])
    in_school_since =  IntegerField('In school since (ie 2008)', [validators.NumberRange(min=1950, max=2030, message='Please enter a valid year')])


@app.route('/register', methods=['GET','POST'])
def do_admin_register():
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate():
            email = form.email.data
            if u_db.psw_retrieval(email) != None:
                error = "That E-mail adress is already taken"
                return render_template('register_short.html', form=form, error=error)
            else:
                password = sha256_crypt.encrypt((str(form.password.data)))
                age = form.age.data
                birth_country = form.birth_cty.data
                residence_country = form.res_cty.data
                town = form.town.data
                mother_tongue = form.mother_tongue.data
                other_language = form.other_language.data
                in_school_since = form.in_school_since.data
                u_db.create_table()
                u_db.data_entry(email, password, age, birth_country, residence_country, town, mother_tongue, other_language, in_school_since)
                session['logged_in'] = True
                session['username'] = email
                return redirect(url_for('do_admin_register'))
        else:
            return render_template('register_short.html', form=form)


allquestions = qn_db.qn_retrieval(1)
'''
with open("translation.json", "r",encoding='utf-8') as read_file:
    qn_translate = json.load(read_file)
'''
#user_input = list(range(max_qn+1))
@app.route('/question/<qn>', methods=['GET', 'POST'])
def question(qn):
    if request.method == 'GET':
        return render_template('mindmap.html', question_id = qn, tuple_of_qn = allquestions[int(qn)-1])
    else:
        if 'user_input' not in session:
            session['user_input'] = [0 for i in range(max_qn*4+1)]
        current_user = session['username']
        car = request.form.get("cars")
        session['user_input'][int(qn)-1] = car
        hinted = request.form.get("used_hint")
        session['user_input'][int(qn)+max_qn-1] = hinted
        translated = request.form.get("used_translate")
        session['user_input'][int(qn)+max_qn+max_qn-1] = translated
        definition = request.form.get("used_definition")
        session['user_input'][int(qn)+max_qn+max_qn+max_qn-1] = definition    
        current_qn = int(qn) + 1
        flash(str(session['user_input']))
        if current_qn > max_qn:
            #flash("Yay! You are done!")
            #return str(session['user_input'])
            session['user_input'][-1] = current_user #since task needs to have current_user at the last place to input into the SQL query, 
            task = tuple(session['user_input'])
            #return str(task)
            #u_db.inser_user_input(task)
            #insert into attempts table
            u_db.inser_input_attempts(task)
            # session['user_input'] is a list of 10 strings
            score = 0
            for i in range(max_qn):
                if session['user_input'][i] == allquestions[i][-2]:
                    score += 1
            return render_template('finish.html', score = score, max_qn = max_qn)
        #if qn == '2':
        #    return str(session['user_input'])
        
        return redirect('/question/' + str(current_qn))



@app.route('/newquestion/<qn>', methods=['GET', 'POST'])
def new_question(qn):
    newquestions = qn_db.new_qn_retrieval()
    difficulty_levels = [[],[]]
    category = 'none'
    for i in range(len(newquestions)):
        if newquestions[i][4] not in difficulty_levels[0]:
            difficulty_levels[0].append(newquestions[i][4])
            difficulty_levels[1].append(i+1)
    if request.method == 'GET':
        return render_template('newmindmap.html', question_id = qn, tuple_of_qn = newquestions[int(qn)-1],difficulty_levels = difficulty_levels,category = 'none', check_answer = 'none', max_qn_number = len(newquestions))
    else:
        current_user = session['username']
        car = request.form.get("cars")
        hinted = request.form.get("used_hint")
        translated = request.form.get("used_translate")
        definition = request.form.get("used_definition")
        checking = request.form.get("check_answer")
        #one_session_id = session['one_session_id']
        if checking == "yes":
            accepted_ans = qn_db.accepted_answers(newquestions[int(qn)-1][2])
            check_answer = qn_db.check_if_answer_is_correct(accepted_ans, car)
            return render_template('newmindmap.html', question_id = qn, tuple_of_qn = newquestions[int(qn)-1],difficulty_levels = difficulty_levels,category = 'none', check_answer = check_answer, max_qn_number = len(newquestions))
        else:
            if 'one_session_id' not in session:
                u_db.insert_one_session((current_user,))
                session['one_session_id'] = u_db.retrieve_last_session_id(current_user)
            one_session_id = session['one_session_id']
            questionid = newquestions[int(qn)-1][0]
            accepted_ans = qn_db.accepted_answers(newquestions[int(qn)-1][2])
            correct_or_not = qn_db.check_answer_true_false(accepted_ans, car)
            #qnid, answer, hint, translate, definition, email
            u_db.inser_input_one_attempt(tuple([questionid, qn, car, correct_or_not, hinted, translated, definition,category, one_session_id, current_user]))
            current_qn = int(qn) + 1
            if current_qn < len(newquestions):
                return redirect('/newquestion/' + str(current_qn))
            else:
                return redirect('/?finished_all=true')

@app.route('/<category>/<qn>', methods=['GET','POST'])
def category(category,qn):
    newquestions = qn_db.new_qn_retrieval(category)
    difficulty_levels = [[],[]]
    for i in range(len(newquestions)):
        if newquestions[i][4] not in difficulty_levels[0]:
            difficulty_levels[0].append(newquestions[i][4])
            difficulty_levels[1].append(i+1)
        
    if request.method == 'GET':
        return render_template('newmindmap.html', question_id = qn, tuple_of_qn = newquestions[int(qn)-1],difficulty_levels = difficulty_levels,category = category, check_answer = 'none', max_qn_number = len(newquestions))
    else:
        current_user = session['username']
        car = request.form.get("cars")
        hinted = request.form.get("used_hint")
        translated = request.form.get("used_translate")
        definition = request.form.get("used_definition")
        checking = request.form.get("check_answer")
        if checking == "yes":
            accepted_ans = qn_db.accepted_answers(newquestions[int(qn)-1][2])
            check_answer = qn_db.check_if_answer_is_correct(accepted_ans, car)
            return render_template('newmindmap.html', question_id = qn, tuple_of_qn = newquestions[int(qn)-1],difficulty_levels = difficulty_levels,category = 'none', check_answer = check_answer, max_qn_number = len(newquestions))
        else:
            if 'one_session_id' not in session:
                u_db.insert_one_session((current_user,))
                session['one_session_id'] = u_db.retrieve_last_session_id(current_user)
            one_session_id = session['one_session_id']
            accepted_ans = qn_db.accepted_answers(newquestions[int(qn)-1][2])
            correct_or_not = qn_db.check_answer_true_false(accepted_ans, car)
            questionid = newquestions[int(qn)-1][0]
            #qnid, answer, hint, translate, definition, email
            u_db.inser_input_one_attempt(tuple([questionid, qn, car, correct_or_not, hinted, translated, definition,category, one_session_id, current_user]))
            current_qn = int(qn) + 1
            if current_qn < len(newquestions):
                return redirect('/' + category + '/' + str(current_qn))
            else:
                return redirect('/?finished_all=true')


if __name__ == "__main__":
    
    app.run(debug=True, port=4004)

