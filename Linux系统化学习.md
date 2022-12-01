# Linux系统化学习

#### 指定运行级别：

设置默认的3等级，多用户服务器

systemctl set-default multi-user.target 

图形界面5等级

systemctl set-default graphical.target

#### 找回root密码：

1. 开机界面前五秒内按e;

2. 找到utf-8后面添加：init=/bin/sh  

3. ctrl+x 进入单用户模式

4. mount - o remount,rw /   :回车单词与/之间有空格

5. passwd   :回车

6. 输入两次密码

7. touch / .autorelabel

8. exec /sbin/init     等待重启（时间有点长）


#### 创建目录

mkdir A; 默认创建一级目录

mkdir -p /home/num/B 创建多级目录num/B

#### 删除目录;文件

rmdir A; 删除空白目录

rm -rf  A;强制删除文件，目录（小心点使用）

-r 表示提示是否删除;

-f 表示强制删除不提示;

#### 创建文件

touch A.txt

空文件;

#### cp拷贝

cp /home/A /home/bbb

cp [参数] 文件地址 目标地址 单个地址

cp /home/bbb /opt  复制目录

目标地址存在时前面加\cp 不提示覆盖。" \"\

#### mv指令

mv /home/A /home/B   同级目录下mv表示重命名；

mv /home/A /opt/B/c 不同级目录代表移动文件或者目录；c表示重命名

A目录下面还可以mv同名目录

#### cat指令more；less

cat查看文件内容;

cat -n 文件;

一般加上管道|符号表示cat查的传递给后面处理。

cat -n /home/A | more或者less

more是交互指令

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119114033123.png" alt="image-20221119114033123" style="zoom: 50%;" />

more也可以单独使用；



less可以单独使用,可以边看加载文件,效率高一点，查看大文件时使用比more好.

less A;

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119114850623.png" alt="image-20221119114850623" style="zoom:50%;" />

echo指令

输出到控制台如 echo hostname   显示hostname；

echo $HOSTNAME  显示主机名  $HOSTNAME是变量;

#### head指令

head A;

查看文件前10行，空格行也算；

head -n 20;表示查看文件前20行;

#### tail指令重定向>与追加>>

tail A;

与head相反,查看文件尾端;

tail -f a.txt;

时实显示a.txt内容的情况

时实监控文件a,txt；

echo "内容" > /home/hubo/a.txt  >覆盖

echo "内容" > /home/hubo/a.txt >>追加

案列：ls -l /home/ > /home/info.txt

cal 单月日期

cal 2022年日期表

#### 软硬链接

ln -s 原文件 软链接建立的目录

软链接相当于快捷方式

[root@hb home]# ln -s /root myln

在home目录下创建软链接到root目录

#### history指令

history查看历史所有指令

history num；显示num条指令。

！加历史指令，执行

！5

#### 时间日期



<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119162912947.png" alt="image-20221119162912947" style="zoom:50%;" />

[root@hb home]# date "+%Y:%m:%d %H:%M:%S "
2022:11:19 03:35:28 

大小写要注意；

date -s "2022-11-19 16:40:50"

设置系统时间

cal；cal 2022；

#### fing查找指令

fing /home -name hiok.txt

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119165938054.png" alt="image-20221119165938054" style="zoom:50%;" />



 find / -size +200M在root 查找200M以上的文件

ls -lh 按照人能看的显示如字节显示成M

#### locate指令

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119172218099.png" alt="image-20221119172218099" style="zoom:50%;" />

updatedb

locate 文件；

which 命令 ；命令放在那个目录下；

#### grep

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119174855727.png" alt="image-20221119174855727" style="zoom:50%;" />

cat /etc/passwd |grep -n "hubo"

grep -n "hubo"/etc/passwd

两种写法

#### zip/unzip压缩解压指令

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119201910515.png" alt="image-20221119201910515" style="zoom:50%;" />

 zip -r myhome.zip /home/ 压缩

unzip -d /opt/tomp/ /home/myhome.zip 解压

