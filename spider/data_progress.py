from pymysql import Connect
import re
# 连接数据库
conn = Connect(host="localhost",user="root",password="root",database="spider_1",charset="utf8",port=3306)

# 建立游标对象
cursor = conn.cursor()

# 读取salary的数据
sql = "select salary,id from jobinfo;"

cursor.execute(sql)
result = cursor.fetchall()
min_salary = []
max_salary = []
for item in result:
    salary = str(item[0])
    if "万/月" in salary:
        salary = salary.replace("万/月", "")
        salary = salary.split("-", 2)
        salary[0] = int(float(salary[0]) * 10000)
        salary[1] = int(float(salary[1]) * 10000)
        sql1 = "UPDATE jobinfo set min_salary='"+str(salary[0])+"',max_salary='"+str(salary[1])+"' where id='"+str(item[1])+"';"
        cursor.execute(sql1)
        conn.commit()

    if "千/月" in salary:
        salary = salary.replace("千/月", "")
        salary = salary.split("-", 2)
        salary[0] = int(float(salary[0]) * 1000)
        salary[1] = int(float(salary[1]) * 1000)
        sql1 = "UPDATE jobinfo set min_salary='"+str(salary[0])+"',max_salary='"+str(salary[1])+"' where id='"+str(item[1])+"';"
        cursor.execute(sql1)
        conn.commit()