from turtle import color
import matplotlib.pyplot as plt

'''绘制散点图'''

# 给图表提供输入值

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

# 调用scatter()
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Greens,
    edgecolors='none',s=30)

# 设置图表标题并给坐标轴上加标签
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 16)
plt.ylabel("Square of Value",fontsize = 16)

# 设置每个坐标轴的取值范围
#plt.axis([0,2001,0,11000])

# 展示图片
plt.show()

# 将该图自动保存到文件中
plt.savefig('num_sqare.jpg',bbox_inches='tight')