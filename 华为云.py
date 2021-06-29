import requests
from lxml import etree
import  re
from concurrent.futures import ThreadPoolExecutor

def main():
    for page in range(1,10):
        dic=get_data(page)
        paser_data(dic)

#请求数据
def get_data(page):
    params={
        'pageNo': page,
        'pageSize': 10,
        'typeCode': 1,
        'form': -1,
        'contentMode': -1,
        'priceRange': -1,
        'supportOS': -1,
        'productType': -1,
        'tagIds': '',
        'priceStart': -1,
        'priceEnd': -1
        }

    headers={
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
        'wise-groupid': '3.bWFya2V0cGxhY2UuaHVhd2VpY2xvdWQuY29tL3NlYXJjaC9iYXNpY1NvZnR3YXJlL3x8..NNu68VUo.1624961469062',
        'x-language': 'zh-cn',
        'referer': 'https://marketplace.huaweicloud.com/',
        'origin': 'https://marketplace.huaweicloud.com'
    }

    url='https://portal.huaweicloud.com/portalsearchqueryservice/marketplacesearch?'
    res=requests.get(url=url,headers=headers,params=params)
    dic=res.json()
    #请求响应，得到json字符串
    return dic

def paser_data(dic):
#对相应进行每一条数据的解析
    item={}
    for i in range(0,10):
        item['name']=dic['pagination']['items'][i]['title']
        item['content']=dic['pagination']['items'][i]['content']
        item['version']=dic['pagination']['items'][i]['version']
        item['onshelftime']=dic['pagination']['items'][i]['onshelftime']
        item['price']=dic['pagination']['items'][i]['price']    #进行清洗
        item['price']=re.findall('^￥\d+',item['price'])[0]
        item['corporationname'] = dic['pagination']['items'][i]['corporationname']
        #d对网页进行二次的解析
        url1=dic['pagination']['items'][i]['url']
        res1=requests.get(url1)
        #对响应进行二次解析
        tree=etree.HTML(res1.text)
        item['Mode_of_delivery']=tree.xpath('//*[@id="product-description-1"]/span[2]/text()')[0]
        item['detial_description']=tree.xpath('//*[@id="detail-description-desc"]/text()')

        for i in item['detial_description']:
            i.replace(r'\xa0','')
            i.replace(r'\uf06c','')
            i.replace(r'\t', '')
        item['detial_description'] = "".join(item['detial_description'])
        if item['detial_description'].isspace() == True:
            item['detial_description'] = '此商品无详情描述'

        item['phone_num']=tree.xpath('//*[@id="contact-service-provider-tel-0"]/text()')
        if len(item['phone_num']) != 0:
            item['phone_num']= item['phone_num'][0]
        else:
            item['phone_num'] = ''

        item['e_mail']=tree.xpath('//*[@id="contact-service-provider-mail-1"]/text()')
        if len(item['e_mail'])!=0:
            item['e_mail']=item['e_mail'][0]
        else:
            item['e_mail']=''

        print(item)



if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=24)
    future1 = pool.submit(main)
    # main()