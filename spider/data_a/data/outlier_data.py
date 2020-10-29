import pandas as pd
import matplotlib.pyplot as plt
#主要用来设置坐标的刻度
from matplotlib.pyplot import MultipleLocator

# 读取excel表格数据
data1 = pd.read_excel("finance.xlsx",index_col="min_salary")
data2 = pd.read_excel("medical.xlsx",index_col="min_salary")
# data3 = pd.read_excel("big_data.xls",index_col="min_salary")
# data4 = pd.read_excel("deep_learning.xls",index_col="min_salary")
# data5 = pd.read_excel("education.xls",index_col="min_salary")
# data6 = pd.read_excel("mechine_learning.xls",index_col="min_salary")
# data7 = pd.read_excel("nature_language_process.xls",index_col="min_salary")
# data8 = pd.read_excel("operate.xls",index_col="min_salary")
# data9 = pd.read_excel("operation_maintenance.xls",index_col="min_salary")
# data10 = pd.read_excel("production_manager.xls",index_col="min_salary")
# data11 = pd.read_excel("ui_design.xls",index_col="min_salary")

# 打印出各种工作类型的统计数据
# print("********************算法工程师工资数据分布***************")
# print(data1.describe())
# print("********************android开发工资数据分布***************")
# print(data2.describe())
# print("********************大数据开发工资数据分布***************")
# print(data3.describe())
# print("********************深度学习工资数据分布***************")
# print(data4.describe())
# print("********************教育类工作工资数据分布***************")
# print(data5.describe())
# print("********************机器学习工资数据分布***************")
# print(data6.describe())
# print("********************自然语言处理工资数据分布***************")
# print(data7.describe())
# print("********************web开发工资数据分布***************")
# print(data8.describe())
# print("********************运维工资数据分布***************")
# print(data9.describe())
# print("********************产品经理工资数据分布***************")
# print(data10.describe())
# print("********************UI设计师工资数据分布***************")
# print(data11.describe())

# 设置图像的字体以及设置图像显示正负号
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

# 创建画布
figure = plt.figure(num="金融异常值检测")
# 给图像设置一个标题
plt.title("金融异常值检测",fontsize=14,color="blue")

# 设置一些，x轴y轴的刻度
y_major_locator=MultipleLocator(30000)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator)
plt.ylim([0,550000])

# 画箱型图，直接采用DataFrame的方法
p1 = data1.boxplot(return_type='dict',sym='r.')

# fliers即为异常值的标签
x = p1['fliers'][0].get_xdata()
y = p1['fliers'][0].get_ydata()

# y的值由大到小的顺序进行排序
y.sort()

plt.ylabel("工资分布",fontsize=14,color="blue")
plt.xlabel("字段名称",fontsize=14,color="blue")

# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i>0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))

# 创建画布
figure2 = plt.figure(num="医学异常值检测")
plt.title("医学异常值检测",fontsize=14,color="blue")

# 设置一些，x轴y轴的刻度
y_major_locator=MultipleLocator(30000)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major_locator)
plt.ylim([0,550000])

# 画箱型图，直接采用DataFrame的方法
p1 = data2.boxplot(return_type='dict',sym='r.')

# fliers即为异常值的标签
x = p1['fliers'][0].get_xdata()
y = p1['fliers'][0].get_ydata()

# y的值由大到小的顺序进行排序
y.sort()

plt.ylabel("工资分布",fontsize=14,color="blue")
plt.xlabel("字段名称",fontsize=14,color="blue")

# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i>0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))

