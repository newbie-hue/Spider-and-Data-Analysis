import requests
import re
import csv


url='https://movie.douban.com/top250'
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}
resp=requests.get(url,headers=headers)

obj=re.compile(r'<li>.*?<div class="item">.*?<a href=".*? <span class="title">(?P<name>.*?)</span>'
               r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;/&nbsp;.*?<span class="rating_num" property="v:average">'
               r'(?P<score>.*?)</span>.*?<span property="v:best" content="10.0"></span>'
               r'.*?<span>(?P<num>.*?)人评价</span>',re.S)
f=open('data.csv',"w",encoding='utf-8')

resu=obj.finditer(resp.text)
with open('data.csv','w',newline='',encoding='utf-8') as f:
    csvwriter=csv.writer(f)
    for item in resu:
        print(item.group('name'))
        print(item.group('year').strip())
        print(item.group('score'))
        print(item.group('num'))
        dic=item.groupdict()
        dic['year']=dic['year'].strip()
        csvwriter.writerow(dic.values())

