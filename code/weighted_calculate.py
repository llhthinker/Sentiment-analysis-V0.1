# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 15:32:30 2017

@author: liulo
"""
from pyltp import Segmentor
from pyltp import SentenceSplitter
import csv
import time

def get_weibos_by_name(name):
    input_file = '../input_data/data_new.csv'
    start_time = time.time()
    weibos = {}
    count = 0
    with open(input_file, encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[8] == name:
                new_weibo = row[2]+'\n'
                send_time = row[3]
                weibos[send_time] = new_weibo
                count = count + 1
    weibo_list = sorted(weibos.items(), key=lambda d:d[0])
    end_time = time.time()
    print("time cost of get weibos: %.2fs" % (end_time-start_time))
    print("weibo count: ", count)
    return weibo_list

def weightedCalc(weibo):
    score = 0
    for sentence in weibo:
        word_list = sentence.split(' ')
        sen_score = 0
        weight = 1
        for word in word_list:
            if len(word) in pos_dict and word in pos_dict[len(word)]:
                # print('pos:'+word+" "+str(weight))
                sen_score += weight
                weight = 1
            if len(word) in neg_dict and word in neg_dict[len(word)]:
                # print('neg:' + word + " " + str(weight))
                sen_score -= weight
                weight = 1
            if word in adv_degree:
                weight *= adv_degree[word]
            if word in inversion_word:
                # print("-1:" + word)
                weight *= -1
        score += sen_score
    return score

pos_dict_file = "../dict/pos_dict.txt"
pos_f = open(pos_dict_file, 'r', encoding='utf-8')
pos_dict = {}
for line in pos_f:
        lines=line.split('\n')
        length = len(lines[0])
        if length > 0:
            if length not in pos_dict.keys():
                pos_dict[length] = []
            if lines[0] not in pos_dict[length]:
                pos_dict[length].append(lines[0])
pos_f.close()

neg_dict_file = "../dict/neg_dict.txt"
neg_f = open(neg_dict_file, 'r', encoding='utf-8')
neg_dict = {}
for line in neg_f:
        lines=line.split('\n')
        length = len(lines[0])
        if length > 0:
            if length not in neg_dict.keys():
                neg_dict[length] = []
            if lines[0] not in neg_dict[length]:
                neg_dict[length].append(lines[0])
neg_f.close()

adv_degree_file = "../dict/adv_of_degree.txt"
adv_degree_f = open(adv_degree_file, 'r', encoding='utf-8')
adv_degree = {}
level = 4
for line in adv_degree_f:
    if line == '\n':
        level -= 1
    else:
        line = line.strip()
        if level == 4:
            adv_degree[line] = 2
        if level == 3:
            adv_degree[line] = 1.75
        if level == 2:
            adv_degree[line] = 1.5
        if level == 1:
            adv_degree[line] = 0.5
adv_degree_f.close()

inversion_word = ['不', '没', '无', '非', '莫', '弗', '毋', '未', '否', '别',
                  '無', '休', '不曾', '未必', '没有', '不要', '难以', '未曾']

# qetina    Gogo-MR0033   LiverpoolSaintyGerrard  小小奸细    lo小乖ve  管宝程   yinyin5366
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

draw_data = []
name = "Gogo-MR0033"
weibos = get_weibos_by_name(name)
cws_model = "F:/ltp_data/cws.model"
segmentor = Segmentor()
segmentor.load(cws_model)
date_index = []
for weibo in weibos:
    weibo_list = []
    sentences = SentenceSplitter.split(weibo[1])
    for s in sentences:
        words = segmentor.segment(s)
        text = " ".join(words)
        weibo_list.append(text)
    print(weibo_list)
    draw_data.append(weightedCalc(weibo_list))
    date_index.append(weibo[0])
segmentor.release()

df = pd.DataFrame(draw_data, index=date_index, columns=['Emotion Score'])

df.index = pd.to_datetime(df.index).to_period(freq='S')
p = df.plot(kind='bar', title=name+'\' emotion swings')
plt.show(p)
