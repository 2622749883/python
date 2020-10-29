import matplotlib.pyplot as plt  # 绘图用的模块
from mpl_toolkits.mplot3d import Axes3D  # 绘制3D坐标的函数
import mpl_toolkits.axisartist as axisartist
from matplotlib.pyplot import MultipleLocator
import numpy as np


# def fun(x, y):
#    return np.power(x, 2) + np.power(y, 2)
#
#
# fig1 = plt.figure()  # 创建一个绘图对象
# ax = Axes3D(fig1)  # 用这个绘图对象创建一个Axes对象(有3D坐标)
# X, Y = np.mgrid[-2:2:40j, -2:2:40j]  # 从-2到2分别生成40个取样坐标，并作满射联合
# Z = fun(X, Y)  # 用取样点横纵坐标去求取样点Z坐标
# plt.title("This is main title")  # 总标题
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, alpha=0.5)  # 用取样点(x,y,z)去构建曲面
# ax.set_xlabel('x label', color='r')
# ax.set_ylabel('y label', color='g')
# ax.set_zlabel('z label', color='b')  # 给三个坐标轴注明
# plt.show()  # 显示模块中的所有绘图对象


# 设置数值的取值范围
theta = np.linspace(-2*np.pi,2*np.pi,num=1000,endpoint=True)
y1 = np.sin(theta)
y2 = np.cos(theta)
y3 = np.tan(theta)

# 开始创建画布
fig = plt.figure(num="三角函数图像",figsize=(10,5),dpi=120)
plt.rcParams['font.sans-serif']=['FangSong']
plt.rcParams['axes.unicode_minus']=False

# 使用axisartist.Subplot方法创建一个绘画区对象ax
ax = axisartist.Subplot(fig,111)
# 将绘画区对象添加到布画中
fig.add_axes(ax)

# 通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis[:].set_visible(False)

# 使用ax.new_floating_axis代表添加新的坐标轴
ax.axis['x'] = ax.new_floating_axis(0,0)
# 同时给x轴添加上箭头
ax.axis['x'].set_axisline_style("->",size=1.0)
ax.axis['y']=ax.new_floating_axis(1,0)
ax.axis['y'].set_axisline_style("->",size=1.0)

# 显示x.y的刻度方向
ax.axis['x'].set_axis_direction('bottom')
ax.axis['y'].set_axis_direction('left')
# 设置x,y轴的刻度以及距离
# 定义x轴的数据
x_labels=['',r'$-2π$', r'$-\frac{3π}{2}$', r'$-π$', r'$-\frac{π}{2}$', '', r'$\frac{π}{2}$', r'$π$', r'$\frac{3π}{2}$', r'$2π$']
plt.xticks((-2.1*np.pi,-2*np.pi,-1.5*np.pi,-1.0*np.pi,-0.5*np.pi,0*np.pi,0.5*np.pi,1.0*np.pi,1.5*np.pi,2.0*np.pi),x_labels)

# 设置y轴的显示刻度
y_major_locator = MultipleLocator(0.2)
tx = plt.gca()
tx.yaxis.set_major_locator(y_major_locator)
plt.plot(theta,y1,color='red',label="y=sinx")
plt.plot(theta,y2,color='blue',label="y=cosx")
plt.plot(theta,y3,color='yellow',label="y=tanx")
plt.ylim(-1.1,1.1)

plt.annotate("y=sin(x)",xy=(np.pi/2,1.0),xytext=(np.pi,1.2),arrowprops=dict(color='red',shrink=0.1,width=2))
plt.annotate('y=cos(x)',xy=(np.pi,-1.0),xytext=(np.pi/4,-1.2),arrowprops=dict(color='blue',shrink=0.1,width=2))
plt.annotate('y=tan(x)',xy=(np.pi,-1.0),xytext=(np.pi/4,-1.2),arrowprops=dict(color='blue',shrink=0.1,width=2))

# 为图像添加辅助线
plt.axhline(y=1.0,xmin=0,xmax=1,color="black",linestyle="--",linewidth=0.5)
plt.axhline(y=-1.0,xmin=0,xmax=1,color="black",linestyle="--",linewidth=0.5)
plt.text(2.28*np.pi,-0.02,"x",fontsize=14)
plt.legend()
plt.show()