# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import urllib.request
import requests

import re
import datetime
from datetime import time

def f_bs(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")
    a=bsObj.find_all("table", class_='main')

    for i in a:
        text=i.get_text()
        cntNum=text.count('平常どおり運転しています。')
        if not cntNum==9:
            return text # なにかあった
        else:
            return False # 平穏


runTime=[5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23, 0]
count = 0

while True:
    dt_now = datetime.datetime.now()
    time=dt_now
    hour=dt_now.hour

    print (hour, hour in runTime, sep='\n')
    bool=hour in runTime

    if bool==True:
        url='http://tra-rep.tobu.jp/index.html'
        ans=f_bs(url)

        if not ans==False:
            txt=ans.replace('\n\n', '\n')
            txt=txt.replace('平常どおり運転しています。', '【平常どおり運転しています。】')
            print(txt)
        else:
            print ('平常ダイヤ')
            break

    count+=1
    if count==3:
        print ('緊急回避が発動')
        break

    import time
    time.sleep(10)

print ("done", sep='\n')