#### tar

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119203007064.png" alt="image-20221119203007064" style="zoom:50%;" />

 tar  -zcvf  **pc.tar.gz**   cat.txt pig.txt  压缩名加粗

tar -zxvf pc.tar.gz 解压

 tar -zxvf myhome.tar.gz -C /opt/tomp 

-C 表示解压到那个目录

## 组管理和权限管理

#### Linux基本组的介绍

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119211219872.png" alt="image-20221119211219872" style="zoom:50%;" />

#### 文件；目录所有者

ls -ahl 查看文件信息；apple.txt属于root组

![image-20221119211942585](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119211942585.png)

chown hubo apple.txt

![image-20221119213829890](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119213829890.png)

改变用户组为hubo，

语法：chown 用户 文件;

用户创建的文件，文件属于用户的组，下面为momster

sky monster 0 Nov 19 21:09 apple.txt

#### 组的创建

groupadd 组名；

创建用户指定组

useradd -g 组名 用户名

#### 修改文件；文件所有组

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119214525955.png" alt="image-20221119214525955" style="zoom:50%;" />

​    groupadd fruit
​    chgrp fruit orange

由root改成fruit文件组

​    chgrp fruit orange.txt 

#### 其他组

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119215720815.png" alt="image-20221119215720815" style="zoom:50%;" />

改变组，sky由manter改成hubo组

usermod -g hubo sky

#### 权限的基本介绍

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119220955194.png" alt="image-20221119220955194" style="zoom:50%;" />

-表示普通文件；

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119221655012.png" alt="image-20221119221655012" style="zoom:50%;" />

可执行文件表示如cd

#### 修改权限chmod

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221119222707731.png" alt="image-20221119222707731" style="zoom:33%;" />

chmod 751 文件名

#### 修改文件；目录所有者-chown

改变所有者

chown 新的所有者 文件或者目录 

改变所有者和所在组

chown 新的所有者：新的所在组 文件或者目录

如果是目录的话要-R递归生效,文件和目录都会生效。

chown -R hubo /home/kkk/

chown hubo /home/hiok.txt 

#### 修改文件；目录所在组-chgrp

chgrp 新所在组 /文件目录地址

chgrp mingjiao /home/abc.txt  文件

chgrp -R mingjiao /home/kkk/ 目录

#### crond任务调度

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120153628030.png" alt="image-20221120153628030" style="zoom:50%;" />

service crand restart 重启任务调度

crontab -e

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120155404822.png" alt="image-20221120155404822" style="zoom:50%;" />

注意sh脚本需要执行权限。

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120162317040.png" alt="image-20221120162317040" style="zoom:50%;" />

#### at定时任务

ps -ef | grep atd  查看atd任务进程在启动没有；



<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120163430397.png" alt="image-20221120163430397" style="zoom:50%;" />

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120163516401.png" alt="image-20221120163516401" style="zoom:50%;" />

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120163902349.png" alt="image-20221120163902349" style="zoom:50%;" />

![image-20221120164708239](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120164708239.png)

按两次Ctrl + d

atq查看系统中的任务

![image-20221120165330890](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120165330890.png)

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120185554245.png" alt="image-20221120185554245" style="zoom:50%;" />

#### LIinux分区

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120190645671.png" alt="image-20221120190645671" style="zoom:50%;" />

lsblk 查看所有设备的挂载情况

lsblk -f 更加详细

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120191957140.png" alt="image-20221120191957140" style="zoom:50%;" />

#### 增加磁盘

wm虚拟机先增加硬盘sdb；

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120193746586.png" alt="image-20221120193746586" style="zoom:50%;" />

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120195054547.png" alt="image-20221120195054547" style="zoom:50%;" />

![image-20221120200322145](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120200322145.png)

#### 磁盘情况查询

查询系统整体磁盘使用情况

df -h

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120201947008.png" alt="image-20221120201947008" style="zoom:50%;" />

#### 查询指定目录的磁盘占用情况

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120202658221.png" alt="image-20221120202658221" style="zoom:50%;" />

--max-depth=1 等价于  -d 1

![image-20221120203129073](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120203129073.png)

