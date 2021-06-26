#coding:utf-8

import requests
from bs4 import BeautifulSoup



def download_page(url):
    headers={
        'User - Agent':"Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 86.0.4240.198  Safari / 537.36"
    }  #模拟请求登录
    r=requests.get(url,headers=headers)
    return r.text

def get_content(html,page):
    output='''第{}页  作者:{}性别:{}年龄:{}点赞：{}\n{}\n----------\n\n'''
    soup=BeautifulSoup(html,'html.parser')
    con=soup.find('div',id='content')
    con_list=con.find_all('div',class_='article')
    for i in con_list:
       # hot_comments = i.find('div', class_='main-text').get_text() # 获取热评
        vote = i.find('i', class_='number').string  # 点赞数
        author=i.find('h2').string       #获得作者的名字
        content=i.find('div',class_='content').find('span').get_text()  #获取内容
        author_info=i.find('div',class_='artciGender') #获取性别，年龄等
        if author_info is not None:
            class_list=author_info['class']
            if 'womenIcon' in class_list:
                 gender='女'
            elif 'manIcon' in class_list:
                 gender='男'
            else:
                gender=''
            age=author_info.string
        else:
            gender=''
            age=''
        save_txt(output.format(page,author,gender,age,vote,content,))#hot_comments

def save_txt(*args):
    for i in args:
        with open('qiubai.txt','a',encoding='utf-8') as f:
            f.write(i)




def main():
        for i in range(1,14):
            url=f'''https://www.qiushibaike.com/text/page/{i}/'''
            html=download_page(url)
            get_content(html, i)

if __name__ == '__main__':
    main()


