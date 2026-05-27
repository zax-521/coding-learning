"""
    一、高级处理 - 缺失值处理（要么删，要么填）
        1.应用isnull判断是否有缺失数据NaN
            np.all(pd.isnull(df)))
            np.all(pd.notnull(df)))
        2.应用fillna实现缺失值的填充
            df[column].fillna(value=df[column].mean(), inplace=True)
        3.应用dropna实现缺失值的删除
            df.dropna(axis='row', how='all')
        4.应用replace实现数据替换
            df.replace('?', np.nan, inplace=True)

        5.实现步骤：
              -获取缺失值的标记方式(Nan或者其他标记)
                -如果是NaN：
                  -判断数据中是否包含NaN：pd.isnull(df) 或 pd.notnull(df)
                    -存在缺失值NaN：
                      -删除存在缺失值的：dropna(axis='row') # 不会修改原数据，需接受返回值
                      -替换缺失值：fillna(value, inplace=True) # value：替换的值； inplace：是否修改原数据，True是，False否
                -如果不是NaN，而是其他的，例如'?'：
                  -先替换'?'为np.nan，然后继续处理

    二、高级处理 - 数据合并
        1.应用pd.concat实现数据合并，类似于union # 能行能并
            pd.concat([data1, data2], axis=1, join='outer/inner') # axis=0为列，axis=1为行
                join：
                    outer：默认是满外连接，即左表全集 + 右表全集 + 交集
                    inner：内连接，即只要交集
            注：列合并默认参考列名，行合并默认参考行号

        2.应用pd.merge实现数据合并，类似于join # 只能行合并
            可以指定按照两组数据的共同键值队合并或者左右各自
            pd.merge(left, right, how='inner', on=[column1, column2, ...])
            left；DataFrame
            right：另一个DataFrame
            on：指定的共同键，默认使用相同列名
            how：按照什么方式连接
                1.left：LEFT OUTER JOIN：保留左表 (df1) 所有行，右表无匹配则为 NaN，即左全+右匹配
                2.right：RIGHT OUTER JOIN：保留右表 (df2) 所有行，左表无匹配则为 NaN，即右全+左匹配
                3.outer：FULL OUTER JOIN：保留左表和右表的所有行，缺失补 NaN，即两边全要
                4.inner：INNER JOIN：只保留两边都匹配的行，即只交集

    三、高级处理 - 数据分组与聚合
        1.分组函数返回分组对象（基于列进行分组）：gs = df.groupby(['列名1', '列名2', ...])
            返回DataFrameGroupBy类型 → DataFrame分组对象

        2.分组后获取各个组内的数据
            1.获取每组第一条数据：gs.first()
            2.获取每组最后一条数据：gs.last()
            3.按分组依据获取其中一组数据：gs.get_group(('value1', 'value2', ...))

        3.分组聚合
            分组后对多列分别使用不同的聚合函数：
            1.返回DataFrame对象
                df.groupby(['列名1', '列名2', ...], as_index=bool).agg({
                    '指定列1': '聚合函数名',
                    '指定列2': '聚合函数名',
                    '指定列3': '聚合函数名',
                })
                as_index：是否将列名当作索引，True：是，False：否，当作列
            2.返回Series对象
                df.groupby(['列名1', '列名2', ...]).列名.聚合函数()
                df.groupby(['列名1', '列名2', ...])['列名'].聚合函数()
            3.返回DataFrame队形
                df.groupby(['列名1', '列名2', ...])[['列名']].聚合函数()

            例：1.按城市和线上线下划分，分别计算销售金额的平均值、成本的总和
                df.groupby(['city', 'channel']).agg({
                    'revenue':  'mean',
                    'unit_cost': 'sum',
                })
                2.df.groupby(['city', 'channel']).revenue.sum()
                  df.groupby(['city', 'channel'])['revenue'].sum()

                3.df.groupby(['city', 'channel'])[['revenue']].sum()

        4.分组过滤操作
            df.groupby(['列名1', ...]).filter(
                lambda x: dosomething return True or False
            )
            例：按照城市分组，查询每组销售金额平均值大于200的全部数据
                # 返回DataFarem对象
                df.groupby(['city']).filter(lambda s: s['revenue'].mean() > 200)
                # 返回Series对象
                df.groupby(['city'])['revenue'].filter(lambda s: s.mean() > 200)

    四、高级处理 - 交叉表与透视表
        1.交叉表：计算一列数据对于另外一列数据的分组个数
            pd.crosstab(column1, column2)

        2.透视表：指定某一列对另一列的关系
            pd.pivot_table(DataFrame对象, values='显示的值', index='索引', columns='列', aggfunc='聚合函数')
            或 DataFrame对象.pivot_table(values='显示的值', index='索引', columns='列', aggfunc='聚合函数')
"""
import pandas as pd
import numpy as np

