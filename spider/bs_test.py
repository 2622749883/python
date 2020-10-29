from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 把不规则的html代码转化成规则的
soup = BeautifulSoup(html_doc,"html.parser")
# .prettify()缩进
print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.head)
# print(soup.a)
# print(soup.p)
# print(soup.p.string)
# print(soup.find_all('a'))
# for item in soup.find_all('a'):
#     print(item)
# print(soup.find(id="link1"))
# for item in soup.find_all('a'):
#     print(item.get("id"))
print(soup.get_text())


