from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

def main():
    #启动谷歌驱动
    #会开会话
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    #option.add_argument('--headless')
    web= webdriver.Chrome(options=option)
    web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
       "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
    })
    web.get('https://login.taobao.com/member/login.jhtml')
    print('==============正在进行登录==============')

    #进行模拟登录,进入已购界面
    #输入账号和密码,进行登录
    web.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('18273192354')
    web.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('18273192354')
    web.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
    print('==========登陆成功==============')
    #进入已购界面
    web.maximize_window()
    WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bought"]')))
    element=web.find_element_by_xpath('//*[@id="bought"]')
    web.execute_script("arguments[0].click();", element)
    print('============进入已购页面==============')

    #滑倒页面低端
    # web.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    # 获得总共的页面数
    WebDriverWait(web,20).until(EC.presence_of_element_located((By.XPATH,r'//*[@id="tp-bought-root"]/div[19]/div[2]/ul/li[8]/a')))
    page_sum=web.find_element_by_xpath('//*[@id="tp-bought-root"]/div[19]/div[2]/ul/li[8]/a').text
    print('=======正在爬取第1页==========')
    parse(web)
    for i in range(2,int(page_sum)):
        print('=======正在爬取第'+str(i)+'页==========')

        try:
            try:
                #找到输入翻页的地方，然后清除
                web.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(2)
                # WebDriverWait(web,20).until(EC.element_to_be_clickable
                #                                 ((By.XPATH,'//*[@id="tp-bought-root"]/div[19]/div[2]/ul/div/div/input')))
                num=web.find_element_by_xpath('//*[@id="tp-bought-root"]/div[19]/div[2]/ul/div/div/input')
                num.clear()
                num.send_keys(i)
                web.find_element_by_xpath('//*[@id="tp-bought-root"]/div[19]/div[2]/ul/div/div/span[3]').click()
                time.sleep(3)
                WebDriverWait(web, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="tp-bought-root"]/div[19]/div[2]/ul/li[8]/a')))
                parse(web)

            except Exception as e:
                time.sleep(2)
                # WebDriverWait(web,20).until(EC.element_to_be_clickable
                #                                 ((By.XPATH,'//*[@id="tp-bought-root"]/div[19]/div[2]/ul/div/div/input')))
                num = web.find_element_by_xpath('//*[@id="tp-bought-root"]/div[18]/div[2]/ul/div/div/input')
                num.clear()
                num.send_keys(i)
                web.find_element_by_xpath('//*[@id="tp-bought-root"]/div[18]/div[2]/ul/div/div/span[3]').click()
                time.sleep(3)
                WebDriverWait(web, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="tp-bought-root"]/div[18]/div[2]/ul/li[8]/a')))
                parse(web)

        except Exception as e:
            # 防止出现滑块的验证
            xpath_ = web.find_element_by_xpath('//*[@id="baxia-dialog-content"]')
            web.switch_to.frame(xpath_)
            action = ActionChains
            drag = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
            action(web).drag_and_drop_by_offset(drag, 300, 0).perform()
            web.switch_to.frame(
                web.find_element_by_xpath('//*[@id="J_xiaomi_dialog"]/div[2]/div/iframe"]'))
            print(e, '出现滑块验证')


def parse(web):
        div_list=web.find_elements_by_xpath('//*[@id="tp-bought-root"]/div')[3:19]
        for div in div_list:
            try:
                buy_time=div.find_element_by_xpath('./div/table//tr/td[1]/label/span[2]').text
                order_num=div.find_element_by_xpath('./div/table//tr/td[1]/span/span[3]').text
                goods_name=div.find_element_by_xpath('./div/table//tr/td[1]/div/div[2]/p[1]/a/span[2]').text
                goods_prices=div.find_element_by_xpath('./div/table//tr/td[5]/div/div[1]/p/strong/span[2]').text
                shop_name=div.find_element_by_xpath('./div/table//tr/td[2]/span/a').text
                print(buy_time, order_num, goods_name, goods_prices, shop_name)
            except:
                pass


       # buy_time, order_num, goods_name, goods_prices, shop_name






if __name__ == '__main__':
   main()