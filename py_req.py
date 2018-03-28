import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve

#获取最大页码
def parserShuaiaOneImgSetPages(url):
    req = requests.get(url)
    req.encoding = "utf-8"
    reqSoup = BeautifulSoup(req.text , "lxml")
    pagination = reqSoup.find_all("div" , class_="pagination")
    # print(pagination)
    pageSoup = BeautifulSoup(str(pagination) , "lxml")
    pageSoupA = pageSoup.find_all("a")
    pages = []
    pages.append(url)
    for a in pageSoupA:
        href = str(a.get("href"))
        if href.endswith(".html",0,len(href)):
            if href not in pages:
                pages.append(href)
    # print(pages)
    return pages

#解析单个集合
def parseShuaiaOneImageSet(url):
    req = requests.get(url)
    req.encoding = "utf-8"
    reqSoup = BeautifulSoup(req.text , "lxml")
    reqDiv = reqSoup.find_all("div",class_="wr-single-content-list")
    divSoup = BeautifulSoup(str(reqDiv) , "lxml")
    # print(divSoup)
    imgUrl = "http://www.shuaia.net" + divSoup.div.img.get("src")
    imgName= imgUrl.split("/")[-1]
    downloadImage(imgUrl , imgName)

#下载图片方法
def downloadImage(url , filePath):
    dir = "images"
    print(url)
    if dir not in os.listdir():
        os.makedirs(dir)
    urlretrieve(url=url , filename=dir + "/" + filePath)
    print("下载完成")
    

#解析shuaia
def parserShuaiaHome(maxPage):
    for i in range(1,maxPage):
        if i == 1:
            url = 'http://www.shuaia.net/index.html'
        else:
            url = 'http://www.shuaia.net/index_%d.html' % i
        req = requests.get(url)
        req.encoding = "utf-8"
        htmlText = req.text
        print("page index=%d------------------page index" % i)
        soup = BeautifulSoup(htmlText , "lxml")
        itemImage = soup.find_all(class_="item-img")
        for item in itemImage:
            pages = parserShuaiaOneImgSetPages(item.get('href'))
            for page in pages:
                parseShuaiaOneImageSet(page)

if __name__ == "__main__":
    parserShuaiaHome(2)
    