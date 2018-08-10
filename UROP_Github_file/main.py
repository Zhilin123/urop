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
'''
Problems yet to be solved:
  # - insert the score into the correct username
  # - debug session['user_input'] ---> use "flash" ????????MAGIC?????
   - the duration of session
  # - logout 
   - homepage design
'''
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
    return render_template('home.html')

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
            session['user_input'] = [0 for i in range(max_qn+1)]
        current_user = session['username']
        car = request.form.get("cars")
        session['user_input'][int(qn)-1] = car
        current_qn = int(qn) + 1
        flash(str(session['user_input']))
        if current_qn > max_qn:
            #flash("Yay! You are done!")
            #return str(session['user_input'])
            session['user_input'][-1] = current_user #since task needs to have current_user at the last place to input into the SQL query, 
            task = tuple(session['user_input'])
            #return str(task)
            u_db.inser_user_input(task)
            # session['user_input'] is a list of 10 strings
            score = 0
            for i in range(max_qn):
                if session['user_input'][i] == allquestions[i][-2]:
                    score += 1
            return render_template('finish.html', score = score, max_qn = max_qn)
        #if qn == '2':
        #    return str(session['user_input'])
        
        return redirect('/question/' + str(current_qn))




if __name__ == "__main__":
    
    app.run(debug=True, port=4002)

