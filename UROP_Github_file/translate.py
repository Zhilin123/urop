#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:30:01 2018

@author: wangxiujiang
"""
"""
'''
from googletrans import Translator
translator = Translator()
translator.translate('Hello I am zhilin',dest='zh-cn').text

import question_database as qn_db
allquestions = qn_db.qn_retrieval(1)

translated_qn_and_ans = {}
for i in allquestions:
    for j in range(len(i)):
        if j in [1,2,3,4,5,6]:
            if i[j] != 'NA':
                translated_qn_and_ans[i[j]] = translator.translate(i[j],dest='zh-cn').text
            
'''
import io
import json
'''
with io.open('translation.json', 'w', encoding='utf8') as json_file:
    json.dump(translated_qn_and_ans, json_file, ensure_ascii=False)
'''  
with open("translation.json", "r",encoding='utf-8') as read_file:
    data = json.load(read_file)
"""
definition_dict = {
        "responses": "a verbal or written answer",
        "attentive": "an answer or reply, as in words or in some action",
        "subtraction" : "to remove something",
        "mistakes" : "an act or judgement that is misguided or wrong.",
        "symbol" : "a mark or character used as a conventional representation of an object, function, or process",
        "mistook" : "be wrong about.",
        "stacks": "to arrange things so that they are placed one on top of another",
        "kerosene" : "a light fuel oil obtained by distilling petroleum, used especially in jet engines and domestic heating boilers; paraffin oil.",
        "digit" : "any of the numerals from 0 to 9, especially when forming part of a number.",
        "pattern": "a set of numbers or objects in which all the members are related with each other by a specific rule.",
        "bazaar": "a market",
        "shopkeeper" : " a person who sells things",
        "calculate": " to determine mathematically",
        "scale": "devices to measure weight",
        "chart" : "a sheet of information in the form of a table, graph, or diagram.",
        "object":"a thing aimed at or sought; a goal"
        }