du -ha --max-depth=1 /opt

#### 磁盘实用命令

统计文件个数

 ls -l /opt | grep "^-" | wc -l

统计目录个数

ls -l /opt | grep "^d" | wc -l

统计文件个数包括子文件夹

ls -lR /opt | grep "^-" | wc -l

统计目录个数包括子目录

ls -lR /opt | grep "^d" | wc -l

wc指令参数：-l/-c/-m/-w -->计算行数/字节数/字符数/单次数

R参数一般表示递归；

以树状显示目录结构tree 目录；没有的话要下载；

yum install tree

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120205247230.png" alt="image-20221120205247230" style="zoom:50%;" />



#### 进程

ps -aux

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120224407516.png" alt="image-20221120224407516" style="zoom:50%;" />

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120224912269.png" alt="image-20221120224912269" style="zoom:50%;" />

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120225410627.png" alt="image-20221120225410627" style="zoom:50%;" />

#### 显示系统执行的进程

ps -ef

#### 父子进程

待

#### 终止进程kill和killall

kill 进程号

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120232448908.png" alt="image-20221120232448908" style="zoom:50%;" />

#### 查看进程树

pstree -p 显示进程号

![image-20221120232812108](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120232812108.png)

pstree -u 显示进程所属用户

![image-20221120233203190](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221120233203190.png)

#### 服务管理

#### service

service network stop  关闭网络

service network start 开启网络

![image-20221122113211819](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221122113211819.png)

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221122113221367.png" alt="image-20221122113221367" style="zoom:50%;" />

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221122113229629.png" alt="image-20221122113229629" style="zoom:50%;" />

 chkconfig --list

chkconfig --level 2 network off

需要重启！

#### systemctl  服务指令

ls -l /usr/lib/systemd/system  |grep 服务名  查看服务名模糊

![image-20221122150106335](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221122150106335.png)

systemctl is-enabled firewalld 查看防火墙是否自启动

systemctl is-enabled sshd   sshd是否自启动

systemctl status firewalld   查看防火墙状态

![image-20221122143130481](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221122143130481.png)

systemctl stop firewalld  关闭防火墙

![image-20221122143914639](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221122143914639.png)

防火墙只是临时的，systemctl stop firewalld  

开机之后会还原成以前对服务的设置

要永久设置需要：enable自启动    disaable 关闭自启动

systemctl disable firewalld  关闭防火墙自启动

systemctl is-enabled firewalld  查看防火墙是不是自启动

systemctl list-unit-files 开机启动状态 可以加管道过滤

![image-20221122145418730](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221122145418730.png)



#### 防火墙firewall指令

![image-20221122150604618](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221122150604618.png)



telnet ip 端口 ； 测试端口是不是能够连接 

netstat -anp |more 查看端口和协议

firewall -cmd --permanent --add-port=111/tcp  打开111端口

firewall-cmd --reload  需要重新载入才能生效

firewall -cmd --permanent --remove-port=111/tcp  关闭111端口

firewall-cmd --zone=public --list-ports 查看已经开放的端口号

#### 动态监控进程 top

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221122154835157.png" alt="image-20221122154835157" style="zoom:50%;" />

top指令与ps相似，他是执行一段时间后会更新正在运行的进程；

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221122155300883.png" alt="image-20221122155300883" style="zoom:50%;" />



top是：系统运行时间； load average :负载均衡三数之和不能太大

zombie 是僵死进程，没有运行但是内存没有释放；

MIB MEMl:是内存

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221122160108350.png" alt="image-20221122160108350" style="zoom:50%;" />

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221122160208198.png" alt="image-20221122160208198" style="zoom:50%;" />

交互下：输入u ；用户名；监控用户

​                 输入K ;进程号；终止进程

可以动态监控和交互

#### 监控网络状态

netstat -an | more   -an是按照顺序排列输出

netstat - | more   -p是显示那个进程在调用

netstat -anp | grep ssh

ping 对方ip地址 

![image-20221122162401700](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221122162401700.png)

#### rpm包管理、

查看安装的软件

