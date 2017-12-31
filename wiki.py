#此程序爬取维基百科的主要上的所有词条，并输出词条对应名称和url
#引入开发包
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


#请求URL并把结果用UTF-8编码
resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8") #打开维基百科的主页 并用utf-8编码
soup = BeautifulSoup(resp, "html.parser")   #引入BS解析器
listUrls = soup.findAll("a", href=re.compile("^/wiki/"))  #用正则表达式模糊匹配查找所有的"/wiki"的词条
for url in listUrls:   #用循环摘出来那些href的
   if not re.search("\.(jpg|JPG)$",url["href"]):# 再逐个过滤，上面的输出里面还有一些.jpg的，并不是我们想要的。
     print(url.get_text(), "<--->","https://en.wikipedia.org"+url["href"])
