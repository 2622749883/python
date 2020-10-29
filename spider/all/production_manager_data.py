import re
import requests
from pymysql import Connect
from bs4 import BeautifulSoup

#设置数据库的连接
conn = Connect(host="localhost",user="root",password="root",db="algorithm_engineer",port=3306,charset="utf8")
cursor = conn.cursor()

# 获取工作数据
def get_html_resources(url,headers):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("获取网站源码出错........")

# 解析网站源码
def parse_detail_page(html,headers):
    parttern = re.compile('engine_search_result":(.*?)</script>',re.S)
    items = re.findall(parttern,html)
    parttern_detail = re.compile('job_href":"(.*?)","job_name":"(.*?)".*?company_name":"(.*?)","providesalary_text":"(.*?)".*?attribute_text":(.*?),"companysize_text',re.S)
    items_detail = re.findall(parttern_detail,items[0])
    for item in items_detail:
        address = []
        education = []
        content = []
        job_url=str(item[0]).replace("\\","")
        job_address_education = str(item[4]).replace('["',"").replace('"]',"").replace('"',"").split(",")
        if len(job_address_education) == 4:
            address.append(job_address_education[0])
            education.append(job_address_education[2])
        if len(job_address_education) == 3:
            address.append(job_address_education[0])
            education.append(job_address_education[1])

        # 开始获取详情页的工作数据
        response = requests.get(job_url,headers=headers)
        response.encoding="gbk"
        if response.status_code == 200:
            detail_html = response.text
            soup = BeautifulSoup(detail_html, "lxml")
            job_request = soup.find("div", class_="bmsg job_msg inbox").text
            content.append(job_request)
        else:
            print("获取详情页的信息错误")
            pass

        yield {
            "工作名称":item[1],
            "公司名称":item[2],
            "工作待遇":item[3],
            "工作地点":address[0],
            "学历要求":education[0],
            "工作要求": content[0],
        }
        try:
            sql = "insert into  production_manager(job_name,company_name,salary,job_request,address,education_requirements) values ('"+item[1]+"','"+item[2]+"','"+item[3]+"','"+content[0]+"','"+address[0]+"','"+education[0]+"');"
            cursor.execute(sql)
            conn.commit()
        except:
            print("数据插入异常............")
            conn.rollback()

    return items

def main():
    headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    for i in range(1070):
        url = "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E4%25BA%25A7%25E5%2593%2581%25E7%25BB%258F%25E7%2590%2586,2,"+str(i+1)+".html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
        try:
            html = get_html_resources(url,headers)
            items = parse_detail_page(html,headers)
            for item in items:
                print(item)
        except:
            print(url)
            print("获取异常")
            pass

if __name__ == "__main__":
    main()