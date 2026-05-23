"""
    原生的 python 连接 mysql
"""
import pymysql

# 1.获取连接对象
conn = pymysql.connect(
    hsot='',
    port=3306,
    user='root',
    password='<PASSWORD>',
    database='sql_name',
    charset='utf8mb4'
)

# 2.根据连接对象，获取游标对象
cursor = conn.cursor()

# 3.定义SQL语句
sql = 'select * from sql_name limit 0,2'

# 4.执行SQL语句
cursor.execute(sql)

# 5.获取结果集
result = cursor.fetchall()

# 6.遍历结果集
for row in result:
    print(row)

# 7.释放资源
cursor.close()