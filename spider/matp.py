import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import xlrd

# 创建一张画布
figure_ = plt.figure(num="折线图",figsize=(10,6),dpi=100)
# 设置图像显示中文和正负号
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
# 读取excel表格中的数据
wb = xlrd.open_workbook("beijing.xlsx")
ws = wb.sheet_by_name("Sheet1")
# 定义一张列表用于存放年份
year_ = []
bejing = []
shanghai = []
shenzheng = []
sichuan = []
# 分别获取一列的数据
years = ws.col_values(0)
for year in years:
    year_.append(int(year))
print(year_)
# 分别获取二列的数据
bejing_ = ws.col_values(1)
for item in bejing_:
    bejing.append(int(item))
print(bejing)
# 读取excel表格上海中的数据
wb = xlrd.open_workbook("shanghai.xlsx")
ws = wb.sheet_by_name("Sheet1")
# 分别获取二列的数据
shanghai_ = ws.col_values(1)
for item in shanghai_:
    shanghai.append(int(item))
print(shanghai)
# 读取excel表格深圳中的数据
wb = xlrd.open_workbook("shenzheng.xlsx")
ws = wb.sheet_by_name("Sheet1")
# 分别获取二列的数据
shenzhen_ = ws.col_values(1)
for item in shenzhen_:
    shenzheng.append(int(item))
print(shenzheng)
# 读取excel表格四川中的数据
wb = xlrd.open_workbook("sichuang.xlsx")
ws = wb.sheet_by_name("Sheet1")
# 分别获取二列的数据
sichuan_ = ws.col_values(1)
for item in sichuan_:
    sichuan.append(int(item))
print(sichuan)

# 设置x、y轴的刻度
y_major_locator = MultipleLocator(4000)
x_major_locator = MultipleLocator(1)
ax = plt.gca()
# 把y轴的主刻度设置为4000的倍数
ax.yaxis.set_major_locator(y_major_locator)
ax.xaxis.set_major_locator(x_major_locator)
plt.xlim([year_[0],year_[-1]])
plt.ylim([0,120000])
# 为图像中的每个点，添加注释
for i in range(len(year_)):
    plt.annotate(s=bejing[i],xy=(year_[i],bejing[i]),xytext=(year_[i]+0.1,bejing[i]+1),fontsize=10,color="red")
    plt.annotate(s=shanghai[i],xy=(year_[i],shanghai[i]),xytext=(year_[i]+0.1,shanghai[i]+1))
    plt.annotate(s=shenzheng[i],xy=(year_[i],shenzheng[i]),xytext=(year_[i]+0.1,shenzheng[i]+1))
    plt.annotate(s=sichuan[i],xy=(year_[i],sichuan[i]),xytext=(year_[i]+0.1,sichuan[i]+1))
# 给x,y轴各定义一个名称
plt.xlabel("年份",color="red",size=15)
plt.ylabel("平均工资",color="blue",size=15)
# 开始绘画图像
plt.plot(year_,bejing,marker='.',label="北京")
plt.plot(year_,shanghai,marker='.',label="上海")
plt.plot(year_,shenzheng,marker='.',label="深圳")
plt.plot(year_,sichuan,marker='.',label="四川")
plt.title("各省历年工资分布图",color="black",size=15)
plt.legend()
plt.savefig("各省历年工资分布图.png")
plt.show()