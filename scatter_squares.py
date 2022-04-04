import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox


'''绘制散点图'''

# 给图表提供输入值
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
color = (0.2,0.3,0.5)

# 调用scatter(),cmap = 'viridis'设置成彩虹颜色
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,edgecolors='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)

# 设置刻度标记的大小
#plt.tick_params(axis='both',which='major',labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 展示图片
# plt.show()

# 将该图自动保存到文件中
plt.savefig('square_save.jpg',bbox_inches='tight')