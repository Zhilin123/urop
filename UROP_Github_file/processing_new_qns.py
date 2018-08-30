#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 17:11:55 2018

@author: wangxiujiang
"""

import json

with open("datasets/draw.json","r") as f:
  all_data = json.load(f)
  
all_templates =[]
for i in all_data:
    if i['Template'] not in all_templates:
        all_templates.append(i['Template'])

ops_symbol = ["*","/","+","-"]

all_template_w_ops_num = []
for i in all_templates:
    opsnum = 0
    for j in i:
        for k in ops_symbol:
            opsnum += j.count(k)
    for l in range(len(templates_in_groups)):
        if i in templates_in_groups[0]:
            group = "one_variable"
            hint = "l3XzepN03KQ"
        if i in templates_in_groups[1]:
            group = "one_variable_reciprocal"
            hint = "JUy99Gkc_YQ"
        if i in templates_in_groups[2]:
            group = "one_variable_sequential"
            hint = "nJLImD-LAWk"
        if i in templates_in_groups[3]:
            group = "two_variable"
            hint = "nVuJEidLhY1E"
        if i in templates_in_groups[4]:
            group = "two_variable_reciprocal"
            hint = " WQYzOpcnWxs"
    all_template_w_ops_num.append([i, opsnum,group,hint])

data_to_enter_database = []
for i in all_data:
    question = i['sQuestion']
    answer = i['lSolutions']
    template = i['Template']
    for j in all_template_w_ops_num:
        if template == j[0]:
            template_level_group = j
    data_to_enter_database.append([question,answer]+template_level_group)
    
#can also have difficulty levels

# 1 variable l3XzepN03KQ
# 1 variable sequential JUy99Gkc_YQ
# 1 variable reciprocal nJLImD-LAWk
# 2 variable VuJEidLhY1E
# 2 varibale reciprocal WQYzOpcnWxs

templates_in_groups = [
        #one _variable
        [
             ['-1 * a * m + m = b - a * c'],
             ['0.01 * a * m - 0.01 * b * m = 0.01 * a * c - 0.01 * d * c'],
             ['0.01 * a * m - 0.01 * b * m = 0.01 * b * c - c'],
             ['0.01 * a * m - 0.01 * b * m = c'],
             ['0.01 * a * m - m = 0.01 * a * b - 0.01 * c * b'],
             ['0.01 * a * m = b'],
             ['0.01 * a * m = b - c'],
             ['1 / 2 * a * m = b'],
             ['a * b * m = c - a * d'],
             ['a * m + a * m = b'],
             ['a * m + a * m = b - a * c'],
             ['a * m + b * a * m = c'],
             ['a * m + b * m - c * m = -1 * a * d - b * e'],
             ['a * m + b * m - c * m = d'],
             ['a * m + b * m = b * c - a * c'],
             ['a * m + b * m = c'],
             ['a * m + b * m = c * a + d * b'],
             ['a * m + b * m = c + b * d'],
             ['a * m + b * m = c - d'],
             ['a * m - b * m = -1 * b * c - a * c'],
             ['a * m - b * m = -1 * c - d'],
             ['a * m - b * m = a'],
             ['a * m - b * m = a * c'],
             ['a * m - b * m = a * c + b * c'],
             ['a * m - b * m = a * c - b * c'],
             ['a * m - b * m = b'],
             ['a * m - b * m = b * c'],
             ['a * m - b * m = b * c + a * d'],
             ['a * m - b * m = b * c - c * d'],
             ['a * m - b * m = b * c - d'],
             ['a * m - b * m = b * c - d - e'],
             ['a * m - b * m = b + c'],
             ['a * m - b * m = c'],
             ['a * m - b * m = c + a * d'],
             ['a * m - b * m = c - b * d - e + a * f'],
             ['a * m - b * m = c - d'],
             ['a * m - m = a * b'],
             ['a * m - m = b'],
             ['a * m - m = b - c'],
             ['a * m = b'],
             ['a * m = b * c'],
             ['a * m = b * c - b * a'],
             ['a * m = b + a * c'],
             ['a * m = b + c'],
             ['a * m = b + c - a * c'],
             ['a * m = b - a * c'],
             ['a * m = b - c'],
             ['a * m = b - c * d'],
             ['m + 0.01 * a * m = b'],
             ['m + a * m = b - c'],
             ['m + m = a - 1'],
             ['m - 0.01 * a * m = 0.01 * a * b - 0.01 * c * b'],
             ['m - 0.01 * a * m = 0.01 * a * b - c'],
             ['m - 0.01 * c * m = 0.01 * a * b + a'],
             ['m - a * m - b * m = c'],
             ['m - a * m = -1 * a * b - c'],
             ['m - a * m = -1 * b - c'],
             ['m - a * m = a * b + c'],
             ['m - a * m = a * b + c - d'],
             ['m - a * m = a * b - c'],
             ['m - a * m = b'],
             ['m = 0.01 * a * b - 0.01 * a * c'],
             ['m = a * b - c'],
             ['m = a - b'],
             ['m = a - b - c']
        ],
        # 1 variable reciprocal
        [
             ['1 / a * m + 1 / b * m + 1 / c * m = 1'],
             ['1 / a * m + 1 / b * m - 1 / c * m = 1'],
             ['1 / a * m + 1 / b * m = 1'],
             ['1 / a * m + 1 / b * m = 1 - 1 / a * c'],
             ['1 / a * m + 1 / b * m = c'],
             ['1 / a * m + 1 / b * m = c - d'],
             ['1 / a * m - 1 / b * m = 1'],
             ['1 / a * m - 1 / b * m = c'],
             ['1 / a * m - 1 / b * m = c * 1 / 60'],
             ['a / b * m + c / d * m = e'],
        ],
        #2 variables solve sequentially
        [
             ['2 * m + 2 * m = a', 'm - n = b * 2'],
             ['a * m - b * m = b * c', 'n - a * m = 0'],
             ['a * m - m = -1 * b - a * c', 'm - n = d'],
             ['a * m = b', 'c * m - n = 0'],
             ['m + m= a', 'n - m = b'],
             ['m = a + b', 'm + n = c'],
        ],
        #2 variables simultaneous
        [
             ['0.01 * a * b * m - 0.01 * c * n = 0', 'm + n = d'],
             ['0.01 * a * m + 0.01 * b * n = c', 'd * m - n = e'],
             ['0.01 * a * m + 0.01 * b * n = c', 'm - d * n = 0'],
             ['0.01 * a * m + 0.01 * b * n = c', 'm - n = d'],
             ['0.01 * a * m + 0.01 * b * n = c', 'n + m = d'],
             ['0.01 * a * m - 0.01 * b * n = c', 'm + n = d'],
             ['0.01 * a * m - 0.01 * b * n = c', 'n - m = d'],
             ['0.05 * m + 0.1 * n = a', 'm + n = b'],
             ['10 * m + n - 10 * n - m - a * n - a * m = 0', 'n + m = b'],
             ['10 * m + n - 10 * n - m = -1 * a', '10 * m + n - b * n = 0'],
             ['10 * m + n - 10 * n - m = -1 * a', 'n + m = b'],
             ['10 * m + n - 10 * n - m = a', 'm - b * n = c'],
             ['10 * m + n - a * 10 * n - a * m = -1 * b', 'm + n = c'],
             ['10 * m + n - a * 10 * n - a * m = -1 * b', 'm - n = c'],
             ['10 * m + n - a * 10 * n - a * m = b', 'n + m = c'],
             ['10 * m + n - a * m - a * 10 * n = b', 'm - n = c'],
             ['10 * m + n - a * m - a * n = 0', '10 * m + n - 10 * n + m = -1 * b'],
             ['10 * m + n - a * m - a * n = 0', 'b * n - m = c'],
             ['10 * m + n - a * m - a * n = 0', 'm + n = b'],
             ['10 * m + n - a * m - a * n = 0', 'm - n = b'],
             ['20 * m + 20 * n = a * b', 'm - n = c'],
             ['a * 10 * m + a * n - b * 10 * n - b * m = 0', 'n - m = c'],
             ['a * b * m + c * d * n = e - c * 1', 'a * m + c * n = f'],
             ['a * m +  b * n = c * d', 'n + m = c'],
             ['a * m + 0.01 * b * n = c * d', 'm + n = c'],
             ['a * m + 0.05 * n = b', 'n - c * m = 0'],
             ['a * m + a * n = b', 'a * m - a * n = c'],
             ['a * m + a * n = b', 'c * m - c * n = b'],
             ['a * m + a * n = b', 'c * m - c * n = d'],
             ['a * m + a * n = b', 'c * n - d * m = 0'],
             ['a * m + a * n = b', 'm - c * n = 0'],
             ['a * m + a * n = b', 'm - n = c'],
             ['a * m + a * n = b', 'n - m = c'],
             ['a * m + b * m + a * n = c', 'm - n = d'],
             ['a * m + b * m - a * n = 0', 'n - m = c'],
             ['a * m + b * m - n = a + b - c', 'a * m - n = 0'],
             ['a * m + b * n = -1 * c', 'd * m + e * n = f'],
             ['a * m + b * n = -1 * c', 'd * m - e * n = f'],
             ['a * m + b * n = 0.01 * c', 'm - n = d'],
             ['a * m + b * n = c', 'd * m + e * n = c'],
             ['a * m + b * n = c', 'd * m + e * n = c - f'],
             ['a * m + b * n = c', 'd * m + e * n = f'],
             ['a * m + b * n = c', 'd * m - e * n = f'],
             ['a * m + b * n = c', 'd * m - n = 0'],
             ['a * m + b * n = c', 'd * m - n = e'],
             ['a * m + b * n = c', 'm + d * n = e'],
             ['a * m + b * n = c', 'm + n = 1 / d'],
             ['a * m + b * n = c', 'm + n = d'],
             ['a * m + b * n = c', 'm - n = 0.01 * d'],
             ['a * m + b * n = c', 'm - n = d'],
             ['a * m + b * n = c * d', 'm + n = c'],
             ['a * m + b * n = c - d', 'n - m = e'],
             ['a * m + n - b * m - b * n = 0', 'm - n = c'],
             ['a * m + n = b', 'c * m - n = b'],
             ['a * m + n = b', 'c * m - n = d'],
             ['a * m + n = b', 'm + n = c'],
             ['a * m + n = b', 'n - c * m = 0'],
             ['a * m + n = b', 'n - m = c'],
             ['a * m - 10 * m - n = b', 'm + n = c'],
             ['a * m - a * n - m = b', 'm - c * n = 0'],
             ['a * m - a * n = b', 'm - c * n = d'],
             ['a * m - a * n = b', 'n + m = c'],
             ['a * m - a * n = b', 'n - c * m = 0'],
             ['a * m - b * m + a * n = c', 'm - n = d'],
             ['a * m - b * n - m = c', 'n - m = d'],
             ['a * m - b * n = -1 * c - d', 'm - n = e'],
             ['a * m - b * n = 0', 'm + n = c'],
             ['a * m - b * n = 0', 'm - c * n = d'],
             ['a * m - b * n = 0', 'm - n = c'],
             ['a * m - b * n = b * c', 'd * n - e * m = 0'],
             ['a * m - b * n = b * c - a * c', 'd * m - e * n = 0'],
             ['a * m - b * n = b * c - a * c', 'm - n = d'],
             ['a * m - b * n = c', 'm - d * n = e'],
             ['a * m - b * n = c', 'm - n = d'],
             ['a * m - b * n = c', 'n + m = d'],
             ['a * m - b * n = c', 'n - d * m = 0'],
             ['a * m - b * n = c', 'n - m = d'],
             ['a * m - b * n = c * d', 'n + m = d'],
             ['a * m - b * n = c + d', 'n + m = e'],
             ['a * m - n - b * m - b * n = 0', 'm - n = c'],
             ['a * m - n = -1 * b + a * b', 'm - c * n = d'],
             ['a * m - n = -1 * b + a * b', 'n - m = c'],
             ['a * m - n = b', '0.05 * m + 0.01 * n = c'],
             ['a * m - n = b', 'c * n - m = d'],
             ['a * m - n = b', 'm + n = c'],
             ['a * m - n = b', 'n - m = b'],
             ['a * m - n = b', 'n - m = c'],
             ['m + 0.01 * a * n = 0.01 * b * c', 'n + m = c'],
             ['m + a * n = b', 'n - m = c'],
             ['m + n - a * m = -1 * b', 'm - c * n = d'],
             ['m + n - a * m = -1 * b', 'm - n - c * n = -1 * d'],
             ['m + n - a * m = -1 * b', 'n - c * m = 0'],
             ['m + n - a * n + a * m = 0', 'n - b * m = c'],
             ['m + n - a * n = b', 'n - m = c'],
             ['m + n = 180', 'a * m - n = b'],
             ['m + n = a', '2 * m + 4 * n = b'],
             ['m + n = a', 'm - 3 / 4 * n = b'],
             ['m + n = a', 'm - n = b'],
             ['m + n = a', 'n - b * m = 0'],
             ['m + n = a + b', 'm - n = a'],
             ['m + n = a + b', 'n - c * m = d'],
             ['m + n = a + b + b', 'm - c * n = 0'],
             ['m + n = a + b + b', 'n - m = c'],
             ['m + n = a - b - b', 'm - c * n = d'],
             ['m + n = a - b - b', 'n - m = c'],
             ['m - 0.01 * a * n = 0', 'n - m = b'],
             ['m - 0.01 * a * n = 1', 'm + n = b'],
             ['m - a * n + a * m - a * n = 0', 'm + n = b'],
             ['m - a * n - b * n = -1 * c', 'n - m = d'],
             ['m - a * n = -1 * a * b + b', 'c * m - n = 0'],
             ['m - a * n = -1 * a * b + b', 'm + n = c - d - d'],
             ['m - a * n = -1 * a * b + b', 'm - c * n = 0'],
             ['m - a * n = -1 * a * b + b', 'm - c * n = c * d - d'],
             ['m - a * n = -1 * a * b + b', 'm - c * n = c * d - e - d'],
             ['m - a * n = -1 * a * b + b', 'n - m = c'],
             ['m - a * n = -1 * a * b + c + b', 'm - d * n = 0'],
             ['m - a * n = -1 * a * b - c', 'm + n = d'],
             ['m - a * n = -1 * a * b - c', 'm - d * n = 0'],
             ['m - a * n = -1 * a * b - c', 'm - n = d'],
             ['m - a * n = -1 * b * a + b - c', 'm - d * n = e'],
             ['m - a * n = a * b', 'c * n - m = c * b'],
             ['m - a * n = a * b + b', 'm - c * n = 0'],
             ['m - a * n = a * b + c - b', 'm - d * n = 0'],
             ['m - a * n = a * b - b', 'm - c * n = 0'],
             ['m - a * n = a * b - b', 'm - c * n = d'],
             ['m - a * n = a * b - b', 'm - n = c'],
             ['m - a * n = a * b - b', 'n + m = c'],
             ['m - a * n = a * b - c', 'm - n = d'],
             ['m - a * n = a * b - c - b', 'd * n - m = e'],
             ['m - a * n = a * b - c - b', 'm - d * n = 0'],
             ['m - a * n = b', '2 * m + 2 * n = c'],
             ['m - a * n = b', 'c * n + d * m = e'],
             ['m - a * n = b', 'c * n + m = d'],
             ['m - a * n = b', 'c * n - m = d'],
             ['m - a * n = b', 'm + n = c'],
             ['m - a * n = b', 'm - n = c'],
             ['m - b * n = a - c + b * c', 'm - d * n = e + f - d * f'],
             ['m - n + m = a - b', 'n - m = c'],
             ['m - n - 0.01 * a * n = 0', 'n + m = b'],
             ['m - n = 0', 'a * n - b * m = c'],
             ['m - n = 0', 'm - a * n = -1 * a * b - c'],
             ['m - n = 1', 'n + a * m = b'],
             ['m - n = 10', 'a * m + a * n = b'],
             ['m - n = a', '2 * n + 2 * m = b'],
             ['m - n = a', 'm - b * n = 0'],
             ['m - n = a + b', 'c * m - d * n = 0'],
             ['m - n = a + b', 'm - c * n = 0'],
             ['m - n = a - b', 'c * m - n = 0'],
        ],       
        # 2 variable reciprocal
        [
            ['1 / a * m + 1 / b * n = c', 'n + m = d']
        ]


]

with open('questions_to_upload.json', 'w') as json_file:
    json.dump(data_to_enter_database, json_file)