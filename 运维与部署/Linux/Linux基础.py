"""
    一、基础知识
        1. Linux系统的组成：
            1.Linux系统内核：内核提供系统最核心的功能，如：调度CPU、调度内存、调度文件系统、调度网络通讯、调度IO等
            2.系统级应用程序

            用户 → 使用第三方程序/系统程序  → 调用内核 → 调度硬件

        2. 虚拟机：通过虚拟化技术，在电脑内，虚拟出计算机硬件，并给虚拟的硬件安装操作系统，即可得到一台虚拟的电脑，称之为虚拟机。

    二、远程连接与权限切换
        1. 连接工具: Xshell （Linux发行版为 ubantu 26.04）
        2. 登录用户: student
        3. 获取管理员权限: sudo -i   (输入 student 的密码)
        4. 退出管理员模式: exit      (或 Ctrl + D)

    二、设置静态 IP (让 IP 地址固定)
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

    三、常用命令速查表
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

    四、常见问题解决
    1. 卡在 vim 界面退出不了:
       按 Esc -> 输入 :q! -> 回车

    2. Xshell 连不上提示 Access denied:
       不要直接连 root。用 student 连上后，再用 sudo -i 切换到 root。

    3. 修改网卡配置后不生效:
       执行 sudo netplan apply

"""