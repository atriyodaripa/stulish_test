
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:47:57 2018

@author: Anirban Das
"""
import mechanize
import markovify
import time
import sys  

#reload(sys)  
#sys.setdefaultencoding('utf8')

def spam_stulish(username, message):
    url = "http://stulish.com/" + username
    br = mechanize.Browser()
    br.set_handle_robots(False) # ignore robots
    br.open(url)
    for frm in br.forms():
        br.form = frm
    #br.select_form()
    br["Text"] = message.encode('utf-8')
    print(br)
    res = br.submit()
# =============================================================================
#     #uncomment if you want the response webpage
#     content = res.read()
#     with open("mechanize_results.html", "w") as f:
#         f.write(content)
#     print(res)
#     
# =============================================================================



spam_limit = 10
username = "lalbalpal"#"<whoever you want to spam>" # e.g. : username = "joydeepiimv"

# Get raw text as string.
with open("book.txt") as f:
    text = f.read()
# Build the model.
text_model = markovify.Text(text)

for i in range(spam_limit):
    spam_stulish(username, "SDfadsfADSFADSFS")#text_model.make_sentence())
    break
    time.sleep(1) #don't sleep if you want to spam Joydeep