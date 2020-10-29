import re
import cv2
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

# 显示中文
plt.rcParams["font.sans-serif"]=["FangSong"]
# 显示正负符号
plt.rcParams["axes.unicode_minus"]=False

# 创建画布
figure_ = plt.figure(num="散点图",figsize=(8,20))
# 开始作画
x = [-1,3,4,6,8]
y = [-3,5,7,8,10]
y1 = [-4,-6,7,9,10]

plt.scatter(x,y)
plt.title("这是一张散点图")

figure_1 = plt.figure(num="折线图",figsize=(8,20))
plt.plot(x,y,label="印度")
plt.plot(x,y1,label="中国")
plt.legend()
plt.title("这是一张折线图")

# 设置横纵作表、
plt.xlabel("人口总数增长率",color="red")
plt.ylabel("平均收入",color="yellow")
plt.show()






# 正则表达式的使用

# content = "my name is li_hua and 52 how are you"
#
# result=re.match('my\s(\w{4})\s\w{2}\s\w{6}\s\w{3}\s(\d+).*you$',content)
# result_1=re.match('^my(.*)you$',content)
# result_2=re.match('^my(.*?)you$',content)
#
# print(result.group())
# print(result.group(1))
# print(result.group(2))
# print(result_1.group(1))
# print(result_2.group(1))

# content = "截至9月26日0时，全省累计报告新型冠状病毒肺炎确诊病例685例(其中境外输入144例），累计治愈出院657例，死亡3例，目前在院隔离治疗25例，1007人尚在接受医学观察"
#
# result = re.match('^截至(.*?)，全省.*?例(.*?)例.*?输入(.*?)例.*?院(.*?)例，死亡(.*?)例.*?治疗(.*?)例，(.*?)人.*?观察$',content)
# print(result.group())
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.group(4))
# print(result.group(5))
# print(result.group(6))
# print(result.group(7))

string = """
<dd><span class="number">1</span><a href="/play/49891/454929.shtml" target="m" title="亲爱的小课桌">亲爱的小课桌</a></dd>
<dd><span class="number">2</span><a href="/play/795/454553.shtml" target="m" title="悟空">悟空</a></dd>
<dd><span class="number">3</span><a href="/play/20222/453529.shtml" target="m" title="粉雾海">粉雾海</a></dd>
<dd><span>4</span><a href="/play/46594/453598.shtml" target="m" title="姐姐真漂亮">姐姐真漂亮</a></dd>
<dd><span>5</span><a href="/play/49518/453225.shtml" target="m" title="斯芬克斯">斯芬克斯</a></dd>
"""

# result_s=re.sub('<dd>|</dd>',"",string)
# result_s_1=re.sub('<span.*?>.*?</span>',"",result_s)
# print(result_s_1)
# result_r = re.findall('<dd>.*?href="(.*?)" target.*?>(.*?)</a>', string)

# result_c=re.compile('<a.*?>(.*?)</a>',re.S)
# result_f=re.findall(result_c,string)
# print(result_f)
#
# for item in result_f:
#     print(item)

# img = cv2.imread("1.jpg")
# # print(img)
# #创建一个矩阵
# data = np.array([1,2,3])
# # 矩阵中的最小值
# min_data = data.min()
# # 矩阵中最大值
# max_data = data.max()
# print(min_data,max_data)
#
# one_array = np.ones(3)
# zero_array = np.zeros(10)
# print(one_array,zero_array)
#
# sum_data =data+one_array
# miu_data = data-one_array
# mul_data = data*one_array
# print(sum_data,min_data,mul_data)
#
# data_2 = np.array([[2,2],[1,2]])
# data_3 = np.array([[3,2],[1,5]])
#
# print(data_2,data_3)
# mul_datas = data_2*data_3
# print(mul_datas)