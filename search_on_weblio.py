# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:07:24 2019

@author: FujiiChang
"""

import requests
from bs4 import BeautifulSoup

def search_on_weblio(search_words):
    result_list = []
    for word in search_words:
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
        level = (soup.find("span", class_="learning-level-content"))
        if level is None:
            level = 99
        else:
            level = int(level.text)
    
        result_set = (word, mean_text, level)
        print(result_set)
        result_list.append(result_set)
    return(result_list)
