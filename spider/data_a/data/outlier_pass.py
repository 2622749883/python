from pymysql import Connect

# 设置数据库的链接
conn = Connect(host="localhost",user="root",password="123456",db="data_for_teacher",charset="utf8")
cursor = conn.cursor()

# 分别设置三个列表用来存放一些列表名字和异常值
table_list = ['algorithm_engineer','android_development','big_data','deep_learning','education','mechine_learning','nature_language_process','operate','operation_maintenance','production_manager','ui_design']
min_salary = [8000,7000,8681.91,7500,6312.56,6500,7215,6016.71,7033.79,8878.38,7956.43]
max_salary = [46288,30978.9,29585.4,52362.2,16672.7,43670,54092.1,22093.3,20427.1,29925.1,25427.8]

# # 循环遍历所有的表，从表中去除异常值
# for i in range(len(table_list)):
#     sql = "select job_name,company_name,salary,address from {}".format(str(table_list[i]))
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     for item in result:
#         if item[2] == None:
#             pass
#         elif item[2]>max_salary[i] or item[2]<min_salary[i]:
#             print(item[2])
#             sql1 = "update "+str(table_list[i])+" set salary=NULL where job_name='"+str(item[0])+"' and company_name='"+str(item[1])+"' and address='"+str(item[3])+"'"
#             print(sql1)
#             cursor.execute(sql1)
#             conn.commit()
