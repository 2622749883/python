from pymysql import Connect# 设置数据库的链接
conn = Connect(host="localhost",user="root",password="123456",db="data_for_teacher",charset="utf8")
cursor = conn.cursor()

table_list = ['algorithm_engineer','android_development','big_data','deep_learning','education','mechine_learning','nature_language_process','operate','operation_maintenance','production_manager','ui_design']
for i in range(len(table_list)):
    print("******************************"+str(table_list[i])+"****************************")
    sql_2 = "update "+str(table_list[i])+" set salary=(min_salary+max_salary)/2"
    cursor.execute(sql_2)
    conn.commit()