# # 一、缺失值处理
# 1.读取数据
# movie_df = pd.read_csv('./data/movie.csv')
# # 2.查看数据信息，检查是否有数据缺失
# movie_df.info() # 基本信息(列名，数据类型，非缺失值数量等)
# print(movie_df.describe()) # 描述性统计信息(均值，中位数，标准差等)
# # 3.1 删除缺失值
# movie_df2 = movie_df.dropna() # 不会修改原数据，加入 inplace=True即可，默认删：行axis=0，列axis=1
# movie_df2.info()
# movie_df.info()

# # 3.2 填充缺失值
# # 判断某列(的某个值)是否有缺失值
# movie_data = pd.isnull(movie_df) # 判断df对象的，每个列，每个值是否为空(缺失值)
# movie_data1 = pd.notnull(movie_df) # 判断df对象的，每个列，每个值是否为不为空(缺失值)

# # 判断某列是否是，包含缺失值的列
# fina = np.all(pd.notnull(movie_df))
# # 填充固定值
# movie_df3 = movie_df.fillna(23)
# # 填充每列的平均值
# movie_df['Revenue (Millions)'].fillna(movie_df['Revenue (Millions)'].mean(), inplace=True)
# movie_df['Metascore'].fillna(movie_df['Metascore'].mean(), inplace=True)

# # 运用for循环的方式，使用每列的平均值，来填充各列的缺失值
# movie_df.info()
# for col_name in movie_df.columns:
#     if not np.all(pd.notnull(movie_df[col_name])):
#         movie_df[col_name].fillna(movie_df[col_name].mean(), inplace=True)
# movie_df.info()

# # 如果缺失值不为NaN，而是用'?'表示，则先将'?'转换成NaN，然后再进行缺失值的删除或填充
# movie_df.replace('?', np.nan)

# # 二、数据合并
# # 1.准备数据
# df = pd.read_csv('./data/1960-2019全球GDP数据.csv', encoding='gbk')
# df1 = df[:10]
# df2 = df[10:20]
# # concat()合并数据 0列 1行
# new_df1 = pd.concat([df1, df2], axis=0)
# new_df2 = pd.concat([df1, df2], axis=1)
# df1.info()
# df2.info()
# new_df1.info()
# new_df2.info()
# print(new_df1)
# print(new_df2)

# # pd.merge()
# df1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                     'key2': ['K0', 'K1', 'K0', 'K1'],
#                     'A': ['A0', 'A1', 'A2', 'A3'],
#                     'B': ['B0', 'B1', 'B2', 'B3']})
#
# df2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                       'key2': ['K0', 'K0', 'K0', 'K0'],
#                       'C': ['C0', 'C1', 'C2', 'C3'],
#                       'D': ['D0', 'D1', 'D2', 'D3']})
#
# df3 = pd.merge(df1, df2, how='inner')
# df4 = pd.merge(df1, df2, how='outer')
# df5 = pd.merge(df1, df2, how='left')
# df6 = pd.merge(df1, df2, how='right')
# print('=============df1=============')
# print(df1)
# print('=============df2=================')
# print(df2)
# print('=============inner================')
# print(df3)
# print('==============outer=================')
# print(df4)
# print('==============left================')
# print(df5)
# print('==============right================')
# print(df6)

# # 三、数据分组
# df = pd.read_csv('./data/uniqlo.csv')
# pd.set_option('display.max_columns', None) # 设置列的最大显示数量
# print(df)
# df.info()
# # 1.分组
# gs = df.groupby(['city', 'channel'])
# print('======================================first city==============')
# print(gs.first())
# print('========================================last city================')
# print(gs.last())
# 按分组依据获取其中一组数据
# ggs = gs.get_group(('深圳', '线下'))
# print(ggs)

# # 2.聚合
# gs1 = df.groupby(['city', 'gender_group']).agg({'customer': 'sum', 'revenue': 'mean'})
# print(gs1)

# # 3.过滤
# gsf1 = df.groupby('city').filter(lambda s: s['revenue'].mean() > 200).city.unique()
# gsf2 = df.groupby('city')['revenue'].filter(lambda s: s.mean() > 200)
# print(gsf1)
# print('===============================================')
# print(gsf2)

# 四、交叉表与透视表
# # 交叉表
# data1 = {
#     '性别': ['男', '女', '男', '女', '男', '女', '女', '男'],
#     '购买': ['是', '否', '是', '是', '否', '否', '是', '否']
# }
# df1 = pd.DataFrame(data1)
# crosstab = pd.crosstab(df1['性别'], df1['购买'])
# print(crosstab)

# # 透视表
data2 = {
    '性别': ['男', '女', '男', '女', '男', '女'],
    '购买': ['是', '否', '是', '是', '否', '否'],
    '金额': [100, 150, 200, 130,160, 120]
}
df2 = pd.DataFrame(data2)
pivot_table1 = pd.pivot_table(df2, values='金额', index='性别', columns='购买', aggfunc='mean')
pivot_table2 = df2.pivot_table(values='金额', index='性别', columns='购买', aggfunc='mean')
print(pivot_table1)
print(pivot_table2)