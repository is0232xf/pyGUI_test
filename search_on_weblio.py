# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:07:24 2019

@author: FujiiChang
"""

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from operator import itemgetter

def search_on_weblio(search_words, min_level, max_level, sort):
    result_list = []
    for word in tqdm(search_words):
        # make url of each search word
        url = "https://ejje.weblio.jp/content/" + word 
        # send request to url
        r = requests.get(url)    
        # extract texts from web site
        soup = BeautifulSoup(r.content, "html.parser")        
        # if there is no word mean on weblio, the mean of word is assigned None
        mean_text = soup.find("div", class_="summaryM descriptionWrp")
        if mean_text is None:
            mean_text = "None"
        else:
            mean_text = mean_text.text
        
        # if there is no word levcel on weblio, the level of word is assigned level 99
        word_level = (soup.find("span", class_="learning-level-content"))
        if word_level is None:
            word_level = 99
        else:
            word_level = int(word_level.text)
    
        result_set = (word, mean_text, word_level)
        if min_level <= result_set[2] <= max_level:
            result_list.append(result_set)
    if sort is True:
        result_list = sorted(result_list, key=itemgetter(2))
    return(result_list)
