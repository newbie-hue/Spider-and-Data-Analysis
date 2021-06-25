import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import jieba
from wordcloud import WordCloud,STOPWORDS
from PIL  import  Image
jieba.setLogLevel(jieba.logging.INFO)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

#建立停用词
stop_words=set(STOPWORDS)

with open(r"C:\Users\sunshine\Desktop\课件\图片\爬取的数据\stop_words.txt",'r',encoding='utf-8') as f:
    stop_words.add(f.read())


#统计文件的读取成为字符串

###数据处理
#读取数据
df=pd.read_csv(r'C:/Users/sunshine/Desktop/课件/图片/爬取的数据/' + '淘宝' + '口红'+'.csv')
#降序排列
df1=df.sort_values('sum_body',ignore_index=True)
#删除重复值
df2=df1.drop_duplicates()
#重置索引
df2.index = range(len(df2))
#用平均值替换缺失值
df3=df2.fillna(df2.mean())

data=df3['shop_name'].values
data="".join(data)


#对统计文本进行分词处理
cut_list=jieba.lcut(data)
#对每一个分词进行处理
def fiter_word(words,stop_words):
        num=re.search('\d+',words)
        if num==None:
            if words not in stop_words:
                if len(words)>1:
                    return words
            else:
                pass
        else:
            pass

#对文本进行次数的统计
word_freq=dict()
for one in cut_list:
    # print(list(one))
    row=fiter_word(one,STOPWORDS)
    if row:
        word_freq[row]=word_freq.get(row,0)+1
# print(word_freq)

#使用图片背景
mask=np.array(Image.open(r'C:\Users\sunshine\Desktop\课件\图片\爬取的数据\背景.png'))
wc=WordCloud(font_path=r'C:\Windows\Fonts\simkai.ttf',background_color='white',max_font_size=100,max_words=200,margin=1,random_state=1,stopwords=stop_words)
wc.generate_from_frequencies(word_freq)
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()





