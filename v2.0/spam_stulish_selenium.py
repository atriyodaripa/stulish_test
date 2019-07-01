
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:47:57 2018

Modified on Monday July 1 - Soumalya Saha

@author: Anirban Das
"""
import markovify

from selenium import webdriver
import time, csv

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--headless")
options.add_argument("--test-type")
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(options=options)


#reload(sys)  
#sys.setdefaultencoding('utf8')

def spam_stulish(username, message):
    url = "http://travelangkawi.com/" + username
    driver.get(url)
    text_area = driver.find_element_by_id('Text')
    text_area.send_keys(message)

    # click submit button
    submit_button = driver.find_elements_by_xpath('//*[@id="Send"]')[0]
    submit_button.click()
    
# =============================================================================
#     #uncomment if you want the response webpage
#     content = res.read()
#     with open("mechanize_results.html", "w") as f:
#         f.write(content)
#     print(res)
#     
# =============================================================================



spam_limit = 20
#username = "soumalya01" # e.g. : username = "joydeepiimv"

# Get raw text as string.
with open("book.txt") as f:
    text = f.read()
# Build the model.
text_model = markovify.Text(text)

for i in range(spam_limit):
    str1=text_model.make_sentence()
    print (str1)
    with open('listSt.csv','rt')as fl:
        lists = csv.reader(fl)
        for name in lists:
            spam_stulish(name[0], str1)
            time.sleep(2) #don't sleep if you want to spam Joydeep
