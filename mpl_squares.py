import matplotlib.pyplot as plt
from numpy import square

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
#导入pyplot模块并指定为Plt，
# 然后调用plot函数根据这些数字绘制有意义的图形。
plt.plot(input_values,squares, linewidth=5)  
# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
# 设置刻度标记的大小
plt.tick_params(axis = 'both',labelsize = 14)


plt.show()  # 显示绘制的图形