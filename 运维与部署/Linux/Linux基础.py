"""
    一、基础知识
        1. Linux系统的组成：
            1.Linux系统内核：内核提供系统最核心的功能，如：调度CPU、调度内存、调度文件系统、调度网络通讯、调度IO等
            2.系统级应用程序

            用户 → 使用第三方程序/系统程序  → 调用内核 → 调度硬件

        2. 虚拟机：通过虚拟化技术，在电脑内，虚拟出计算机硬件，并给虚拟的硬件安装操作系统，即可得到一台虚拟的电脑，称之为虚拟机。

        3. 路径的描述方式：
            1.Linux：/user/local/hello.txt
                /：开头的 /表示根目录，后面的 / 表示层级关系

            2.windows：D:\data\work\hello.txt
                D:：表示D盘
                \：表示层级关系
    二、Linux基础操作
        1. Linux命令入门
            1.Linux命令基础：
                1.Linux命令基础格式：无论是什么命令，用于什么用途，在Linux中，命令有其通用的格式。
                    通用格式：command [-options] [parameter]
                        1. command：命令本身
                        2. -options：[可选, 非必填]命令的一些选项，可以通过选项控制命令中的行为细节
                        3. parameter：[可选, 非必填]命令的参数，多数用于命令的指向目标等
                    注：语法中的[]表示可选的意思
                2.例子：
                    1.ls -l/home/itheima：ls是命令本身，-l是选项，/home/itheima是参数
                        含义：以列表的形似，显示/home/itheima目录内的内容

                    2.cp -r trst1 test2：cp是命令本身，-r是选择，test1和test2是参数
                        含义：复制文件夹test1 成为 test2

            2.ls命令：展示文件列表命令
                1. ls [-a -l -h] [Linux路径]：
                    1.ls：表示以平铺形式，列出当前工作目录下的内容（文件或文件夹）
                        注：1.默认为当前登录用户的HOME目录作为当前工作目录
                           2.HOME目录：每个Linux操作用户在Linux系统的个人账户目录，路径在:/home/用户名

                    2.选项：[-a -l -h]
                        1. -a（ls -a）：表示 all 的意思，即列出全部文件（包含隐藏的文件和文件夹）
                            注：只要以 "." 开头，就能自动隐藏，即隐藏文件都是以 “.” 开头，例：.cache

                        2. -l（ls -l）：表示以列表（竖向排列）的形式展示内容，并展示更多信息（权限 用户和用户组 大/小 创建时间 文件/文件夹名称）

                        3. -h（ls -lh）：表示以易于阅读的形式，列出文件大小，如K、M、G
                            注：-h 选项必须搭配 -l 一起使用

                        4. 命令选项的组合使用：语法中的选项是可以组合使用的
                            1. ls -l -a、ls -la、ls -al：三种写法的作用都是一样的，以列表的形式输出全部文件，包括隐藏文件
                    注：用ls查看文件时，最开头的字母是 d 的表示为文件夹， 为 - 的表示文件，一般文件夹为深蓝色，文件为白色


                    3.参数：[Linux路径]
                        1.ls /：显示根目录下的文件或文件夹
                        2.ls -l -/：以列表的形式显示根目录下的文件或文件夹
            3.cd命令：切换工作目录命令，无选项 （cd：Change Directory）
                1. cd [Linux路径]：切换目录到指定目录，不给参数默认回到HOME目录

            4.pwd命令：查看当前工作目录，无选项，无参数

            5.相对路径和绝对路径：
                1.绝对路径：以根目录为起点，路径描述以 / 开头；例：cd /home/itheima/Desktop
                2.相对路径：以当前目录为起点，路径描述无需以 / 开头；例： cd Desktop

            6.特殊的路径表示符：
                例：绝对路径：/home/itheima/Desktop
                1. .：表示当前目录
                    cd ./Desktop 表示切换到当前目录下的 Desktop目录内， 和cd Desktop效果一样

                2. ..：表示上一级目录
                    cd .. 表示切换到上一级目录，即 /home/itheima

                3. ~：表示HOME目录
                    cd ~ 表示切换到HOME目录或cd ~/Desktop，切换到HOME内的Desktop目录

            7.mkdir命令：创建目录（文件夹） （mkdir：Make Directory）
                语法：mkdir [-p] Linux路径
                    选项：-p选项可选，表示自动创建不存在的父目录，适用于创建连续多层级的目录
                    参数：参数必填，表示Linux路径，即要创建文件夹的路径，相对/绝对都可
                    注：1.可以一次性创建多个文件夹
                       2.创建文件夹需要修改权限，在HOME目录内不需要，在HOME目录外需要权限

            8.touch命令：创建文件
                语法：touch Linux路径
                    无选项，参数必填：表示要创建的文件路径

            9.cat、more命令：查看文件内容
                cat语法：cat Linux路径
                    无选项，参数必填：表示被查看的文件路径
                more语法：more Linux路径
                    无选项，参数必填：表示被查看的文件路径，查看过程中，可以通过空格翻页
                cat和more的区别：
                    1.cat是直接将文件内容全部显示出来
                    2.more支持翻页，如果文件内容过多，可以一页页的展示
                    3.都通过 q 退出查看

            10.cp命令：复制文件\文件夹 （cp：copy）
                cp语法：cp [-r] 参数1 参数2
                -r选项：可选，用于复制文件夹使用，表示递归
                参数1：Linux路径，表示被复制的文件或文件夹
                参数2：Linux路径，表示要复制去的地方

            11.mv命令：移动文件\文件夹 （mv：move）
                mv语法：mv 参数1 参数2
                参数1：Linux路径，表示被移动的文件或文件夹
                参数2：Linux路径，表示要移动去的地方，如果目标不存在，则进行改名，确保目标存在
                注：只有到目标路径不存在的时候才有改名的效果

            12.rm命令：删除文件\文件夹
                rm语法：rm [-r -f] 参数1 参数2 ...... 参数N
                -r选项：可选，用于删除文件夹

                -f选项：可选，表示force，强制删除（不会弹出提示确认信息），删除文件夹要用-fr
                    1.普通用户删除内容不会弹出提示，只有root管理员用户删除内容会有提示
                    2.所以一般普通用户同步到-f选项

                参数1 参数2 ...... 参数N：表示要删除的文件或文件夹路径，按照空格隔开

                rm命令通配符：支持通配符 * ，用来做模糊匹配
                    1.符号 * 表示通配符，级匹配任意内容（包含空）
                    2.例：
                        1.test*：表示匹配任何以test开头的内容
                        2.*test：表示匹配任何以test结尾的内容
                        3.*test*：表示匹配任何包含test的内容
            13.which命令：查找命令的程序文件具体地址
                Linux命令，其本体就是一个个的二进制可执行程序。和Windows系统中的.exe文件，是一个意思。
                which语法：which 要查找的命令
                无选项，参数必填：表示要查找的命令

            14.find命令：
                1.按文件名查找指定文件/文件夹：
                    语法：find 起始路径 -name "被查找的文件名"
                    注：这里也可以使用通配符 * 进行模糊搜索

                2.按照文件大小查找文件：
                    语法：find 起始路径 -size +|-n[kMG]
                    +|-：表示大于和小于，任选其一
                    n：表示大小数字
                    kMG：表示大小单位，k（小写字母）表示kb，M表示MB，G表示GB
                    例：查找小于10KB的文件：find / -size -10k
                       查找大于100MB的文件：find / -size +100M
                       查找大于1GB的文件：find / -size +1G
            15.echo命令：可以使用echo命令在命令行内输出指定的内容
                echo语法：echo 输出的内容
                无选项，只有一个参数：表示要输出的内容，复杂内容可以用 "" 包围
                注：带有空格或\等特殊符号，建议使用双引号包围，防止空格后被识别为参数2

            16.反引号：``
                当想要输出的内容为命令时，可以用反引号``包围，
                    被``包围的内容，会被作为命令执行，而非普通字符。
                例：echo pwd 输出结果为：pwd
                    echo `pwd` 输出结果为：具体的当前目录路径

            17.重定向符：> 和 >>：即 覆盖 和 追加
                1.>：将左侧命令的结果，覆盖写入到符号右侧指定的文件中
                2.>>：将左侧命令的结果，追加写入到符号右侧指定的文件中
                例：1.echo "Hello World" > test.txt：test.txt文件内容为：Hello World
                   2.echo "Hello Linux" > test.txt：test.txt文件内容为：Hello Linux
                   3.echo "Hello itcast" >> test.txt：test.txt文件内容为：Hello Linux 换行 Hello itcast

            18.tail命令：查看文件尾部内容，跟踪文件的最新更改，即从尾部开始查看文件
                tail语法：tail [-f -num] Linux路径
                -f选项：表示持续跟踪
                -num选项：表示查看尾部多少行，不填默认10行
                参数：Linux路径，表示被跟踪文件的路径

            19.grep命令：过滤文件内容，即搜索含有对应关键字的行，并将行的内容输出出来。
                从文件中通过关键字过滤文件行：
                    语法：grep [-n] 关键字 文件路径
                    -n选项，可选，表示在结果中显示匹配的行的行号，即显示该内容为那一行
                    参数：关键字，必填，表示过滤的关键字，带有空格或其他特殊符号，建议使用""将关键字包围起来
                    参数：文件路径，必填，表示要过滤内容的文件路径，可作为内容输入端口

            20.wc命令：统计内容数量
                wc语法：wc [-c -m -l -w] 文件路径
                不带选项时，输出结果：总行数 单词的数量(按照空格和换行划分) 当前文件的字节数 文件名
                -c选项：可选，统计bytes数量
                -m选项：可选，统计字符数量
                -l选项：可选，统计行数
                -w选项：可选，统计单词数量
                参数：文件路径，被统计的文件，可作为内容输入端口

            21.管道符" | "的概念和应用：
                含义：将管道符左边命令的结果，作为右边命令的输入
                例：1.cat test1.txt | grep "Hello"：
                    输出test1.txt文件内，含有"Hello"的行，即把左边的内容给右边去过滤
                   2.cat test1.txt | wc -l:
                    将test1.txt的文件内容按照 "wc -l"命令输出
                   3.cat test1.txt | grep "s" | grep "y":
                    将test1.txt中含有s的行输出之后，再在输出结果中找出含有y的行输出
                   4.ls / /usr/bin | wc -l

            22.VI\VIM编辑器：文件编辑
                1.简介：vi\vim时visual interface的简称，是Linux中最经典的文本编辑器
                    vi：命令行下对文本文件进行编辑的绝佳选择
                    vim：vi的加强版本，兼容vi的所有指令，不仅能编辑文本，而且还具有shell程序编辑功能，
                        可以不同颜色的字体来辨别语法的正确性，极大方便了程序的设计和编辑性

                2.vi\vim编辑器的三种工作模式：
                    1.命令模式（Command mode）：命令模式下，所敲的案件编辑器都理解为命令，以命令驱动执行不同的功能。
                        此模型下，不能自由进行文本编辑。

                    2.输入模式（Insert mode）：即编辑模式、插入模式。此模式下，可以对文件内容进行自由编辑。

                    3.底线命令模式（Last line mode）：以：开始，通常用于文件的保存、退出。

                3.Vim\Vi工作模式执行方法：
                    vi filename(文件名) → 命令模式：1：输入 i a o → 输入模式 ESC键退出输入模式 返回命令模式
                                                  2：输入":"：进入底线命令模式 命令以回车结束运行
                                                  3：进入底线模式 → 输入":wq"：退出命令模式
                4.语法：
                    1.vi：vi 文件路径
                    2.vim：vim 文件路径
                    注：如果文件路径表示的文件不存在，那么此命令会用于编辑新文件，反之编辑已有文件

                5.命令模式快捷键：详情请看 "vim命令模式快捷键1.png" 和 "vim命令模式快捷键2.png"

                6.底线命令模式：详情请看 "vim底线命令模式快捷键.png"

        2.root用户（超级管理员）
            无论是Windows、MacOS、Linux均采用多用户的管理模式进行权限管理
            root用户：拥有最大的操作系统权限
            普通用户：其权限，一般在其HOME目录内是不受限的，其他地方仅有只读和执行权限，无修改权限

            1.su命令：用于账户切换的系统命令（su：Switch User）
                su语法：su - 用户名
                -：符号可选，表示是否在切换用户后加载环境变量
                参数：用户名，表示要切换的用户，可省略，默认切换到root

                注：使用普通用户，切换到其他用户需要输入密码；
                    使用root用户，切换则不用

            2.exit命令：切换用户后，退回上一个用户，也可以使用快捷键 ctrl + d

            3.sudo命令：在其他命令之前，带上sudo，即可为这条命令临时赋予root授权
                sudo语法：sudo 其他命令
                注：不是所有用户都有权力使用sudo，我们需要为普通用户配置sudo认证

                为普通用户配置sudo认证：
                    1.切换到root用户，执行vi sudo命令，会自动通过vi编辑器打开：/etc/sudoers
                        在文件的最后添加 用户名 ALL=(ALL) NOPASSWD:ALL ，最后通过 wq保存
                    2.NOPASSWD:ALL：表示使用sudo命令，无需输入密码

            4.用户、用户组：
                Linux系统中可以：1.配置多个用户
                               2.配置多个用户组
                               3.用户可以加入多个用户组中

                Linux中关于权限的管控级别：1.针对用户的权限控制
                                       2.针对用户组的权限控制

            5.用户管理：以下命令需root用户执行
                1.创建用户组：groupadd 用户组名
                2.删除用户组：groupdel 用户组名

                3.创建用户：
                    语法：useradd [-g -m -d] 用户名
                    -g选项：可选，指定用户的组，不指定-g，会创建同名组并自动加入，如有同名，必须使用-g
                    -m选项：可选，将文件创建在-d路径下
                    -d选项：可选，指定用户HOME路径，不指定，HOME目录默认在：/home/用户名
                    参数：必填，用户名

                4.删除用户：
                    语法：userdel [-r] 用户名
                    -r选项：可选，删除用户的HOME目录，不使用-r，删除用户时，HOME目录默认保留
                    参数：必填，用户名

                5.查看用户所属组：
                    语法：id [用户名]
                    参数：可选，用户名，不提供时，查看自身

                6.修改用户所属组：
                    语法：usermod [-g -G -aG] 用户组 用户名
                    -g选项：可选，修改用户的主组（primary group），指定的组必须已存在
                    -G选项：可选，重新设置用户的附加组列表（会覆盖原有所有附加组）
                    -aG选项：可选，将用户追加到指定的附加组中（保留原有附加组，必须与-G连用）
                    参数：必填，用户名

            6.getent命令：
                1.查看当前系统中有哪些用户
                    语法：getent passwd
                    结果：用户名:密码(x):用户ID:描述信息(无用):HOME目录:执行终端(默认bash)

                2.查看当前系统中有哪些组
                    语法：getent group
                    结果：组名称:组认证(显示为x):组ID

        3.Linux文件的权限管控信息：
            1.ls -l结果信息解读：
            例：drwxr-xr-x 4 root root 4096 May 11 21:32 study
                    1         2    3
                序号1（drwxr-xr-x）：表示文件、文件夹的权限控制信息
                序号2（root）：表示文件、文件夹的所属用户
                序号3（root）：表示文件、文件夹的所属用户组

            关于序号1（drwxr-xr-x）的具体解读：权限细节总共分为10个槽位（这里我使用"{}"来表示划分的组，"|"来划分槽位）
                -或d或l | { r/- | w/- | x/- } | { r/- | w/- | x/- } | { r/- | w/- | x/- } |
                    a        b：所属用户权限      c：所属用户组权限       d：其他用户权限
                1。-：在a中表示文件，在bcd表示无此权限
                2.d：表示文件夹
                3.l：表示软链接
                4.r：表示读权限，针对文件可以查看文件内容，针对文件夹可以查看文件夹内容
                5.w：表示写权限，针对文件可以修改此文件，针对文件夹可以在文件夹内，创建、删除、改名等操作
                6.x：表示执行权限，针对文件可以将文件作为程序执行，针对文件夹，可以更改工作目录到此文件夹，即cd进入

            例：drwxr-xr-x 4 root root 4096 May 11 21:32 study
            该数据表示：a：该文件为d(文件夹)
                       b：用户（root）对该文件夹的权限是：rwx
                       c：用户组（root）对该文件夹的权限是：r-x
                       d：其他的用户对该文件夹的权限：r-x


            2.chmod命令：修改文件、文件夹的权限信息
                注：只有文件、文件夹的所属用户或root用户可以修改
                chmod语法：chmod [-R] 权限 文件或文件夹
                -R选项：对文件夹内的全部内容应用同样的操作
                例：
                    1.chmod u=rwx,g=rx,o=x hello.txt：将hello.txt文件权限修改成rwxr-x--x
                        其中：u：表示user所属用户权限，g：表示group组权限，o：表示other其他用户权限

                    2.chmod -R u=rwx,g=rx,0=x test：将test文件夹以及文件夹内的全部内容权限修改成rwxr-x--x

                    3.快捷写法：chmod 751 hello.txt：将文件权限修改为751

                权限的数字序号：权限可以用3为数字来代表，第一位数字表示用户权限，第二位数字表示用户组权限，第三位数字表示其他用户权限
                    数字的细节如下：r记为：4；w记为：2；x记为：1；具体详情可以看 "权限的数字序号.png"

            3.chown命令：修改文件、文件夹的所属用户和用户组
                注：普通用户无法修改所属为其他用户或组，所以此命令只适用于root用户执行
                chown语法：chown [-R] [用户][:][用户组] 文件或文件夹
                -R选项：同chmod
                用户选项：用户，修改所属用户
                用户组选项：用户组，修改所属用户组
                :：用于分隔用户和用户组

            例：
                1.chown root hello.txt：将hello.txt所属用户修改为root
                2.chown :root hello.txt：将hello.txt所属用户组修改为root
                3.chown root:student hello.txt：将hello.txt所属用户修改为root，所属用户组修改为student
                4.chown -R root test：将test文件夹所属用户修改为root，并对文件夹内全部内容应用同样规则

    三、Linux实用操作
        1.各类小技巧（快捷键）：
            1.强制停止：ctrl + c
            2.退出、登出：ctrl + d （注：不能用于退出vi/vim）
            3.历史命令搜索：
                1.history命令，查看历史输入过的全部命令
                2.可以通过：!命令前缀，自动执行上一次匹配前缀的命令
                    例：history：  241  python
                                  242  python3
                                  244  hsitory | grep python3
                                  245  history | grep python
                    这时输入 "!p" 时，会自动执行 python3 的命令，从下往上前缀为 p 的命令
                3.可以通过快捷键 ctrl + r，输入内容去匹配历史命令
                    1.回车键可以直接执行
                    2.左右键，可以得到此命令（不执行）

            4.光标移动：
                1.ctrl + a：跳到命令开头
                2.ctrl + e：跳到命令结尾
                3.ctrl + 键盘左键：向左跳一个单词
                4.ctrl + 键盘右键：向右跳一个单词

            5.清屏：（其实向上划还是能看到之前的内容）
                1.ctrl + l，可以清空终端内容
                2.clear命令：语法：clear

        2.软件安装：
            1.操作系统安装软件有许多种方式，一般分为：
                1.下载安装包自行安装：例如：win中的exe、msi文件等，mac中的dmg、pkg文件等
                2.系统的应用商店内安装：例如：win中的Microsoft Store，mac中的AppStore
                3.我们使用的ubantu Linux发行版 为Debian家族
                    Debian家族：使用apt命令， .deb文件格式；
                    Red Hat家族：使用yum命令， .rpm文件格式

            2.ubantu软件安装：apt命令 （注：apt命令需要root权限，可以su切换到root，或使用sudo提权，apt命令需联网使用）
                apt语法：apt [-y] [install | remove | search] 软件名称
                -y选项：可选，自动确认，无需手动确认安装或卸载过程
                install：安装
                remove：卸载
                search：搜索

        3.systemctl命令：控制软件的启动和关闭
            Linux系统很多软件（内置或第三方）均支持使用systemctl命令控制：启动、停止、开机自启
                能够被systemctl管理的软件，一般也称之为：服务
            系统内置的服务比较多，比如：
                1.systemd-networkd：主网络服务
                2.ufw (Uncomplicated Firewall)：防火墙服务
                3.sshd，ssh服务：Xshell远程登录Linux使用的就是这个服务

            1.systemctl命令的使用：
                1.systemctl语法：systemctl start | stop | status | enable | disable 服务名
                2.start：启动
                3.stop：关闭
                4.status：查看状态
                    1.Active: active (running)：表示正在运行中
                    2.Active: inactive (dead)：表示已被关闭
                    3.Loaded: loaded ...service; enabled|disabled：enabled：表示开机自启；disabled：表示不开机自启
                5.enable：开启开机自启
                6.disable：关闭开机自启

            2.将软件集成到systemctl中：
                部分软件安装后没有自动集成到systemctl中，我们可以手动添加

        4.软连接：
            在系统中创建软链接，可以将文件、文件夹链接到其他位置（类似Windows系统中的《快捷方式》）
            1.ln命令：创建软连接
                ln语法：ln -s 参数1 参数2
                -s选项：创建软连接
                参数1：被链接的文件或文件夹
                参数2：要链接去的目的地

        5.日期、时区：
            1.date命令：查看系统的时间
                date语法：date [-d] [+格式化字符串]
                -d选项：可选，按照给定的字符串显示日期，一般用于日期计算
                    例：date -d "+1 day" +%Y%m%d 显示后一天的时间
                        year年
                        month月
                        day天
                        hour小时
                        minute分钟
                        second秒
                格式化字符串：可选 有空格记得用""包围
                    %Y：年
                    %y：年份后两位数字（00~99）
                    %m：月份（01~12）
                    %d：日（01~31）
                    %H：小时（00~23）
                    %M：分钟（00~59）
                    %S：秒（00~60）
                    %s：自 1970-01-01 00:00:00 UTC 到现在的秒数

            2.修改Linux系统的时区
                rm -f /etc/localtime
                sudo ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
                将系统自带的localtime文件删除，并将/usr/share/zoneinfo/Asia/Shanghai文件链接为localtime文件即可

            3.chronyc命令：
                1.强制校准时间：
                    语法：sudo chronyc makestep
                2.查看校准结果：
                    语法：chronyc tracking

        6.IP地址、主机名
            1.IP地址：
                每一台联网的电脑都会有一个地址，用于和其他计算机进行通讯
                IP地址主要有2个版本，V4版本和V6版本
                IPv4版本的地址格式是：a.b.c.d，其中abcd表示0~255的数字，如192.168.99.101就是一个标注的IP地址

                1.ifconfig命令：ifconfig，查看本机ip，如无法使用该命令，可以安装 apt -y install net-tools
                    或 建议使用 ip命令：查看本机ip：语法：ip addr

                特殊的IP地址：
                    1. 127.0.0.1：IP地址用于指代本机
                    2. 0.0.0.0：
                        1.可以用于指代本机
                        2.可以在端口绑定中用来确定绑定关系
                        3.在一些IP地址限制中，表示所有IP的意思，如放行规则设置为0.0.0.0，表示允许任意IP访问

            2.主机名：
                每一台电脑除了对外联络地址（IP地址）以外，也可以有一个名字，称之为主机名
                1.查看主机名：语法：hostname
                2.修改主机名（需root）：语法：hostnamectl set-hostname 主机名,需要修改的主机名

            3.域名解析（主机名映射）：可以通过主机名找到对应计算机的IP地址，这就是主机名映射
                访问域名(网址)的流程：具体请看"域名解析.png"
                    先查看本机的记录（私人地址本）：
                        Windows：C:\Windows\Sysrem32\drivers\etc\hosts
                        Linux：/etc/hosts
                    再联网去DNS服务器(如：114.114.114.114，8.8.8.8等)询问

        7.虚拟机配置固定IP：
            当前我们虚拟机的Linux操作系统，其IP地址是通过DHCP服务获取的
            DHCP：动态获取IP地址，即每次重启后都会获取一次，可能导致IP地址频繁变更
            1.在VMware Workstation中配置IP地址网关和网段（IP地址的范围）
                1.在编辑里面找到虚拟网络编辑器
                2。找到VMnet8设置 "子网IP" 为 192.168.88.0 和 确认 "子网掩码" 是不是 225.225.225.0
                3.点击NAT设置，确定NAT设置里的 "网关IP" 为 192.168.88.2

            2.在Linux系统中手动修改配置文件，固定IP
                1.使用vim编辑/etc/sysconfig/network-scripts/ifcfg-ens33
                    将 BOOTPROTO="dhcp"改为BOOTPROTO="static"
                    然后在最下面添加：1.IPADDR="192.168.88.130" # IP地址
                                   2.NETMASK="255.255.255.0" # 子网掩码固定：255.255.255.0
                                   3.GATEWAY="192.168.88.2" # 网关和VMware虚拟网络编辑器中设置的一致
                                   4.DNS="192.168.88.2" # DNS1设置为网关即可
                2.执行systemctl restart network重启网卡，执行ip addr 或 ifconfig 即可看到ip地址固定为 "192.168.88.130"

        8.网络传输：
            1.下载和网络请求：
                1.ping命令：检查服务器是否可联通
                    ping语法：ping [-c num] ip或主机名
                    -c选项：可选，检查的次数，不使用时，将无限次数持续检查
                    参数：ip或主机名，被检查的服务器的ip地址或主机名地址

                2.wget命令：下载文件
                    wget时非交互的文件下载器，可以在命令行内下载网络文件
                    wget语法：wget [-b] url
                    -b选项：可选，后台下载，会将日志写入到当前工作目录的wget-log文件
                    参数：url，下载链接
                    在后台下载时，可以通过监控后台下载进度：tail -f wget-log
                    注：无论下载是否完成，都会生成要下载的文件，如果下载未完成，请及时清理未完成的不可用文件

                3.curl命令：发送http网络请求，可用于下载文件、获取信息等
                    curl语法：curl [-O] url
                    -O选项：用于下载文件，当url是下载链接时，可以使用此选项保存文件
                    参数：url，要发起请求的网络地址

            2.端口：
                1.端口的概念：
                    端口是指计算机和外部交互的出入口，可以分为物理端口和虚拟端口
                        物理端口：USB、HDMI、DP、VGA、RJ45等
                        虚拟端口：操作系统和外部交互的出入口
                    IP只能确定计算机，通过端口才能锁定要交互的程序

                2.端口的划分：
                    1.公认端口：1~1023，用于系统内置或常用知名软件绑定使用，如SSH服务的22端口，HTTPS服务的443端口
                    2.注册端口：1024~49151，用于松散绑定使用（用户自定义）
                    3.动态端口：49152~65535，用于临时使用（多用于出口）

                3.查看端口的占用情况：
                    命令：ss -tulnp
                    -t 显示TCP，
                    -u 显示UDP，
                    -l 显示监听端口，
                    -n 不解析服务名，
                    -p 显示进程名和PID。

                4.查看指定端口的占用情况：、
                    1.ss -tulnp | grep :8080
                    2.lsof -i :8080

        9.进程管理：
            1.进程的概念：
                进程是指在操作系统内运行后被注册为系统内的一个进程，并拥有独立的进程ID（进程号）

            2.管理进程的命令：
                1.查看进程信息：
                    语法：ps -ef
                    -e选项：显示出全部的进程
                    -f选项：以完全格式化的形式展示信息（展示全部信息）
                    结果数据分析：从左往右
                        UID：进程所属的用户ID
                        PID：进程的进程号ID
                        PPID：进程的父ID（启动此进程的其他进程）
                        C：此进程的CPU占用率（百分比）
                        STIME：进程的启动时间
                        TTY：启动此进程的终端序号，如显示"?"、表示非终端启动
                        TIME：进程占用CPU的时间
                        CMD：进程对应的名称或启动路径或启动命令

                2.过滤指定关键字进程信息
                    语法：ps -ef | grep 关键字

                3.关闭指定进程号的进程：
                    语法：kill [-9] 进程号
                    -9选项：可选，强制关闭

        10.主机状态：主机运行状态的监控命令
            1.查看系统资源占用：通过top命令查看CPU、内存使用情况，类似Windows的任务管理器
                1.语法：top
                注：默认五秒刷新一次，按q或ctrl + c退出
                2.top命令内容详解：具体请看 "top命令内容详解1.png" 和 "top命令内容详解2.png"
                3.top命令的选项：具体请看 "top命令的选项.png"
                4.top命令的交互式选项：具体请看 "top命令的交互式选项.png"

            2.磁盘监控：
                1.查看硬盘的使用情况：
                    语法：df [-h]
                    -h选项：以更加人性化的单位显示

                2.查看CPU、磁盘的相关信息：
                    语法：iostat [-x] [num1] [num2]
                    -x选项：显示更多信息
                    num1：数字，刷新间隔
                    num2：数字，刷新几次

                    内容详解：具体请看 "iostat -x命令内容详解.png"
                        tps：该设备每秒的传输次数；
                        "一次传输"的意思是"一次I/O请求"，多个逻辑请求可能会被合并为"一次I/O请求"，"一次传输"请求的大小是未知的。

            3.网络状态监控：
                1.查看网路的相关统计（sar命令非常复杂，这里仅简单用于统计网络）
                    语法：sar -n DEV num1 num2
                    -n选项：查看网络，DEV表示查看网络接口
                    num1：刷新间隔，不填默认查看一次就结束
                    num2查看次数，不填默认查看无限次
                    内容详解：请看 "sar -n DEV内容的详解.png"

        11.环境变量：是一组信息记录，类型是KeyValue型（名称=值），用于操作系统运行的时候记录关键信息
            1.查看当前系统配置的环境变量信息：语法：env

            2.符号 "$" 的作用：取出环境变量的值
                例：echo $PATH 或 echo ${PATH}ABC

            4.什么是PATH，作用是：
                环境变量PATH会记录一组目录，目录之间用":"隔开。
                这里记录的是命令的搜索路径，当执行命令会从记录中记录的目录中挨个搜索要执行的命令并执行。
                可以通过修改这个项目的值，加入自定义的命令搜索路径
                例：export PATH=$PATH:自定义路径

            3.在Linux中配置环境变量：
                1.临时生效：export 名称=值
                2.永久生效：
                    1.针对当前用户，配置在当前用户的：~/.bashrc文件中配置
                    2.针对全部用户，配置在系统的：/etc/profile文件中配置
                    3.配置完成，可以通过source命令立即生效，例：source /etc/profile
                    注：export PATH=$PATH:添加的路径，记得加上$PATH不然会覆盖

        12.上传、下载
            rz、sz命令需要安装，可以通过apt -y install lrzsz
            1.上传：语法：rz
            2.下载：语法：sz 要下载的文件

        13.压缩、解压:
            Linux系统常用的压缩格式有：
                1.tar格式，归档文件建档的将文件整合到一个文件内，无压缩效果
                2.gizp格式：gizp压缩文件，不仅能整合到一个文件，同时有体积压缩效果
            1.tar命令：压缩或解压tar或gzip文件
                语法：tar [-c -v -x -f -z -C] 参数1 参数2 ... 参数N
                主要使用：tar -czvf 或 tar -xzvf即可
                -c选项：创建压缩文件，用于压缩模式
                -v选项：显示压缩、解压过程、用于查看进度
                -x选项：解压模式
                -f选项：要创建的文件，或要解压的文件，-f选项必须在所有选项中位置处于最后一个
                -z选项：gzip模式，不适用-z就是普通的tarball格式
                -C选项：选择解压的目的地，用于解压模式
                例：1.tar -cvf test.tar 1.txt 2.txt 3.txt：
                        将 1.txt 2.txt 3.txt 压缩到test.tar文件内。
                   2.tar -zcvf test.tar.gz 1.txt 2.txt 3.txt：
                        将 1.txt 2.txt 3.txt 压缩到test.tar.gz文件内，使用gzip模式
                   3.tar -xvf test.tar：
                        解压test.tar，将文件解压至当前目录
                   4.tar -xvf test.tar -C /home/student：
                        解压test.tar，将文件解压至指定目录（/home/student）
                    5.tar -zxvf test.tar.gz -C /home/student：
                        以Gzip模式解压test.tar.gz，将文件解压至指定目录（/home/student）
                   注：1.-z选项如果使用的话，一般处于选项位第一个
                      2.-f选项，必须在选项位最后一个
                      3.-C选项单独使用，和解压所需的其他参数分开


            2.zip、unzip命令，压缩或解压zip文件：
                1.压缩zip文件：zip命令
                    zip语法：zip [-r] 参数1 参数2 ... 参数N
                    -r选项：被压缩的包含文件夹的时候，需要使用-r选项，和rm、cp等命令-r效果一致
                    例：1.zip test.zip a.txt b.txt c.txt：
                            将 a.txt b.txt c.txt 压缩到test.zip文件内
                        2.zip -r test.zip test1 test2 test3 test1.txt：
                            将 test1、test2、test3三个文件夹和 test1.txt文件，压缩到test.zip文件内

                2.解压zip文件：unzip命令
                    unzip语法：unzip [-d] 参数
                    -d选项：指定要解压去的位置，同tar的-C选项
                    参数：被解压的zip压缩包文件
                    例：1.unzip test.zip：将test.zip解压到当前目录
                        2.unzip test.zip -d /home/student：将test.zip文件解压到指定文件夹内（/home/student）

    四、软件连接Xshell VMware Ubantu
        1、远程连接与权限切换
            1. 连接工具: Xshell （Linux发行版为 ubantu 26.04，虚拟机软件：VMware）
            2. 登录用户: student
            3. 获取管理员权限: sudo -i   (输入 student 的密码)
            4. 退出管理员模式: exit      (或 Ctrl + D)

        2、设置静态 IP (让 IP 地址固定)
            1. 查看网卡信息:
               ip addr   (找到你的网卡名，比如 ens33)

            2. 编辑配置文件:
               sudo nano /etc/netplan/01-netcfg.yaml

            3. 配置内容 (按此修改)
                # 网络配置版本，不用改
                network:
                version: 2
                # 有线网卡配置
                ethernets:
                ens33:                         # 网卡名称（虚拟机里的网卡）
                    dhcp4: false                 # true=自动获取IP，false=手动设置
                    dhcp6: true
                addresses:                   # ↓ 虚拟机IP地址和子网掩码
                    - 192.168.182.100/24       # 虚拟机IP：192.168.182.100 丨 /24 = 子网掩码255.255.255.0 丨 网段：192.168.182.0
                routes:                      # ↓ 网关配置
                  - to: default              # 所有出站流量
                    via: 192.168.182.2       # 网关 = VMware NAT网关（VMnet8的.2）
                nameservers:                 # ↓ DNS服务器
                    addresses:
                    - 119.29.29.29           # 腾讯DNS
                    - 8.8.8.8                # Google DNS
                match:
                    macaddress: # 根据MAC地址匹配网卡
                set-name: ens33

            4. 保存并应用修改:
               Ctrl + O 回车保存
               Ctrl + X 退出编辑
               sudo netplan apply

        3、常用命令速查表
            类别          命令                      作用
            文件管理      ls -l                   显示详细信息
                        cd ..                   返回上一级
                        mkdir 文件夹名            创建文件夹
                        rm 文件名                 删除文件

            网络        ping 8.8.8.8            测试网络
                       curl www.baidu.com      测试网站访问

            权限        sudo -i                 切换到 root
                       passwd root             修改 root 密码

            系统        apt update              更新软件源
                       apt install 软件名       安装软件
                       reboot                  重启系统
"""
