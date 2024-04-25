#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import yagmail
import pandas
import datetime
import time
from sender import NewsFeed

def send_email():

    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days = 1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest = rows['interest'], 
                         from_date = yesterday, 
                         to_date = today  )
    email = yagmail.SMTP(user = "annmariasalin.misc@gmail.com", password = "izxr vbci fvaw dyas")
    email.send(to = rows["email"], 
               subject = f"Your {rows['interest']} news for today",
               contents = f"Hi {rows['name']},\n see what's on about {rows['interest']} today.\n {news_feed.get()} \n Thanks",
               attachments = "design.txt")

while True:
    if datetime.datetime.now().hour == 15 and datetime.datetime.now().minute == 39:
        df = pandas.read_excel('people.xlsx')
        for index, rows in df.iterrows():
            send_email()

    time.sleep(10)

