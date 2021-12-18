from re import search
from bs4 import BeautifulSoup
import requests
import time
import json
import os.path
import numpy as np

BASE_URL = 'https://www.nationalforests.org/our-forests/find-a-forest'
PATH = r"C:/Users/yuxinspc/Documents/SI 507/HW/final_project"
FILE_NAME="forests_html.jason"
CACHE_FILE_NAME = os.path.join(PATH, FILE_NAME)         

CACHE_DICT = {}


def load_cache():
    try:
        cache_file = open(CACHE_FILE_NAME, 'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache


def save_cache(cache):
    cache_file = open(CACHE_FILE_NAME, 'w')
    contents_to_write = json.dumps(cache)
    cache_file.write(contents_to_write)
    cache_file.close()


def make_url_request_using_cache(url, cache):
    if (url in cache.keys()): # the url is our unique key
        print("Using cache")
        return cache[url]
    else:
        print("Fetching")
        time.sleep(1)
        response = requests.get(url)#
        cache[url] = response.text
        save_cache(cache)
        return cache[url]



def deal_with_text(t):
#---------------------------------------------------
# turn the text block into splited word list
# Input:
#   t - the text string from the url link
# Output:
#   w - cleaned word list
#---------------------------------------------------
    ct = ''
    for i in t.rstrip():
        if(i == '\n'):
            continue
        else:
            ct += i 
    w = ct.split()
    return w



def find_text_idx(t, l):
#---------------------------------------------------
# find the idx of a word(with punctuation mark) in the wrod list
# Input:
#   t - the text
#   l - the string list
# Output:
#   idx - the index list of the text
#---------------------------------------------------
    idx = np.where(np.array(l) == t+',')[0]
    idx = np.concatenate((idx,np.where(np.array(l) == t+')')[0]), axis = None)
    idx = np.concatenate((idx,np.where(np.array(l) == t+'.')[0]), axis = None)
    idx = np.concatenate((idx,np.where(np.array(l) == t)[0]), axis = None)
    idx = np.concatenate((idx,np.where(np.array(l) == t+']')[0]), axis = None)
    idx = np.concatenate((idx,np.where(np.array(l) == t+'?')[0]), axis = None)
    idx = np.concatenate((idx,np.where(np.array(l) == t+';')[0]), axis = None)
    idx = np.concatenate((idx,np.where(np.array(l) == t+':')[0]), axis = None)

    return idx




def find_forest_size(l):
#---------------------------------------------------
# find the size of forest
# Input:
#   l - the word list 
# Output:
#   forest_size - a number
#---------------------------------------------------  
    acres_idx = find_text_idx('acres', l)
    acre_idx = find_text_idx('acre', l)
    acres_idx = np.concatenate((acre_idx ,acres_idx),axis = None)
    acre_num_idx = np.array(acres_idx - 1)
    acre_num = []
    for i in acre_num_idx:
        num = ''
        for j in l[i]:
            if j.isdigit() :
                num = num + j
            else:
                continue  
        if len(num)>0: 
            acre_num.append(int(num))
        else:
            return None
    if len(acre_num)>0:
        forest_size = max(acre_num)
    else:
        return None
    return forest_size


FORESTS_DATA = "forests_data.jason"

#if __name__ == "__main__":
def store_data():
    CACHE_DICT = load_cache()
    page = requests.get(BASE_URL) 
    soup = BeautifulSoup(page.content, 'html.parser')
    url_body = 'https://www.nationalforests.org/our-forests/find-a-forest/'
    
#-------------------------------------------------
#read the links of all forests into a list
    forest_url_list = [] # store the forests url link
    #forests = [] # store the name of the forests
    for link in soup.find_all('a'):
        if link.get('href')[:58] == url_body:
            cur_url = link.get('href')
            #forests.append(cur_url[58:])
            forest_url_list.append(cur_url)
        else:
            continue
#-------------------------------------------------
    forests_dict = {} # the dictionary to store the information of forests
    forest_dict = {}# the dictionary to store the information of one forest
    count = 0
    forest_text = []
    for url in forest_url_list:
        forest_page = make_url_request_using_cache(url, CACHE_DICT)#requests.get(url) #
        forest_soup = BeautifulSoup(forest_page, 'html.parser')
        forest_text.append(forest_soup.get_text())
        state_list = forest_soup.findAll('div', class_='block-col col-12 col-md-6 offset-lg-1 col-lg-6 text-compact')
        state = state_list[0].findAll('p', class_='mt-0')
        state = state[0].findAll('a')
        state_name = []
        for element in state:
            state_name.append(element.text)
        count += 1
        #print(count)

        cleaned_text = deal_with_text(forest_text[count - 1])
        forest_dict["size"] = find_forest_size(cleaned_text)

        camping_idx = find_text_idx('camping', cleaned_text)
        fishing_idx = find_text_idx('fishing', cleaned_text)

        forest_dict["fishing"] = len(fishing_idx)
        forest_dict["camping"] = len(camping_idx)
        forest_dict["state"] = state_name#extract_state(cleaned_text)

        #print(forest_dict)
        
    #for i in range(len(forests)):
        forests_dict[url[58:]] = forest_dict.copy()
    #print(forests_dict)
    cache_file = open(FORESTS_DATA, 'w')
    contents_to_write = json.dumps(forests_dict,indent = 2)
    cache_file.write(contents_to_write)
    cache_file.close()