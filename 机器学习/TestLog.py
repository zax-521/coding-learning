# 导入数学计算库，用于计算对数
import math
# 导入matplotlib绘图库，用于绘制曲线
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # 生成x轴数据：1到299的整数除以100，得到0.01到2.99的浮点数序列
    x = [float(i)/100 for i in range(1,300)]
    # 计算每个x对应的自然对数值，生成y轴数据
    y = [math.log(i) for i in x]
    # 绘制对数曲线：红色实线，线宽3，设置图例标签
    plt.plot(x, y, 'r-', linewidth= 3, label='log Curve')
    # 选取x列表中索引20和175对应的两个点的x坐标
    a = [x[20], x[175]]
    # 选取对应点的y坐标
    b = [y[20], y[175]]
    # 绘制两点之间的绿色连线，线宽2
    plt.plot(a,b, 'g-', linewidth= 2)
    # 在两个点位置绘制蓝色星型标记，大小10，透明度0.75
    plt.plot(a,b, 'b*', markersize=10, alpha= 0.75)
    # 显示图例，位置在左上角
    plt.legend(loc= 'upper left')
    # 显示网格线
    plt.grid(True)
    # 设置x轴标签
    plt.xlabel('X')
    # 设置y轴标签
    plt.ylabel('log(X)')
    # 展示绘制的图像
    plt.show()