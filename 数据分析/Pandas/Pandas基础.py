"""
    一、Pandas简介：
        Pandas优势：
            1.底层是基于Numpy构建的，所以运行速度特别的快
            2.有专门的处理缺失数据的API（删、填）
            3.强大而灵活的分组、聚合、转换功能

    二、Pandas数据结构与数据类型
        1.Pandas数据结构和数据类型
            注：图解为："Pandas数据结构和数据类型"
            DataFrame
              - Series
                - 索引列
                  - 索引名、索引值
                  - 索引下标、行号
                - 数据列
                  - 列名
                  - 列值，具体的数据
            其中最核心的就是Pandas中的两个数据结构：DataFrame和Series，其中Series为一列数据，DataFrame为多列数据

        2.Series对象
            Series也是Pandas中的最基本的数据结构对象，下文中简称s对象；是DataFrame的列对象，series本身也具有索引。
            Series是一种类似于一维数组的对象，右下面两个部分组成：
                1.index：相关的数据索引标签；如果没有为数据指定索引，于是会自动创建一个0到N-1（N为数据的长度）的整数型索引。
                2.value：一组数据（numpy.ndarray类型）
            1.创建series对象
                1.通过list列表来创建
                    1.使用默认自增索引：s1 = pd.Series([1,2,3,4,5])
                    2.自定义索引：s2 = pd.Series([1,2,3,4,5], index=['a', 'b', 'c', 'd', 'e'])

                2.使用字典或元组创建series对象
                    1.使用字典创建：s3 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
                    2.使用元组创建：s4 = pd.Series((1, 2, 3, 4, 5))

                3.使用numpy创建series对象：s5 = pd.Series(np.arange(5))

            2.Series对象属性
                1.索引：Series对象.index
                2.values：Series对象.values
                3.通过索引获取数据：Series对象['索引']
                4.通过索引修改Series对象的元素值：Series对象['索引'] = 新值


        3.DataFrame
            DataFrame是一个类似于二维数组或表格(如excel)的对象，既有行索引，又有列索引
                - 行索引，表明不同行，横向索引，叫index，0轴，axis=0
                - 列索引，表名不同列，纵向索引，叫columns，1轴，axis=1

            1.创建DataFrame对象：
                1.使用字典加列表创建df，使默认自增索引：
                    每个键值对 = 一列数据
                    info1 = {
                        'name': ["周杰伦", "那英", "刘欢", "庾澄庆"],
                        'gender': ['男', '女', '男', '男'],
                        'age': [47, 58, 62, 64],
                    }
                    df1 = pd.DataFrame(info)

                2，使用列表加元组创建df，并自定义索引：
                    每个键值对 = 一行数据
                    info2 = [
                        ("周杰伦", "男", 47),
                        ("那英", "女", 58),
                        ("刘欢", "男", 62),
                        ("庾澄庆", "男", 64),
                    ]
                    df2 = pd.DataFrame(info2, columns=['name', 'gender', 'age'])

                3，使用numpy创建df：
                    arr1 = np.arange(12).reshape(3, 4)
                    df3 = pd.DataFrame(data=arr1, columns=['a', 'b', 'c', 'd'])

                4。

            2.DataFrame对象属性
                1.shape：维度，即行列数：DataFrame对象.shape
                2.index：索引列：DataFrame对象.index
                3.columns：列名：DataFrame对象.columns
                4.data：数据：DataFrame对象.values
                5.行列转置：T：DataFrame对象.T

            3.DataFrame对象方法
                1.获取前n行内容：DataFrame对象.head(n) # 默认五条

                2.获取后n行内容：DataFrame对象.tail(n) # 默认五条

                3.查看DataFrame对象的信息：DataFrame对象.info()

                4.查看DataFrame对象的描述性统计信息（四分法）：DataFrame对象.describe()

            4.DataFrame索引的设置
                1.修改行列索引值：index_names = ["学生" + str(i) for i in range(score_df.shape[0])]
                               DataFrame对象.index = index_names # 必须整体全部修改

                2.重设索引，设置新的下标索引：reset_index[drop=False]
                    注：drop默认为False，不删除原来索引，如果为True，则删除原来索引

                3.设置新索引：
                    df = pd.DataFrame({
                        'month': [1, 4, 7, 10],
                        'year': [2012, 2014, 2013, 2014],
                        'sale': [55, 40, 84, 31],
                    })
                    1.以月份设置新的索引：df.index('month')
                    2.设置多个索引，以年和月份设置新的索引：df.index(['year', 'month'])


        4.Pandas的数据类型
            1.Object：字符串类型，即String
            2.int：整数类型
            3.float：浮点数类型
            4.datetime：日期时间类型
            5.timedelta：时间差类型
            6.category：分类类型
            7.bool：布尔类型
            8.nan：空值类型

    三、Pandas基本数据操作
        1.索引操作：
            1.直接使用行列索引（先行后列）：
                获取'2018-02-27'这天的'open'结果：
                    data['open']['2018-02-27']

            2.结合loc或者iloc使用索引：
                1.loc：根据 '行索引' 和 '列名' 来获取元素
                    获取从'2018-02-27'到'2018-02-22'的'open'结果：
                        data.loc['2018-02-27':'2018-02-22', 'open']
                2.iloc：根据 '行号' 和 '列的索引' 来获取元素 （包左不包右）
                    获取前3天数据，前五列的结果：
                        data.iloc[:3, :5]

            3.赋值操作：
                对DataFrame当中的close列进行重新赋值为1
                data['close'] = 1
                data.close = 1 # 效果同上，缺点有空格等字符，该方式会报错

            4.排序操作：排序有两种形式，一种对于索引进行排序，一种对于内容进行排序
                1.索引排序：df.sort_index()

                2.内容排序：df.sort_values(by=, ascending=)
                    单个键或者多个键进行排序
                    参数：
                        1.by：指定排序参考的键
                        2.ascending：默认升序，False：降序，True：升序

                3.Series排序：
                    1.data.series.sort_index(ascending=True)
                    2.data.series.sort_values(ascending=True)

    四、DataFrame运算
        1.算数运算
            1.Series对象 和 数值运算，则Series中的每个数值都会和该数字进行运算
                注：close为Series对象
                加：df.close.add(2) 或 df.close + 2 或 df['close'] + 2
                减：df.close.sub(10)

        2.逻辑运算符：& 和 |
        3.逻辑运算函数：筛选
            1. 筛选出所有open>23的数据
                df[df['open'] > 23]
            2. 筛选出所有23<open<24的数据
                1.df[(df['open'] > 23) & (df['open'] < 24)] # 注：多组判断记得加 小括号
                3.df.query('open > 23 & open < 24')

            4.固定值的筛选，isin
                1.df[(df.open == 23.53) | (df.open == 23.67)]
                2.df.query('open == 23.53 | open == 23.67')
                3.df.query('open.isin([23.53, 23.67])')
                4.df.query('open in [23.53, 23.67]')


        4.统计函数
            describe：查看各列的描述性统计信息
            1.count：每列总数据
            2.sum：总和
            3.mean：平均数
            4.median：中位数
            5.min：最小值
            6.max：最大值
            7.mode：众数
            8.abs：绝对值
            9.prod：
            10.std：标准差
            11.var：方差
            12.idxmax：最大值索引
            13.idxmin：最小值索引
            14.cumsum：计算前n个数的和
            15.cummax：计算前n个数的最大值
            16.cummin：计算前n个数的最小值
            17.cumpord：计算前n个数的乘积

        5.自定义运算：apply
            1.apply(func, axis=0)
                func：自定义函数
                axis=0：默认是列，axis=1为行进行运算
                例：data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0)

    五、文件读取与存储
        1.Pandas读写CSV文件
            1.pandas.read_csv(filepath_or_buffer, sep=',', usecols=, index_col=0)
                filepath_or_buffer：文件路径
                sep：分隔符，默认用','隔开
                usecols：指定读取的列名，列表形式
                index_col=0：将索引为0的列，设置为索引

            注：特殊的csv文件：tsv文件
                区别：csv文件以','做分隔，tsv文件以tab键做分隔

            2.DataFrame.to_csv(path_or_buf=None, sep=',', columns=None,
                    header=True, index=True, mode='w', encoding=None)
                path_or_buf：文件路径
                sep：分隔符，默认用","隔开
                columns：选择需要的列索引
                header：boolean or list of string, default True
                index：是否进行索引，是否写入列索引值
                mode：'w'：重写，'a'：追加


        2.Pandas操作MySQL
            pip install pymysql sqlalchemy
            1.读取数据
                data = pandas.read_csv('filepath', encoding='编码方式')
            2.创建数据库引擎
                engine = create_engine('数据库+模块名://数据库用户名:密码@主机名:端口号/要操作的数据库名?编码方式')
            3.将数据写入数据库：
                data.to_sql('表名', con=engine, if_exists='append', index=False)
                    name：数据库表名
                    con：引擎对象
                    if_exists=fail/replace/append：当数据表存在时，如何处理：fail：报错，replace：替换，append：追加
                    index：是否将索引写入数据库
            4.从sql表中读取数据
                sql_df = pd.read_sql('my_table', engine) # 读取所有数据
                sql_df = pd.read_sql('select name, AKA from my_table limit 0,2', engine) # 读取指定数据

        3.Pandas读写JSON文件
            1.将JSON格式转换成默认的 Pandas DataFrame格式
                pandas.read_json(path_or_buf=None, orient=None, typ='frame', lines=False)
                    path_or_buf：文件路径
                    orient：默认使用columns格式
                        1.split：{index: [index], columns: [columns], data: [values]}将索引总结到索引，列名到列名，数据到数据
                        2.records：以[{columns: value},..., {columns: value}]的形式输出
                        3.index：以{index: {columns: value}...}的形式输出
                        4.columns：以{column: {index: value}}的形式输出
                    typ：指定转换成的对象类型series或dataframe
                    lines：按照每行读取json对象

    六、DataFrame数据的增删改查操作
        1.增添：
            1.通过直接赋值的方式添加新列
                1.固定值：df['新列名'] = 固定值 # 列名不能跟已有的相同
                2.传入列表：df['新列名'] = [] # 传入的列表的元素必须跟数据的行相等
                3.通过已有的列(Series)来计算新列的值：df['新列名'] = df.列名 * 2
                4.通过函数来计算新列的值：df['新列名'] = 函数

            2.df.assign函数添加列
                df.assign(c1=,c2=,...,cn=)

        2.删除，去重：
            1.df.drop删除行数据：
                1.df3.drop([0]) # 默认删除行
                2.df3.drop([0, 2, 4]) # 删除多行
                  # 会修改原数据：inplace=True：修改原数据,inplace默认为False
                  df4 = df3.drop(index=[0, 2, 4], inplace=True)


                3.df.GDP.drop([0, 2]) # 对series对象按索引删除

            2.df.drop删除列数据：df3.drop([0], axis=1) # axis=1指定删除列

            3.使用del删除指定的列：
                注：del是永久删除原df中的列，drop是返回删除后的df或series，原数据不变
                del df3['c3']

            4.DataFrame数据去重：
                # 添加一部分重复的数据（merge(), join(), concat()）
                df4 = pd.concat([df2,df2])
                # 实施去重操作
                df5 = df4.drop_duplicates()

            5.series数据去重：'GDP'：列名
                1.df5 = df4.GDP.drop_duplicates()
                2.df5 = df4.GDP.unique()

        3.修改：
            1.df.assign替换列
            2.直接对原始的DF进行赋值修改处理
                pd['列名'] = []
            3.replace函数替换数据
                1.df.replace(old, new)
                2.df.列名.replace(old, new)

        4.查询：
            1.head()
            2.tail()
            3.df[['列名1', '列名2', ...]] 或 df.列名
            4.df[start : end : step]：包左不包右
            5.df.query()
            6.df2.sort_values

        5.rank函数：
            1.用法：DataFrame/Series.rank(axis=0/1, numeric_only=True, na_option=keep/top/bottom,
                    ascending=True, pct=True, method=average/min/max/dense)
            2.axis：设置按照列还是行排序，0为列，1为行
            3.numeric_only：是否值计算数字型的columns，默认为True
            4.na_option：NaN值是否参与排序，以及如何排序
                1.keep；NaN值保留原有位置
                2.top：NaN值全部放在前面（升序时）
                3.bottom：NaN值全部放在末尾（升序时）
            5.ascending：升序或降序，默认True升序
            6.pct：是否以排名的百分比显示排名（所有排名与最大排名的百分比），默认False
            7.method：排名评分的计算方式，固定值参数
                1.average：默认值，排名评分不连续；数值相同的评分一致，都为平均值（即都为2.5名）
                2.min：数值相同的取最小排名，排名不连续（即并列第2，没有第3名）
                3.max：数值相同的取最大排名，排名不连续（即并列第3，没有第2名）
                4.dense：数值相同的取相同排名，且排名连续（即并列第2，且有第三名）

"""
import os

