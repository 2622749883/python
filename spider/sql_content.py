import pymysql

# 打开数据库
try:
    db = pymysql.connect(host="localhost",user="root",password="root",database="spider_1",charset='utf8')
except:
    print("数据库连接失败")