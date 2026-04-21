"""
    SQL：SQL是结构化查询语言（Structured Query Language）的缩写。它是
        一种专门用来和数据库“对话”的编程语言。你可以通过 SQL 告诉数据库：
        帮我存一条数据、查一下某个信息、改一个数字，或者删掉某条记录。

        information_schema（系统元数据）
        mysql（存账号、密码、权限）
        performance_schema（性能监控）
        sys（性能视图）

        PRIMARY KEY：主键，唯一键，不能重复，具有唯一性，主键不能为NULL
        FOREIGN KEY：外键
    SQL层级格式：数据库 → 表 → 字段/列 → 行/记录 → 值

    数据类型：
        1.INT：整数型
        2.DECIMAL(m,n)：精确小数型；m：总共几位数，n：小数点后有几位
            例子：DECIMAL(3,2) 3.22，m：322三位数，n：3.22小数点后两位
        3.VARCHAR(n)：可变字符串；n：该字段最多能存储多少个 “字符”
        4.BLOB：二进制大对象(Binary Large Object)，存二进制资料，如：图片、视频、文件
        5.DATA：'YYYY-MM-DD' 日期型
        6.TIMESTAMP：'YYYY-MM-DD HH:MM:SS' 时间戳

    关键字：通常用大写，在工具中显示蓝色，
        自己命名的名称可以用  `` ，为了避免名称和关键字冲突
        例子：CREATE DATABASE `database`;
        去重关键字：DISTINCT

    SQL语句：
        基础：
        创建数据库(create database)：
            创建数据库：CREATE DATABASE sql_tutorial;
            显示所有数据库：SHOW DATABASES;
            显示数据库中的表：SHOW TABLES;
            显示指定数据库中的表：SHOW TABLE FROM `sql_test`;
            删除数据库：DROP DATABASE `database`;
            使用数据库：USE `sql_tutorial`;


        创建表格(create table)：
            创建表：CREATE TABLE `student`(
                       `student_id` INT PRIMARY KEY,
                       `name` VARCHAR(20),
                       `major` VARCHAR(20)
                   );
                   或者
                   CREATE TABLE `student`(
                       `student_id` INT,
                       `name` VARCHAR(20),
                       `major` VARCHAR(20),
                       PRIMARY KEY('student_id')
                   );
            显示表：DESCRIBE TABLE `student`;
            删除表：DROP TABLE `student`;
            新增表的字段(属性)：ALTER TABLE `student` ADD `gpa` DECIMAL(3,2);
            删除表的字段(属性)：ALTER TABLE `student` DROP COLUMN 'gpa';

        存储资料(insert)：
            向表中插入记录：INSERT INTO `student` VALUES(1, '小白', '历史');
                    或者：INSERT INTO `student` VALUES(3, '小兰', NULL); 不知道具体值时可以写：NULL
                    或者：INSERT INTO `student`(`name`, `major`, `student_id`) VALUES('小红', '英语', '4');
                    或者：INSERT INTO `student`(`major`, `student_id`) VALUES('英语', '5');
                    或者：INSERT INTO `student` VALUES(1, '小白', '英语', 50), (2, '小黄', '生物', 90);

        限制、约束(constraint)：
            NOT NULL：值不能为NULL
            UNIQUE：值不能重复
            DEFAULT '默认值'：新增预设值
            AUTO_INCREMENT：自动生成唯一数字序列，即自增
            CREATE TABLE `student`(
                `student_id` INT PRIMARY KEY AUTO_INCREMENT,
                `name` VARCHAR(20) NOT NULL,
                `major` VARCHAR(20) DEFAULT '数学',
                `phone` VARCHAR(30) UNIQUE NOT NULL
            );

        修改、删除数据(update, delete)：
            修改：# 将`student`表中`major`字段中的值全部修改成'物理'
                 UPDATE `student`
                 SET `major` = '物理';
                 或者
                 # 修改`student`表中 `major`为'英语'记录，将其中`major`属性的值修改为'英语课'
                 UPDATE `student`         # 修改 `student`表
                 SET `major` = '英语课'    # 设置 `major`属性中的值为 '英语课'
                 WHERE `major` = '英语';   # 条件是 `major` 为 '英语'的记录
                 或者
                 # 修改`student`表中 `student_id`为'4'的记录，将其中`major`属性的值修改为'数学'，`name`属性的值修改为'小红'
                 UPDATE `student`
                 SET `major` = '数学', `name` = '小红' # SET 列名1 = 新值1, 列名2 = 新值2, ... 不能用AND连接
                 WHERE `student_id` = '4'
                 或者
                 # 修改`student`表中 `major`为'生物'或者'化学'的记录，将其中`major`属性的值修改为'生化'
                 UPDATE `student`
                 SET `major` = `生化`
                 WHERE `major` = '生物' or `major` = '化学' # WHERE 条件1 AND/OR 条件2, ...

            删除：# 删除`student`列表中的所有数据
                 DELETE FROM `student`;
                 # 删除`student`列表中`name`为'小红'的记录
                 DELETE FROM `student`
                 WHERE `name` = '小红';
                 或者
                 DELETE FROM `student`
                 WHERE `name` = '小白' AND `major` = '物理';
                 或者
                 DELETE FROM `student`
                 WHERE `score` < 60;

        查询数据(select)：
            查询表中的所有列(字段)和所有行(记录)：SELECT * FROM `student`;
            查询`student`表中`name`字段的所有值：SELECT `name` FROM `student`;
            查询`student`表中`name`和`major`字段的所有值：SELECT 'name',`major` FROM `student`;
            查询`student`表中所有数据，并按根据`score`从小到大排序：
                SELECT * FROM `student` ORDER BY `score` ASC; # 这里的ASC可以省略，因为默认就是ASC
            查询`student`表中所有数据，并按根据`score`从大到小排序：
                SELECT * FROM `student` ORDER BY `score` DESC;
            查询`student`表中所有数据，并按根据`score`从小到大的排序后，再根据`student_id`排序：
                SELECT * FROM `student` ORDER BY `score`, 'student_id';
            限制查询返回的记录数量：SELECT * FROM `student` LIMIT 3;
            先排序再限制返回数量：SELECT * FROM `student` ORDER BY `score` LIMIT 3;
            添加查询条件：SELECT * FROM `student` WHERE `major` = '英语' AND/OR `score` > '60';
            查询`major`为'数学'或'英语'或'语文'的数据：SELECT * FROM `student` WHERE `major` IN('数学', '英语', '语文');

        进阶：
        创建公司数据库：
            CREATE TABLE `employee`(
                `end_id` INT PRIMARY KEY,
                `name` VARCHAR(20),
                `birth_date` DATE,
                `sex` VARCHAR(1),
                `salary` INT,
                `branch_id` INT,
                `sup_id` INT
            );

            CREATE TABLE `branch`(
                `branch_id` INT PRIMARY KEY,
                `branch_name` VARCHAR(20) UNIQUE,
                `manager_id` INT,
                FOREIGN KEY (`manager_id`) REFERENCES `employee`(`emp_id`) ON DELETE SET NULL
            );

            CREATE TABLE `client`(
                `client_id` INT PRIMARY KEY,
                `client_name` VARCHAR(20),
                `phone` VARCHAR(32)
            );

            CREATE TABLE `works_with`(
              `emp_id` INT ,
              `client_id` INT ,
              `total_sales` INT,
              PRIMARY KEY(`emp_id`,`client_id`),
              FOREIGN KEY (`emp_id`) REFERENCES `employee`(`emp_id`) ON DELETE CASCADE,
              FOREIGN KEY(`client_id`) REFERENCES `client`(`client_id`) ON DELETE CASCADE
            );

            ALTER TABLE `employee` DROP PRIMARY KEY; # 如果字段名是主键，将字段名重命名前要先删除主键，再进行重命名
            ALTER TABLE `employee` CHANGE `emd_id` `emp_id` INT PRIMARY KEY; # 将字段名重命名

            # 将`employee`表中的`branch_id`设置成外键连接`branch`(branch_id)
            ALTER TABLE `employee`
            ADD FOREIGN KEY(`branch_id`)
            REFERENCES `branch`(`branch_id`)
            ON DELETE SET NULL;

            ALTER TABLE `employee` ADD FOREIGN KEY(`sup_id`) REFERENCES `employee`(emp_id) ON DELETE SET NULL;

            DESCRIBE `employee`;
            DESCRIBE `branch`;
            DESCRIBE `client`;
            DESCRIBE `works_with`;

            INSERT INTO `employee` VALUES(206, '小黄', '1998-10-08', 'F', 50000, 1, NULL),
            (207, '小绿', '1985-09-16', 'M', 29000, 2, 206),
            (208, '小黑', '2000-12-19', 'M', 35000, 3, 206),
            (209, '小白', '1997-01-22', 'F', 39000, 3, 207),
            (210, '小兰', '1925-11-10', 'F', 84000, 1, 207);

            INSERT INTO `branch` VALUES(1, '研发', NULL),
            (2, '行政', NULL),
            (3, '咨询', NULL);

            INSERT INTO `client` VALUES(400, '小狗', '254354335'),
            (401, '小猫', '25633899'),
            (402, '旺财', '45354365'),
            (403, '露西', '54354365'),
            (404, '艾瑞克', '18783783');

            INSERT INTO `works_with` VALUES(206, 400, 70000),
            (207, 401, 24000),
            (208, 400, 9800),
            (208, 403, 24000),
            (210, 404, 87940);

            UPDATE `branch` SET `manager_id` = 206 WHERE `branch_id` = 1;
            UPDATE `branch` SET `manager_id` = 207 WHERE `branch_id` = 2;
            UPDATE `branch` SET `manager_id` = 208 WHERE `branch_id` = 3;

        查询公司资料：
            # 获取所有员工数据
            SELECT * FROM `employee`;
            # 获取所有客户数据
            SELECT * FROM `client`;
            # 按薪水从小到大获取员工资料
            SELECT * FROM `employee` ORDER BY `salary`;
            # 获取薪水前三高的员工
            SELECT * FROM `employee` ORDER BY `salary` DESC LIMIT 3;
            # 获取所有员工的名字
            SELECT `name` FROM `employee`;
            # 获取所有员工的性别并去重
            SELECT DISTINCT `sex` FROM `employee`;
            SELECT * FROM `branch`;
            SELECT * FROM `works_with`;

        聚合函数(aggregate function)：
            # 获取员工人数
            SELECT COUNT(*) FROM `employee`;

            # 获取所有出生于 1970-01-01 之后的女性员工人数
            SELECT COUNT(*) FROM `employee` WHERE `birth_date` > '1970-01-01' AND `sex` = 'F';

            # 获取所有员工的平均工资
            SELECT AVG(`salary`) FROM `employee`;

            # 获取所有员工工资的总和
            SELECT SUM(`salary`) FROM `employee`;

            # 获取工资最高的员工
            SELECT MAX(`salary`) FROM `employee`;

            # 获取工资最低的员工
            SELECT MIN(`salary`) FROM `employee`;

        通配符(wildcard)： '%' ：代表多个任意字符； '_' ；代表刚好1个任意字符； LIKE：模糊匹配
            # 获取电话号码尾数是335的客户
            SELECT * FROM `client` WHERE `phone` LIKE '%335';
            # 获取电话号码开头是254的用户
            SELECT * FROM `client` WHERE `phone` LIKE '254%';
            # 获取电话号码中有354的用户
            SELECT * FROM `client` WHERE `phone` LIKE '%354%';

            # 获取姓艾的客户
            SELECT * FROM `client` WHERE `client_name` LIKE '艾%';

            # 获取生日在12月的员工
            SELECT * FROM `employee` WHERE `birth_date` LIKE '_____12%';

        集合运算符(union)：用于将两个或多个 SELECT 查询的结果合并成一个结果集。
                注：统一数据类型，
            # 员工名字 UNION 客户名字
            SELECT `name` FROM `employee` UNION SELECT `client_name` FROM `client`;

            # 员工id + 员工名字 UNION 客户id + 客户名字   AS 后接命名字段
            SELECT `emp_id` AS `total_id`, `name` AS `total_name`
                FROM `employee` UNION SELECT `client_id`, `client_name` FROM `client`;

            # 员工工资 UNION 销售金额
            SELECT `salary` AS `total_money` FROM `employee` UNION SELECT `total_sales` FROM `works_with`;

        连接运算符(join)：根据两个或多个表之间的共同字段，把它们的行连接在一起的运算符
                JOIN 类型	左表无匹配	        右表无匹配	            使用场景
                NNER JOIN	不返回	            不返回	            只要有关联的数据
                LEFT JOIN	返回（右表为NULL）	不返回	            保留左表所有数据
                RIGHT JOIN	不返回	            返回（左表为NULL）	保留右表所有数据
                FULL JOIN	返回（右表为NULL）	返回（左表为NULL）	保留两表所有数据
                CROSS JOIN	所有组合	            所有组合	            需要生成所有组
            # 获取所有部门经理的名字  ON后面接的是限制条件
            SELECT * FROM `employee` JOIN `branch` ON `emp_id` = `manager_id`;
            或者
            SELECT `emp_id`, `name`, `branch_name` FROM `employee` JOIN `branch` ON `emp_id` = `manager_id`;
            或者
            SELECT `employee`.`emp_id`, `employee`.`name`, `branch`.`branch_name` FROM `employee`
            JOIN `branch` ON `employee`.`emp_id` = `branch`.`manager_id`;

            # LEFT JOIN 即 LEFT JOIN 在sql语句中的位置的左右， 返回所有左边的数据，返回右边匹配条件的数据。
            SELECT `e`.`emp_id`, `e`.`name`, `b`.`branch_name`
                FROM `employee` AS `e` LEFT JOIN `branch` AS `b` ON `e`.`emp_id` = `b`.`manager_id`;

        子查询(subquery)：（也叫内查询或嵌套查询）是指嵌套在另一个 SQL 查询中的查询。
            # 找出研发部门的经理名字
            SELECT `name` FROM `employee`
                WHERE `emp_id` = (SELECT `manager_id` FROM `branch` WHERE `branch_name` = '研发');
            相当于：SELECT `name` FROM `employee` WHERE `emp_id` = 206;

            # 找出对单一位客户销售金额超过50000的员工名字  这里用IN，原因是查询出来的条件不止一个，多个条件要用IN
            SELECT `name` FROM `employee`
                WHERE `emp_id` IN (SELECT `emp_id` FROM `works_with` WHERE `total_sales` > 50000);

        ON DELETE：是外键约束的一部分，用于定义：当父表（被引用的表）中的一行被删除时，子表（包含外键的表）中的数据该如何处理。
            选项	                           行为	                                适用场景
            CASCADE	        删除父表记录时，自动删除子表中所有引用它的记录	    订单删除时，同时删除订单明细
            SET NULL	    删除父表记录时，将子表中的外键字段设为 NULL	        部门解散时，员工部门设为 NULL
            SET DEFAULT	    删除父表记录时，将子表中的外键字段设为默认值	        较少使用
            RESTRICT	    拒绝删除父表记录（默认行为）	                    有订单的客户不能删除
            NO ACTION	    与 RESTRICT 相同（MySQL 中）	                同上

        python 连接 Mysql：
"""
# # 导入包
from mysql import connector
from dotenv import load_dotenv
import os

