#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:30:01 2018

@author: wangxiujiang
"""

"""
from googletrans import Translator
translator = Translator()
print(translator.translate('Hello I am Zhilin',dest='te').text) #telugu te #hindi hi #chinese zh-cn

import question_database as qn_db
allquestions = qn_db.new_qn_retrieval()

#difficult words are basicaly words that are not top 2000 in frequency and are not named entities

from nltk import FreqDist
from nltk.corpus import brown
frequency_list = FreqDist(i.lower() for i in brown.words())


most_common_1000_words = [ i[0] for i in frequency_list.most_common()[:1000]]



non_common_words = []
for i in allwords:
    if i.lower() not in most_common_1000_words:
        non_common_words.append(i)

import question_database as qn_db
allquestions = qn_db.new_qn_retrieval()

import nltk
allwords = []

for i in allquestions:
    tokens = nltk.word_tokenize(i[1])
    for j in tokens:
        if j not in allwords and j.isalpha():
            allwords.append(j)

allwords_lower = [i.lower() for i in allwords]

included_hardwords = []
counter = 0
for i in range(len(allwords_lower)):
    if allwords_lower[i] in hard_words:
        included_hardwords.append([allwords_lower[i], allwords[i]])
        counter += 1

print(counter)
"""
from nltk.corpus import wordnet as wn
from collections import Counter
def get_most_common_pos(word):
    wn_synsets = wn.synsets(word)
    pos_counts = Counter()
    pos_counts["n"] = len([item for item in wn_synsets if item.pos() == "n"])
    pos_counts["v"] = len([item for item in wn_synsets if item.pos() == "v"])
    pos_counts["a"] = len([item for item in wn_synsets if item.pos() == "a"])
    pos_counts["r"] = len([item for item in wn_synsets if item.pos() == "r"])
    most_common_pos = pos_counts.most_common(3)
    return most_common_pos[0][0]

def get_definition(word):
    pos_tag = get_most_common_pos(word)
    syns = wn.synsets(word,pos_tag)
    definition = syns[0].definition()
    return definition

definition_dict = {}

for i in included_hardwords:
    try:
        definition_dict[i[1]] =  get_definition(i[0])
    except:
        pass
    
with open('definition_1000.json', 'w') as json_file:
    json.dump(definition_dict, json_file)
#print(syns[0].definition())

"""           
import csv


with open('WikiNews_Train.tsv','r',errors="ignore") as tsvin, open('new.csv', 'wb') as csvout:
    tsvin = csv.reader(tsvin, delimiter='\t')
    csvout = csv.writer(csvout)

    for row in tsvin:
        if row[9] == '1' and len(row[4].split()) == 1 and row[4].lower() not in hard_words:
            hard_words.append(row[4].lower())
        


counter = 0
translated_qn_and_ans = {}
for i in allquestions:
    try:
        translated_qn_and_ans[i[1]] = translator.translate(i[1],dest='te').text
        counter += 1
        if counter % 20 == 0:
            print(counter, " / ", 1000)
    except:
        translated_qn_and_ans[i[1]] = translator.translate(i[1],dest='te').text
        counter += 1
        if counter % 20 == 0:
            print(counter, " / ", 1000)

           
import io
import json

with io.open('translation_1000_telugu.json', 'w', encoding='utf8') as json_file:
    json.dump(translated_qn_and_ans, json_file, ensure_ascii=False)

""" 

"""
with open("translation.json", "r",encoding='utf-8') as read_file:
    data = json.load(read_file)

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
"""
