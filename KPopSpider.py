import requests
import re
from  lxml import etree
import os
import time


#15849
urls = []
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
index = 1
class MyStruct:
    """docstring for ClassName"""
    def __init__(self):
        self._title = None
        self._time = None
        self._content = None

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        self._title = title

    
    @property
    def time(self):
        return self._time
    @time.setter
    def time(self,time):
        self._time = time

    
    @property
    def content(self):
        return self._content
    @content.setter
    def content(self,content):
        self._content = content    

def get_many_urls():
    for x in range(1,406):
               url = r'http://www.koreatimes.co.kr/www/sublist_688_'+str(x)+'.html'
               urls.append(url)      

def get_contents(urls):
    index = 1
    for i in range(len(urls)):
        try:
            res = request_web(urls[i])
            s = etree.HTML(res)

            result = s.xpath('//div[@class="list_article_area"]/div[@class="list_article_headline HD"]/a')
            for j in range(len(result)):
                try:
                    vivi = MyStruct()
                    vivi.title = result[j].text
                    url_ = 'http://www.koreatimes.co.kr'+result[j].get('href')
                    html = request_web(url_)
                    s = etree.HTML(html)
                    times = s.xpath('//div[@class="date_div"]/div[@class="view_date"]/text()')
                    date_all = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})",times[0])
                    vivi.time = date_all[0]
                    texts = s.xpath('//div[@id="startts"]//span/text()')
                    str_text = ''.join(texts)
                    vivi.content=str_text
                    str_chain = vivi.title+"#"+vivi.time+'#'+vivi.content
                    save_text(str_chain,str(index)+'.txt')
                    index = index+1
                except:
                    index = index+1
                    print("error")
                    pass
                    
        except:
            index = index+1
            print("ERROR")
    
         
        
        
      
def request_web(url):
    response = requests.get(url,headers = headers)
    html = response.text
    return html

def save_text(text,name):
    with open(name,'w+',encoding='utf-8') as f:
        for i in text:
            f.write(i)
        
os.chdir(r'C:/Users/Administrator/Desktop/korea/text')
if __name__ =='__main__':
    get_many_urls()
    get_contents(urls)
    print("DONE!!")
    