# # 创建画布
# figure3 = plt.figure(num="大数据开发异常值检测")
# plt.title("大数据开发异常值检测",fontsize=14,color="blue")
#
# # 设置一些，x轴y轴的刻度
# y_major_locator=MultipleLocator(30000)
# ax=plt.gca()
# ax.yaxis.set_major_locator(y_major_locator)
# plt.ylim([0,550000])
#
# # 画箱型图，直接采用DataFrame的方法
# p1 = data3.boxplot(return_type='dict',sym='r.')
#
# # fliers即为异常值的标签
# x = p1['fliers'][0].get_xdata()
# y = p1['fliers'][0].get_ydata()
#
# # y的值由大到小的顺序进行排序
# y.sort()
#
# plt.ylabel("工资分布",fontsize=14,color="blue")
# plt.xlabel("字段名称",fontsize=14,color="blue")
#
# # 使用annotate来对图像进行添加注释
# for i in range(len(x)):
#     if i>0:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
#     else:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
#
# # 创建画布
# figure4 = plt.figure(num="深度学习异常值检测")
# plt.title("深度学习异常值检测",fontsize=14,color="blue")
#
# # 设置一些，x轴y轴的刻度
# y_major_locator=MultipleLocator(30000)
# ax=plt.gca()
# ax.yaxis.set_major_locator(y_major_locator)
# plt.ylim([0,550000])
#
# # 画箱型图，直接采用DataFrame的方法
# p1 = data4.boxplot(return_type='dict',sym='r.')
#
# # fliers即为异常值的标签
# x = p1['fliers'][0].get_xdata()
# y = p1['fliers'][0].get_ydata()
#
# # y的值由大到小的顺序进行排序
# y.sort()
# plt.ylabel("工资分布",fontsize=14,color="blue")
# plt.xlabel("字段名称",fontsize=14,color="blue")
#
# # 使用annotate来对图像进行添加注释
# for i in range(len(x)):
#     if i>0:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
#     else:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
#
# # 创建画布
# figure5 = plt.figure(num="教育类工作异常值检测")
# plt.title("教育类工作异常值检测",fontsize=14,color="blue")
#
# # 设置一些，x轴y轴的刻度
# y_major_locator=MultipleLocator(30000)
# ax=plt.gca()
# ax.yaxis.set_major_locator(y_major_locator)
# plt.ylim([0,550000])
#
# # 画箱型图，直接采用DataFrame的方法
# p1 = data5.boxplot(return_type='dict',sym='r.')
#
# # fliers即为异常值的标签
# x = p1['fliers'][0].get_xdata()
# y = p1['fliers'][0].get_ydata()
#
# # y的值由大到小的顺序进行排序
# y.sort()
# plt.ylabel("工资分布",fontsize=14,color="blue")
# plt.xlabel("字段名称",fontsize=14,color="blue")
#
# # 使用annotate来对图像进行添加注释
# for i in range(len(x)):
#     if i>0:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
#     else:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
#
# # 创建画布
# figure6 = plt.figure(num="机器学习工作异常值检测")
# plt.title("机器学习异常值检测",fontsize=14,color="blue")
#
# # 设置一些，x轴y轴的刻度
# y_major_locator=MultipleLocator(30000)
# ax=plt.gca()
# ax.yaxis.set_major_locator(y_major_locator)
# plt.ylim([0,550000])
#
# # 画箱型图，直接采用DataFrame的方法
# p1 = data6.boxplot(return_type='dict',sym='r.')
#
# # fliers即为异常值的标签
# x = p1['fliers'][0].get_xdata()
# y = p1['fliers'][0].get_ydata()
#
# # y的值由大到小的顺序进行排序
# y.sort()
# plt.ylabel("工资分布",fontsize=14,color="blue")
# plt.xlabel("字段名称",fontsize=14,color="blue")
#
# # 使用annotate来对图像进行添加注释
# for i in range(len(x)):
#     if i>0:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
#     else:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
#
# # 创建画布
# figure7 = plt.figure(num="自然语言处理工作异常值检测")
# plt.title("自然语言异常值检测",fontsize=14,color="blue")
#
# # 设置一些，x轴y轴的刻度
# y_major_locator=MultipleLocator(30000)
# ax=plt.gca()
# ax.yaxis.set_major_locator(y_major_locator)
# plt.ylim([0,550000])
#
# # 画箱型图，直接采用DataFrame的方法
# p1 = data7.boxplot(return_type='dict',sym='r.')
#
# # fliers即为异常值的标签
# x = p1['fliers'][0].get_xdata()
# y = p1['fliers'][0].get_ydata()
#
# # y的值由大到小的顺序进行排序
# y.sort()
# plt.ylabel("工资分布",fontsize=14,color="blue")
# plt.xlabel("字段名称",fontsize=14,color="blue")
#
# # 使用annotate来对图像进行添加注释
# for i in range(len(x)):
#     if i>0:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
#     else:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
#
# # 创建画布
# figure9 = plt.figure(num="运维工作异常值检测")
# plt.title("运维工作异常值检测",fontsize=14,color="blue")
#
# # 设置一些，x轴y轴的刻度
# y_major_locator=MultipleLocator(30000)
# ax=plt.gca()
# ax.yaxis.set_major_locator(y_major_locator)
# plt.ylim([0,550000])
#
# # 画箱型图，直接采用DataFrame的方法
# p1 = data9.boxplot(return_type='dict',sym='r.')
#
# # fliers即为异常值的标签
# x = p1['fliers'][0].get_xdata()
# y = p1['fliers'][0].get_ydata()
#
# # y的值由大到小的顺序进行排序
# y.sort()
# plt.ylabel("工资分布",fontsize=14,color="blue")
# plt.xlabel("字段名称",fontsize=14,color="blue")
#
# # 使用annotate来对图像进行添加注释
# for i in range(len(x)):
#     if i>0:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
#     else:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
#
# figure8 = plt.figure(num="web开发工作异常值检测")
# plt.title("web开发工作异常值检测",fontsize=14,color="blue")
#
# # 设置一些，x轴y轴的刻度
# y_major_locator=MultipleLocator(30000)
# ax=plt.gca()
# ax.yaxis.set_major_locator(y_major_locator)
# plt.ylim([0,550000])
#
# # 画箱型图，直接采用DataFrame的方法
# p1 = data8.boxplot(return_type='dict',sym='r.')
#
# # fliers即为异常值的标签
# x = p1['fliers'][0].get_xdata()
# y = p1['fliers'][0].get_ydata()
#
# # y的值由大到小的顺序进行排序
# y.sort()
# plt.ylabel("工资分布",fontsize=14,color="blue")
# plt.xlabel("字段名称",fontsize=14,color="blue")
#
# # 使用annotate来对图像进行添加注释
# for i in range(len(x)):
#     if i>0:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
#     else:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
#
# # 创建第10张表格
# figure10 = plt.figure(num="产品经理异常值检测")
# plt.title("产品经理异常值检测",fontsize=14,color="blue")
#
# # 设置一些，x轴y轴的刻度
# y_major_locator=MultipleLocator(30000)
# ax=plt.gca()
# ax.yaxis.set_major_locator(y_major_locator)
# plt.ylim([0,550000])
#
# # 画箱型图，直接采用DataFrame的方法
# p1 = data10.boxplot(return_type='dict',sym='r.')
#
# # fliers即为异常值的标签
# x = p1['fliers'][0].get_xdata()
# y = p1['fliers'][0].get_ydata()
#
# # y的值由大到小的顺序进行排序
# y.sort()
# plt.ylabel("工资分布",fontsize=14,color="blue")
# plt.xlabel("字段名称",fontsize=14,color="blue")
#
# # 使用annotate来对图像进行添加注释
# for i in range(len(x)):
#     if i>0:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
#     else:
#         plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
#
# # 创建第11张表格
# figure11 = plt.figure(num="UI设计师异常值检测")
# plt.title("UI设计师异常值检测",fontsize=14,color="blue")
#
# # 设置一些，x轴y轴的刻度
# y_major_locator=MultipleLocator(30000)
# ax=plt.gca()
# ax.yaxis.set_major_locator(y_major_locator)
# plt.ylim([0,550000])
#
# # 画箱型图，直接采用DataFrame的方法
# p1 = data11.boxplot(return_type='dict',sym='r.')
#
# # fliers即为异常值的标签
# x = p1['fliers'][0].get_xdata()
# y = p1['fliers'][0].get_ydata()
#
# # y的值由大到小的顺序进行排序
# y.sort()
# plt.ylabel("工资分布",fontsize=14,color="blue")
# plt.xlabel("字段名称",fontsize=14,color="blue")

# 使用annotate来对图像进行添加注释
for i in range(len(x)):
    if i>0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))

plt.show()