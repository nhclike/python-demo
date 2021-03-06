#需要调用的requests 库和 BeautifulSoup库中的bs4工具
import requests
from bs4 import BeautifulSoup
num=0 #定义条数的初始值
#定义一个变量url，为需要爬取数据我网页网址
url = 'https://movie.douban.com/subject/26683723/comments?status=P'
#获取这个网页的源代码，存放在req中，{}中为不同浏览器的不同User-Agent属性，针对不同浏览器可以自行百度
req = requests.get(url,{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
#生成一个Beautifulsoup对象，用以后边的查找工作
soup = BeautifulSoup(req.text,'lxml')
#找到所有p标签中的内容并存放在xml这样一个类似于数组队列的对象中
xml = soup.find_all('p')
#利用循环将xml[]中存放的每一条打印出来

for i in range(len(xml)):#表示从0到xml的len()长度
    msg = xml[i].string
    if not msg is None:
        num += 1
        print('第', num, '条', msg)
