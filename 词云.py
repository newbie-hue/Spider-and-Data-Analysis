
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS



# 读取文件
filename = r"C:\Users\sunshine\Desktop\课件\图片\爬取的数据\hertz.txt"
with open(filename, 'r',encoding='utf-8') as f:
    text = f.read()

# 设置停止词
stop_words = set(STOPWORDS)
word_cloud = WordCloud(background_color='white', max_words=200, stopwords=stop_words)
word_cloud.generate(text)

plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
plt.show()
