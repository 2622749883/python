import pandas as pd
import matplotlib.pyplot as plt
#主要用来设置坐标的刻度
from matplotlib.pyplot import MultipleLocator

# 读取excel表格数据
data = pd.read_excel("operate.xls",index_col="max_salary")
print(len(data))
print(data.describe())

# 创建画布
figure = plt.figure(num="异常值检测")

# 设置图像的字体以及设置图像显示正负号
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

plt.title("异常值检测",fontsize=18,color="red")

# 设置一些，x轴y轴的刻度
# y_major_locator=MultipleLocator(40000)
# ax=plt.gca()
# ax.yaxis.set_major_locator(y_major_locator)
# plt.ylim([0,550000])

# 画箱型图，直接采用DataFrame的方法
p = data.boxplot(return_type='dict')

# fliers即为异常值的标签
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()

# y的值由大到小的顺序进行排序
y.sort()

# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i>0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))

plt.show()