rpm -qa |grep jdk 

查看是否安装软件

rpm -q firefox

查看安装软件包的信息

rpm -qi firefox

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221124183220307.png" alt="image-20221124183220307" style="zoom:50%;" />

查看软件包中的文件

rpm -ql firefox

查文件所属的软件包

rpm -qf /etc/passwd

rpm -qf 文件全路径名

#### 卸载安装rpm包

卸载rpm -e 软件

一定要删除，加参数--nodeps

rpm -e --nodeps 软件

安装软件rpm -ivh 安装包的路径

rpm -ivh /opt/firefox-68.10.0-1.el7.centos.x86_64.rpm 

![image-20221124184543292](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221124184543292.png)

#### yum软件包管理器

自动处理依赖关系

查询是否有需要的软件

yum list | grep 软件

安装软件

yum install 软件

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221124185424066.png" alt="image-20221124185424066" style="zoom:33%;" />

#### 安装配置jdk

![image-20221124193742052](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221124193742052.png)

export JAVA_HOME=/usr/local/java/jdk1.8.0_281
export PATH=$JAVA_HOME:&PATH

source /etc/profile 更新一下配置文件！

#### cat



#### mysql安装与找回密码

**找回密码**

登录成功以后出现这个修改密码强度

**ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executing this statement**

1：set global validate_password_policy=LOW;

2： set global validate_password_length=6;

3：alter user user() identified by "123456";  

4：FLUSH PRIVILEGES; 

### sh编程

#### sh变量

a=10 变量定义不能有空格

echo $a 输出要加$

echo "a=$a" --->a=10

unset a删除变量

readonly b=2 是静态变量,不能使用unset删除；

变量不能以数字开头；

变量名习惯性大写；这个是一个规范

