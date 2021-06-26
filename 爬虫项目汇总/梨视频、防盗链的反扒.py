#1、拿到contid
#2、拿到videoStatus返回的json.->  srcURL
#3、srcURL里面的内容进行修整  成为src
#4、下载视频

import requests


url="https://www.pearvideo.com/video_1731253"
contID=url.split("_")[1]


videoStatus=f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.1439190374449233"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Cookie":"__secdyid=0f41d0262006d0b31968d5c88769daa2df68409fa6084e95021622815510; acw_tc=76b20f4316228155101423983e4711fbffe30112131ed2eeeb54cb88ff6047; JSESSIONID=DDBE22CF0FB70CF42DCD429215865C30; PEAR_UUID=a59220d2-0472-4705-bd25-403465b55b93; _uab_collina=162281551309942960271009; UM_distinctid=179d7579fafb-01a4416c1ec026-57442618-144000-179d7579fb062; CNZZDATA1260553744=1690517977-1622811263-https%253A%252F%252Fwww.baidu.com%252F%7C1622811263; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1622815515; p_h5_u=0E520F02-6A99-4542-BB7C-0F1C630A2CCD; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1622815518; SERVERID=ed8d5ad7d9b044d0dd5993c7c771ef48|1622815789|1622815510",
    "Referer": url
}
resp=requests.get(videoStatus,headers=headers)
dic=resp.json()
srcURL=dic["videoInfo"]["videos"]["srcUrl"]
systemTime=dic["systemTime"]
url_=srcURL.replace(systemTime,"cont-"+contID)

with open(r'C:\Users\sunshine\Desktop\图片\i'+contID+".mp4","ab+") as f:
    f.write(requests.get(url_).content)
print('over')
