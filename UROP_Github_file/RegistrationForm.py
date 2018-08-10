# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 11:39:55 2018

@author: Zhou Renjie
"""
from wtforms import Form, TextField, PasswordField, DateField, IntegerField, validators
from passlib.hash import sha256_crypt


class RegistrationForm(Form):
    first_name = TextField('First Name', [validators.Length(min=1, max=20)])
    last_name = TextField('Last Name', [validators.Length(min=1, max=20)])
    email = TextField('Email Address', [
        validators.Length(min=6, max=50),
        validators.Required(),
        validators.Email(message='Please enter a valid email address')
    ])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Your passwords do not match!')
        ]) #message is printed when the password doesnt not match the confirmation password
    confirm = PasswordField('Confirm Password')
    dob = DateField('Date of Birth', format='%d-%m-%Y', )
    age = IntegerField('Age', [validators.NumberRange(min=0, max=100, message='Please enter a valid age')])
    birth_cty = TextField('Country of Birth', [validators.Length(min=1, max=30)])
    res_cty = TextField('Country of Residence', [validators.Length(min=1, max=30)])
    