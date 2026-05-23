"""
    Pandas初体验，绘制中日美三国GPD趋势图
"""
# 创建python脚本，导入pandas库
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# 解决中文不能在图标中正常显示的问题
# 将列名改为中文，使图例显示为各国名称 以下代码只需要运行一次即可
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 基于pandas加载数据
df = pd.read_csv("data/1960-2019全球GDP数据.csv", encoding="gbk")

# 设置显示的最大行数和列数为None
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# 恢复显示的最大行数和列数到默认值
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')

# 恢复所有选项到默认值
pd.reset_option('all')

# 基于pandas完成相关查询
china_gdp = df[df['country']=='中国'] # df.country 选中名为country的列
print((china_gdp.head(10))) # 显示前10条数据

# 将year年份设置为索引
china_gdp = china_gdp.set_index('year')
print(china_gdp.head()) # 默认显示前5条



# 同样方法画出日本和美国的GDP变化曲线，和中国的GDP变化进行对比
jp_gdp = df[df['country']=='日本'].set_index('year')
us_gdp = df[df['country']=='美国'].set_index('year')

# 对指定的列修改列名
jp_gdp.rename(columns={'GDP': '日本'}, inplace=True)
china_gdp.rename(columns={'GDP': '中国'}, inplace=True)
us_gdp.rename(columns={'GDP': '美国'}, inplace=True)

# 画出GDP逐年变化的曲线图
china_gdp.中国.plot(legend=True)

# 出图并添加图例 legend=True
jp_gdp.日本.plot(legend=True)
us_gdp.美国.plot(legend=True)



