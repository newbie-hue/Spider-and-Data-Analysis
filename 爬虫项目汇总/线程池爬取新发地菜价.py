#线程池：一次性开辟一些线程，我们用户直接给线程池提交任务
#线程任务的调度交给线程池完成



from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from bs4 import BeautifulSoup
import requests
import csv
from concurrent.futures import ThreadPoolExecutor

def main(url):
        ask=askURL(url)
        f = open('菜价.csv', 'a+', newline='', encoding='utf-8')
        csvwriter = csv.writer(f)
        getDAta(ask,csvwriter)
        print(url+ '提取完成')
        f.close()




#1、请求网页，得到源代码
def askURL(url):
    res=requests.get(url)
    return res.text


#2、解析源代码
def getDAta(ask,csvwriter):
    html=BeautifulSoup(ask,'html.parser')
    table=html.find('table',class_='hq_table')
    row=table.find_all('tr')[1::]
    for i in row:
        td=i.find_all("td")
        name1=td[0].string
        name2=td[1].string
        name3=td[2].string
        name4=td[3].string
        name5=td[4].string
        name6=td[5].string
        name7=td[6].string
        csvwriter.writerow([name1,name2,name3,name4,name5,name6,name7])


if  __name__=='__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1,100):
            url = f'http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml'
            t.submit(main,url)
    print('over')