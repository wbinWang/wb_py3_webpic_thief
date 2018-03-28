import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

targetUrl = "http://www.shuaia.net/zhengtai/2017-07-10/1320_2.html"
imgName = "123"
imgReq = requests.get(targetUrl)
imgReq.encoding = "utf-8"
imgReqSoup = BeautifulSoup(imgReq.text , "lxml")
imgReqSoupDiv = imgReqSoup.find_all('div',class_="wr-single-content")
print(imgReqSoupDiv)
divSoup = BeautifulSoup(str(imgReqSoupDiv), "lxml")
imgUrl = "http://www.shuaia.net" + divSoup.div.img.get("src")
print(imgUrl)
# if "images" not in os.listdir():
#     os.makedirs("images")
# urlretrieve(url=imgUrl , filename="images/" + imgName)
# print("下载完成")