import pandas as pd
import numpy as np
import matplotlib as plt
from dotenv import load_dotenv
from sqlalchemy import create_engine


# # 默认自增索引
# s1 = pd.Series([1, 2, 3, 4, 5])
# print(s1)

# # 自定义索引
# s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# print(s2)

# # 字典形式
# s3 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
# print(s3)

# # 元组形式
# s4 = pd.Series((1, 2, 3, 4, 5))
# print(s4)

# # 使用numpy创建
# s5 = pd.Series(np.arange(5))
# print(s5)

# # Series对象属性
# s6 = pd.Series(data=[i for i in range(6)], index=[i for i in 'ABCDEF'])
# print(s6)
# print(s6.index)
# print(s6.values)
# print(s6['A'])

# # 通过字典 + 列表 创建
# info = {
#     'name': ["周杰伦", "那英", "刘欢", "庾澄庆"],
#     'gender': ['男', '女', '男', '男'],
#     'age': [47, 58, 62, 64]
# }
# df1 = pd.DataFrame(info)
# print(df1)

# # 通过 列表 + 元组 创建
# info2 = [
#     ("周杰伦", "男", 47),
#     ("那英", "女", 58),
#     ("刘欢", "男", 62),
#     ("庾澄庆", "男", 64),
# ]
# df2 = pd.DataFrame(info2, columns=['name', 'gender', 'age'])
# print(df2)

