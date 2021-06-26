

"""
1、http://book.sbkk8.com/gudai/sidawenxuemingzhu/xiyouji/
抓取里面的网页
2、然后使用网页进行异步的下载
"""
import requests
import asyncio
import aiohttp
from lxml import etree
import os


async def download(url):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as resp:
            #print(await resp.text(encoding='gbk'))
            tree=etree.HTML(await resp.text(encoding='gbk'))
            title=tree.xpath('/html/body/div[5]/h1/text()')
            content=tree.xpath('/html/body/div[5]/div[1]//text()')
            content_=''.join(content)
            #print(title,content_)
            with open("C:\\Users\\sunshine\\Desktop\\图片\\西游记\\"+title[0]+'.txt','a+',encoding='utf-8') as f:
                    content_.replace('\r', '').replace('\n', '')
                    f.write(title[0]+content_)


async def main():
    url='http://book.sbkk8.com/gudai/sidawenxuemingzhu/xiyouji/'
    html=requests.get(url)
    html.encoding='gb2312'
    tree=etree.HTML(html.text)
    n='http://book.sbkk8.com/'
    urls=tree.xpath('/html/body/div[5]/div[1]/div[2]/ul//a/@href')
    tasks=[]
    for i in urls:
        urls_=n+i
        tasks.append(asyncio.create_task(download(urls_)))

    await asyncio.wait(tasks)



if __name__ == '__main__':
    asyncio.run(main())
    print('over')
