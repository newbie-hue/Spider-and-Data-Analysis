#coding:"utf-8"


from selenium.webdriver import Chrome
import time
import xlwt




#1、请求数据
web=Chrome()
web.get('https://www.douyu.com/directory/all')

#2、解析数据

data=[]
web.execute_script("var q=document.documentElement.scrollTop=100000")
time.sleep(4)
#web.implicitly_wait(20)
li_list=web.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li')
#print(li_list)
for li in li_list:
    temp={}
    temp['title']=li.find_element_by_xpath('./div/a/div[2]/div[1]/h3').text
    temp['type']=li.find_element_by_xpath('./div/a/div[2]/div[1]/span').text
    temp['owner']=li.find_element_by_xpath('./div/a/div[2]/div[2]/h2/div').text
    temp['num']=li.find_element_by_xpath('./div/a/div[2]/div[2]/span').text
    temp['img']=li.find_element_by_xpath('./div/a/div[1]/div[1]/img').get_attribute('src')
    data.append(temp)
    print(temp)

# #3、保存数据
def data_list(data_list):
    pass