# Fabric使用说明

乐岸教育Fabric教程<http://www.leanntech.com>

# Fabric使用入门

fab的使用方法如下：

    fab hostname
    fab ls

hostname函数本身就没有参数，但是，函数ls可以接受参数，带参数的函数通常使用默认参数，不过我们也可以执行参数的取值，例如：

    fab ls:~

对于多个参数的情况，使用逗号分隔即可，和Python的函数一样，我们既可以参数位置参数，也可以传递关键字参数，如下所示：

    fab tail:/etc/passwd
    fab tail:/etc/passwd,20
    fab tail:path=/etc/passwd,line=20
    fab tail:line=20,path=/etc/passwd

# 通过命令行指定Fabric的参数

可以通过`fab --help`看到fab的参数信息。例如，我们通过命令行执行hosts、port和用户名等，如下所示：

    fab --hosts=`cat hosts | xargs | tr ' ' ','` --user=rds-user --port=1046 --fabfile=fabfile.py ls:~/log
