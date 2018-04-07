from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.np_extractors import ConllExtractor
import pymysql
import sys


# 打开数据库连接
db =  pymysql.connect("localhost","root","3327","final_project" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql ="SELECT * FROM final_project.guardian_asia_pacific where date between '2017/1/1' and '2017/12/31';" 
list1 = []

if(len(sys.argv)>2):
   sss = sys.argv[1]+' '+sys.argv[2]
else:
   sss= sys.argv[1]
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      _ID = row[0]
      _DATE = row[1]
      _TITLE = row[2]
      _CONTENT = row[3]
      if(sss == 'South Korea'):
         if(sss in _CONTENT and 'North Korea' not in _CONTENT):
            list1.append(_CONTENT)
      else:
         if(sss in _CONTENT):
            list1.append(_CONTENT)
      
except:
   print ("Error: unable to fetch data")
 
# 关闭数据库连接
db.close()
sum= 0;
count = 0;
for str1 in list1:
   arr = str1.split('.')
   for s in arr:
      sblob=TextBlob(s)
      sum+=sblob.sentiment.polarity
      count+=1
     
print("Sentiment of [ %s ] is : %.5f "%(sss,sum/count))




