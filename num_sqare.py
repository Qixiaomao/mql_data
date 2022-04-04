import matplotlib.pyplot as plt

# 给图表提供输入值
x_values = list(range(1,6))
y_values = [x**3 for x in x_values]

# 调用scatter()
plt.scatter(x_values,y_values,cmap=plt.cm.Greens,edgecolors='none',s=4)

# 设置图表标题并给坐标轴加上标签
plt.title("Three times",fontsize = 25)
plt.xlabel("input nums",fontsize = 14)
plt.ylabel("squared nums",fontsize = 14)

# 设置每个坐标轴的取值范围
#plt.axis([0,10,0,150])

# 展示图表
plt.show()