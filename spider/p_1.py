import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
def get_html(url):
    url = url
    response = requests.get(url,headers=headers)
    response.encoding = "gbk"
    if response.status_code == 200:
        html = response.text
        pattern = re.compile('<div class="bmsg job_msg inbox">(.*?)<div class="mt10">', re.S)
        items = re.findall(pattern,html)
        content = re.sub("<p>|</p>", "", items[0])
        content = re.sub("<br>", "", content)
        return content
    else:
        print("有错")

# content = get_html('https://jobs.51job.com/guangzhou/124906095.html?s=01&t=0')
# print(content)