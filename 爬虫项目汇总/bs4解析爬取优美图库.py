#encoding='utf-8'

#1、拿到主页面的源代码，然后提取到企业民的链接地址，herf
#2、通过herf拿到子页面的内容，从子页面中找到图片的下载地址  img->src
#3、下载图片




import  requests
from bs4 import BeautifulSoup
import  time

def main():
    url=f'''https://www.umei.net/meinvtupian/index_3.htm'''
    res=askURL(url)             #第一次进行请求，获得网页的源代码
    getData(res)
    print('all over!')


def getData(res):  #解析第一次请求得到的页面
    html=BeautifulSoup(res,'html.parser')
    li=html.find('div',class_='TypeList').find_all('img')
    for i in li:
        img=i.get('src')
        p=requests.get(img)
        jpg=p.content
        nam=img.split('/')[-1]
        with open(r'C:\Users\sunshine\Desktop\图片\i'+nam,"ab+") as f:
            f.write(jpg)
        print(nam,'over')
        time.sleep(1)



def askURL(url):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"

    }
    res=requests.get(url,headers=headers)
    res.encoding='UTF-8'
    return  res.text


if __name__ == '__main__':
    main()