load_dotenv()

# 连接数据库服务器
connection = connector.connect(
    host=os.getenv("DB_HOST")
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database='sql_test' # 直接选择使用的数据库
)

# # 创建游标
# cursor = connection.cursor()

# # 创建数据库
# cursor.execute("CREATE DATABASE `qq`;")

# # 删除数据库
# cursor.execute("DROP DATABASE `qq`")

# # 获取所有数据库名称
# cursor.execute("SHOW DATABASES;")
# records = cursor.fetchall() # 读取所有数据
# for r in records:
#     print(r)

# # 使用数据库
# cursor.execute("USE `sql_test`;")

# # 创建表格
# cursor.execute("CREATE TABLE `test`(ts INT);")

# # 删除表格
# cursor.execute("DROP TABLE test")

# # 获取部门所有数据
# cursor.execute("SELECT * FROM `branch`;")
# records = cursor.fetchall()
# for r in records:
#     print(r)

# # 新增
# cursor.execute("INSERT INTO `branch` VALUES(5, '测试', NULL);")

# # 修改
# cursor.execute("UPDATE `branch` SET `manager_id` = NULL WHERE `branch_id` = 4")

# # 删除
# cursor.execute("DELETE FROM `branch` WHERE `branch_id` = 5;")

# # 关闭数据库
# cursor.close()
# # 提交指令 直接修改具体数据值的指令需要提交
# connection.commit()
# # 关闭连线
# connection.close()