反引号：C=`date`TAB上面的`

或者 F=$(date)

#### 设置环境变量

export 变量名=变量值 全局变量

![image-20221124223925351](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221124223925351.png)

#### shell多行注释

:<<! 

内容

 ! ![image-20221124224906217](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221124224906217.png)

#### 位置参数

![image-20221125134548363](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125134548363.png)

echo $0 $1 $2 $3
echo $*          
echo $@
echo $#

![image-20221125134944228](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125134944228.png)

#### 预定义变量

![image-20221125135929770](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125135929770.png)

![image-20221125140028540](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125140028540.png)

![image-20221125140042157](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125140042157.png)

#### 运算符

![image-20221125140924607](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125140924607.png)

#!/bin/bash
num1=$(((2+3)*4))
echo $num1
num2=$[(3+3)*2]
echo $num2
num3=`expr 2 + 3`
num4=`expr $num3 \* 4`    用小瓜号反引号引起来``

#### 条件判断

![image-20221125145521808](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125145521808.png)

![image-20221125150308774](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125150308774.png)

条件与[ ]  要有空格

[  ]没有条件也要空格

if [  ] 非空为真，无为假，后面还有条件继续执行。

#### 控制流程

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125151248597.png" alt="image-20221125151248597" style="zoom:50%;" />

case语法

#!/bin/bash
case $1 in
"1")
echo "星期一"
;;
"2")
echo "星期二"
;;
*)
echo "要周末了"
;;
**esac语法**
           

![image-20221125153229499](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125153229499.png)

**for循环***

![image-20221125154502242](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125154502242.png)

$*是全部输出

$@是顺序输出

#!/bin/bash
SUM=0
for(( i=1; i<=100; i++))
do
  SUM=$[$SUM+$i]
done
echo $SUM

![image-20221125164307556](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125164307556.png)

变量定义不能有空格  SUM=$[$SUM+$i]  

##### while循环

#!/bin/bash
SUM=0
i=0
while [ $i -le $1 ]
do
        SUM=$[$SUM+$i]
        i=$[$i+1]
done
echo $SUM

![image-20221125165650711](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125165650711.png)

whlie  [  条件判断  ]  要有空格

#### read读取控制台输入

#!/bin/bash
read -p "请输入一个数=" NUM1
echo $NUM1

read -t 5 -p "请五秒内输入一个数=" NUM2
echo $NUM2

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125173512461.png" alt="image-20221125173512461" style="zoom:50%;" />

-p提示信息；-t 5 时间

#### 函数

basename 文件路径 后缀--->文件名

basename /home/dome/re.sh .sh

![image-20221125173654891](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125173654891.png)

dirname 文件路径 -->文件路径

dirname /home/dome/re.sh 

![image-20221125173922714](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125173922714.png)

**自定义函数**

#!/bin/base
function getSUM() {
        SUM=$[$N1+$N2]
        echo "两个数之和是:$SUM"
}
read -p "请你输入的一个数子：" N1
read -p "请你输入的二个数子：" N2
getSUM $N1 $N2

![image-20221125175536101](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221125175536101.png)

#### 定时备份数据库

#!/bin/bash
#备份目录
BACKUP=/data/backup/db
#获取当前时间
DATETIME=$(date +%Y-%m-%d_%H%M%S)
echo $DATETIME
HOST=localhost
DB_USER=root
DB_PW=123456

#备份数据库名

DATABASE=hubo

[ ! -d "${BACKUP}/${DATETIME}" ] && mkdir -p "${BACKUP}/${DATETIME}"

#### ubuntu安装

#### APT 

![image-20221126105115402](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126105115402.png)

netstat -anp 查看运行端口服务



##### ubuntu服务集群远程连接

ssh 用户名@ip

ssh hubo@192.168.10.134

可以互相互连接包括centos

exit 退出

#### 系统日志

![image-20221126153328053](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126153328053.png)

#### 自定义日志服务

**vim /etc/rsyslog**

![image-20221126161932140](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126161932140.png)

![image-20221126161947780](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126161947780.png)

![image-20221126162116207](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126162116207.png)

![image-20221126162720620](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126162720620.png)

**/var/log  存放常用日志文件**

#### 日志轮替

![image-20221126163655314](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126163655314.png)

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126164233808.png" alt="image-20221126164233808" style="zoom:50%;" />

**cd /etc/logrotate.d**

日志轮替规则文件

#### 查看内存日志

![image-20221126170047245](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126170047245.png)

![image-20221126170222280](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126170222280.png)

#### 原理图

<img src="C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126170838026.png" alt="image-20221126170838026" style="zoom:50%;" />

#### 自定义Linux系统





#### LINUX内核阅读源码

内核地址：kernel.org

#### 备份dump

是针对分区的，目录和文件不支持增量备份。

![image-20221126204233683](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126204233683.png)

![image-20221126202310632](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126202310632.png)

增量备份需要带参数u，c代表数字层级。

![image-20221126202341575](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126202341575.png)

dump -0uj -f /opt/boot.bak0.bz2 /boot/  备份boot分区

![image-20221126203316289](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126203316289.png)

最多到九个备份，就会轮替。

dump W  如上参数

![image-20221126203604157](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126203604157.png)

cat /etc/dumpdates 查看备份时间文件

![image-20221126203748357](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126203748357.png)

### 恢复restore

![image-20221126205132844](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126205132844.png)

restore -C -f boot.bak1.bz2 比较模式，备份文件与原文件的区别

![image-20221126205302528](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126205302528.png)

如上是不同的。

restore -t -f boot.bak1.bz2  查看备份文件

restore -r -f /opt/boot.bak1.bz2  还原模式恢复

要从0级顺序恢复

#### webmin安装配置

修改密码为hubo

/usr/libexec/webmin/changepass.pl /etc/webmin root hubo

修改端口

vim /etc/webmin/miniserv.conf 

![image-20221126222413802](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126222413802.png)

![image-20221126222422112](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126222422112.png)

两个地方

![image-20221126222625361](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126222625361.png)

firewall-cmd --zone=public --add-port=011122/tcp --permanent  开放端口

![image-20221126223529389](C:\Users\胡博\AppData\Roaming\Typora\typora-user-images\image-20221126223529389.png)

用户root mm：hubo

#### 面试题

awk；cut 不能空格分隔