# # 通过 numpy的ndarray → pandas DataFrame对象
# arr1 = np.arange(12).reshape(3, 4)
# print(arr1)
# df3 = pd.DataFrame(data=arr1, columns=['a', 'b', 'c', 'd'])
# print(df3)

# # 简单案例，生成10名同学，5门功课的数据
# # 1.生成10名学生，5门功课的成绩，成绩范围：40~100
# score_df = pd.DataFrame(np.random.randint(40,101, (10, 5)))
#
# # 2.修改DataFrame对象的 列名 和 索引列值
# column_names = ["语文", "数学", "英语", "政治", "体育"]
# # index_names = ["同学0", "同学1", "同学2", "同学3", "同学4", "同学5", "同学6", "同学7", "同学8", "同学9"]
# index_names = ["同学" + str(i) for i in range(score_df.shape[0])]
#
# # 3.具体的修改DataFrame的对象 列名 和 索引值
# # score_df.columns = column_names
# # score_df.index = index_names
# # rename函数
# score_df.rename(
#     index={i: index_names[i] for i in range(score_df.shape[0])},
#     columns= {i: column_names[i] for i in range(score_df.shape[1])},
#     inplace=True
# )
#
# # 4.打印修改后的结果
# print(score_df)

# # df详细信息
# score_df.info()
# # df详细统计信息
# score_df.describe()
# # 重置索引列 reset_index()
# score_df.reset_index(drop=False)
# 重新设置索引 set_index()
# score_df.set_index('数学')
# print(score_df)

