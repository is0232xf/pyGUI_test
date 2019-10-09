# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:09:41 2019

@author: FujiiChang
"""


import nltk
import os
from nltk.corpus import wordnet as wn

nltk.download('all')
category_list = ["NN", "NNS", "VB", "VBG", "VBD", "VBN", "VBN", "VBP", "JJ", "RB"]

def split_sentence(sentence):
    split_sentence = str(sentence)
    split_sentence = split_sentence.split(" ")
    return split_sentence

def exclude_special_characters(data_lines):
    data_lines = data_lines.replace("-", "")
    data_lines = data_lines.replace("-\n", "")
    data_lines = data_lines.replace("\n", " ")
    data_lines = data_lines.replace(",", "")
    data_lines = data_lines.replace(".", "")
    data_lines = data_lines.replace("(", "")
    data_lines = data_lines.replace(")", "")
    data_lines = data_lines.replace("[", "")
    data_lines = data_lines.replace("]", "")
    data_lines = data_lines.replace("%", "")
    data_lines = data_lines.replace(":", "")
    data_lines = data_lines.replace(";", "")
    data_lines = data_lines.replace("&", "")
    data_lines = data_lines.replace("”", "")
    data_lines = data_lines.replace("“", "")
    data_lines = data_lines.replace("/", "")
    data_lines = data_lines.replace("'", "")
    return data_lines

def make_list(text_dir, input_file):   
    whole_data = []
    large_whole_data = []    
    new_data = []
    
    for input_text in input_file:
        path = text_dir + "/" + input_text
        print("path: ", path)
        with open(path, "r") as myfile:
            data=myfile.read()
            data = data.split('. ')
            large_whole_data = large_whole_data + data
    
            for i in range(len(data)):
                data[i] = data[i].lower()
            whole_data = whole_data + data

    for sentence in whole_data:
        data = split_sentence(sentence)
        for num in range(len(data)):
            data[num] = exclude_special_characters(data[num])
            original_word = wn.morphy(data[num])
            if len(data[num]) > 2:
                if original_word == None:
                    new_data.append(data[num])
                else:
                    new_data.append(original_word)
            else:
                pass
    
    fdist1 = nltk.FreqDist(new_data)
    
    common_list = fdist1.most_common(1000) # 多い単語と数を出力
    word_list = []
    
    for i in range(len(common_list)):
        if common_list[i][1] > 2:
            word_list.append(common_list[i][0])
    tagged_word_list = nltk.pos_tag(word_list[1:1000]) # 上位500をタグ付け
    important_words = []
    
    for j in range(len(tagged_word_list)):
        if tagged_word_list[j][1] in category_list:
            important_words.append(tagged_word_list[j]) # 必要な品詞タグが付いた単語だけを取り出す
    
    word_result = []
    
    for k in range(len(important_words)):
        word_result.append(important_words[k][0])
    return word_result