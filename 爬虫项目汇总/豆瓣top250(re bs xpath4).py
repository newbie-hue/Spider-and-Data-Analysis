'''爬取豆瓣前50%的电影以及基本信息'''
#html和css基础
#名称、评分、评价数、电影概况、电影链接

from  bs4 import BeautifulSoup  #网页解析，获取数据
import re    #正则表达式进行文字匹配
import urllib.request,urllib.error   #制定URL，获取网页数据
import xlwt     #进行Excel操作
import sqlite3           #进行SQLLit数据库操作
import time


def main():
    baseurl="https://movie.douban.com/top250?start="
    #1，获取网页
    datalist=getData(baseurl)
    #2.解析数据（逐一解析数据）
    #3.保存数据
    savepath=r"豆瓣电影top250.xls"
    saveData(datalist,savepath)

#获取影片链接的规则
findlink=re.compile(r'<a href="(.*?)">')   #生成、创建正则表达式，表示规则（字符串模式）
#获取图片的链接
findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S)  #re.s忽略里面的换行情况
#影片的片名
findtitle=re.compile(r'<span class="title">(.*)</span>')
#影片的评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#找到评价人数
findJudge=re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findTnq=re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)

'''爬取网页'''
def getData(baseurl):
    datalist=[]       #逐一解析
    for i in range(0,10):
        url=baseurl+str(i*25)   #调用获取页面信息的函数.10次
        html=askURL(url)  #保存回去哦到的网页源码
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):   #查找符合要求的字符串，形成列表。
             #print(item.txt)  #测试查看item全部信息
             data=[]   #保存一部电影的所有信息
             item=str(item)
             #电影的详情链接
             link=re.findall(findlink,item)[0]  #re库用来查找指定的字符串findlink,item   link获取到影片详情的链接
             data.append(link)
             #添加图片的链接
             imgSrc=re.findall(findImgSrc,item)[0]
             data.append(imgSrc)
             #添加电影名字
             titles=re.findall(findtitle,item)   #片名可能只有一个中文名
             if len(titles)==2:
                ctitle=titles[0]            #添加中文名
                data.append(ctitle)         #添加非中文名
                otitle=titles[1].replace("/","")
                data.append(otitle)
             else:
                data.append(titles[0])
                data.append('')   #留空
            #评分
             rating=re.findall(findRating,item)[0]
             data.append(rating)
            #评价人数
             judgeNum=re.findall(findJudge,item)[0]
             data.append(judgeNum)
            #找到概述
             inq=re.findall(findTnq,item)
             if len(inq)!=0:
                inq=inq[0].replace('。','')
                data.append(inq)
             else:
                data.append('')
            #相关内容
             bd=re.findall(findBd,item)[0]
             bd=re.sub('<br(\s+)?/>(\s+?)','',bd)#去掉
             bd=re.sub('/','',bd)  #替换
             data.append(bd.strip())   #去掉前后的空格
             datalist.append(data)    #把处理好的一部电影信息放入到datalist
    return datalist


'''得到一个指定的url网页信息和内容'''
def askURL(url):
    head={  #模拟浏览器头部信息，向豆瓣服务器发送信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }   #用户代理表示告诉豆瓣我们是什么类型的机器和浏览器，本质上是告诉浏览器我们能够接受什么水平的内容
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        time.sleep(1)
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):   #判断e,里面是否有错误代码
            print(e.code)
        if hasattr(e,"reason"):    #判断对象e是否有获取错误的原因
            print(e.reason)
    return html




'''保存数据'''
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)  # 创建工作表 ,覆盖以前的内容。
    col=("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])   #写完列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])  #数据


    book.save("豆瓣电影Top250.xls")  # 保存数据


if __name__ == '__main__':   #调用函数   #ctrl+?   可以将多行代码转为注释
    main()
    print("爬取完毕")