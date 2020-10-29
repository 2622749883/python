from bs4 import BeautifulSoup
import requests

def get_html(url):
    reponse = requests.get(url)
    reponse.encoding = 'UTF-8'
    if reponse.status_code == 200:
        return reponse.text
    else:
        print("链接错误")
def main():
    # url = "http://eecs.pku.edu.cn/rcpy1/yjspy.htm"
    url = "http://www.sicnu.edu.cn/#"
    html = get_html(url)
    print(html)
    soup = BeautifulSoup(html,"html.parser")
    print(soup.find_all("a",class_="fl nowrap"))
    for item in soup.find_all("a",class_="fl nowrap"):
        print(item.get("href"))
        print(item.get_text())

if __name__ == '__main__':
    main()
