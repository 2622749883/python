import requests
import re

def get_page_html(url):
    # headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
    response = requests.get(url)
    if response.status_code == 200:
        parttern=re.compile('<ul id="info-list-ul" class="unstyled news">(.*?)</ul>',re.S)
        items=re.findall(parttern,response.text)
        print(items)
        # print(response.text)
        return items[0]
    else:
        print("有问题")

def parse_datail_page(html):
    parttern=re.compile('<a href="(.*?)" title',re.S)
    items=re.findall(parttern,html)
    for i in items:
        print("http://www.ss.pku.edu.cn"+i)
    return items

def get_content(u):
    reponse=requests.get(u)
    if reponse.status_code == 200:
        parttern=re.compile('<div class="article-content">(.*?)</div>',re.S)
        itmes=re.findall(parttern,reponse.text)
        print(itmes)
        return reponse.text
    else:
        print("出错")

def main():
    url = "http://www.ss.pku.edu.cn/index.php/admission/admnotice?start=0"
    html=get_page_html(url)
    urls=parse_datail_page(html)
    for u in urls:
        url_detail="http://www.ss.pku.edu.cn"
        detail=get_content(url_detail+u)
        print(detail)

if __name__=="__main__":
    main()