# # 4.Pandas的数据类型
# df = pd.DataFrame({
#     'name': ["周杰伦", "那英", "刘欢", "庾澄庆"],
#     'gender': ['男', '女', '男', '男'],
#     'age': [47, 58, 62, np.nan]
# })
# print(df)
# df.info()
#
# df2 = pd.DataFrame(['2026-05-20', '2026-05-21', '2026-05-22'], dtype='datetime64[ns]')
# print(df2)
# df2.info()
#
# start_date = pd.to_datetime('2002-04-03')
# end_date = pd.to_datetime('2026-05-21')
# days = end_date - start_date
# print(days)
# print(type(days))
#
# s1 = pd.Series(['男', '女', '未知'], dtype='category')
# print(s1)

# 读取一个真实的股票数据，确保完成基本操作
# df = pd.read_csv('./data/stock_day.csv')
# # 删除一些暂时不用的列
# df = df.drop(['ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20'], axis=1)
# print(df)
# df.info()
# df.describe()

# # 根据行列索引获取元素，先行后列
# print(df['open']['2018-02-23'])

# # 结合loc或者iloc使用索引
# print(df.loc['2018-02-27': '2018-02-14', 'open': 'high'])
# print(df.iloc[:5, :2])

# # 赋值操作
# df['close'] = 1
# df.close = 1

