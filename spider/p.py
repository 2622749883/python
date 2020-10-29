import requests
import re
import p_1
from pymysql import Connect


# 连接数据库
connect = Connect(host="localhost",user="root",password="root",database="spider_1",charset="utf8",port=3306)
# 设置一个游标，用来操作数据库
cursor = connect.cursor()
def get_html(url,headers):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("失败")
# 正则表达式匹配工作数据
def parse_content(content):
    pattern = re.compile('window.__SEARCH_RESULT__ = {(.*?)<table',re.S)
    result = re.findall(pattern,content)
    return result[0]

# 匹配具体的工作信息
def pare_content_detail(result):
    pattern = re.compile('"job_href":"(.*?)","job_name":"(.*?)",.*?,"company_name":"(.*?)","providesalary_text":"(.*?)"', re.S)
    items = re.findall(pattern, result)
    for item in items:
        p_c = p_1.get_html(str(item[0]).replace("\\", ""))
        p_c = re.sub("\r\n","",p_c)
        p_c = re.sub("&nbsp;","",p_c)
        p_c = re.sub("<span.*?>|</span>","",p_c)
        p_c = re.sub("<div>|</div>","",p_c)
        p_c = re.sub("<b>|</b>","",p_c)
        p_c = re.sub("<li>|</li>","",p_c)
        salary = str(item[3]).replace("\\", "")
        yield {
            "工作名称" : item[1],
            "公司名称" : item[2],
            "具体薪资" : salary,
            "工作要求" : p_c,
        }
        sql = "insert into jobinfo(job_name,company_name,salary,job_request) values ('"+item[1]+"','"+item[2]+"','"+salary+"','"+p_c+"');"
        cursor.execute(sql)
        connect.commit()
    return items


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
    for i in range(763):
        try:
            url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,'"+str(i+1)+"'.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
            print("******************************"+str(i+1)+"********************")
            content = get_html(url,headers)
            reuslt=parse_content(content)
            re=pare_content_detail(reuslt)
            for item in re:
                print(item)
        except:
            print("dded")
if __name__ == '__main__':
    main()