# # 排序
# # 基于open排序
# print(df.sort_values(by='open', ascending=False))

# # 基于open排序，open一样的基于high排序
# print(df.sort_values(by=['open', 'high'], ascending=[True,True]))

# # 按照索引排序
# print(df.sort_index(ascending=True))

# # 基于 Series对象的 sort_index()排序方法
# print(df.open.sort_index(ascending=True))
# print(df['open'].sort_values(ascending=True))

# # DataFrame运算
# # 算数运算
# print(df['close'] + 2)
# print(df.close.add(2))
# print(df.close.sub(10))

# # 逻辑运算
# # 筛选出所有open>23的数据
# print(df[df['open'] > 23])
# # 筛选出所有23<open<24的数据
# print(df[(df['open'] > 23) & (df['open'] < 24)]) # 注：多组判断记得加 小括号
# # query()函数
# print(df.query('open > 23 & open < 24'))

# # 固定值的筛选，isin
# print(df[(df.open == 23.53) | (df.open == 23.67)])
# print(df.query('open == 23.53 | open == 23.67'))
# print(df.query('open.isin([23.53, 23.67])'))
# print(df.query('open in [23.53, 23.67]'))

# 统计函数

# 文件的读取与存储
# data = pd.read_csv('./data/stock_day.csv', usecols=['open', 'close', 'high', 'low'])
# print(data)
# data = data.drop(['high', 'low'], axis=1)
# print(data)

# csv文件的存储
# data[0: 10].to_csv('./data/my_file1.csv')
# data1 = pd.read_csv('./data/my_file1.csv')
# print(data1)

# # tsv文件的存储
# data.to_csv('./data/my_file2.tsv', sup='\t')

# load_dotenv()
# # # Pandas 操作 Mysql
# data = pd.read_csv('./data/csv示例文件.csv', encoding='gbk', index_col=0)
# # print(data)
# # 将数据写入mysql表中
# mysql_url = os.getenv('MYSQL_URL')
# engine = create_engine(mysql_url)
# # data.to_sql('my_table', engine, index=False, if_exists='append')
# # sql_df = pd.read_sql('my_table', engine)
# sql_df2 = pd.read_sql('select name, AKA from `my_table` limit 0,2', engine)
# print(sql_df2)

# # Pandas读取json文件
# # 读取json文件
# json_df = pd.read_json('./data/test.json', orient='records', lines=True)
# print(json_df)
# # 将上述数据，写入json文件中
# json_df.to_json('./data/my_file1.json', orient='records', lines=True)


# # Pandas的增删改查操作
# # 通过直接赋值的方式添加新列
df1 = pd.read_csv('./data/1960-2019全球GDP数据.csv', encoding='gbk')
# 浅拷贝
df2 = df1[:5].copy()
# print(df2)
# # 增添
# df2['c1'] = 33
# print(df2)
# # 新增数据数量必须和行数相等
# df2['c2'] = [1, 2, 3, 4, 5]
# df2['c3'] = df2.year * 2
def my_fun1():
    return 1200
# df2['c4'] = my_fun1()
# print(df2)
# # df.assign函数添加列
# df3 = df2.assign(c1=66)
df3 = df2.assign(
    c1=33,
    c2=[1,2,3,4,5],
    c3=df2.year * 2,
    c4 = my_fun1()
)
print(df3)
print('=========修改后==========')

# 删除
# df4 = df3.drop(index=[0, 2, 4])
# 会修改原数据
# df3.drop(index=[0, 2, 4], inplace=True)
# print(df3)
# df4 = df3.drop(['c4'], axis=1)
# print(df4)
# del df3['c4']
# print(df3)

# # 去重
# # 添加一部分
# df4 = pd.concat([df3, df3])
# print(df4)
# print('==============DataFrame去重=================')
# df5 = df4.drop_duplicates()
# print(df5)

# 修改
# 查询