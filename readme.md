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

# Fabric并行执行

Fabirc还可以并行执行，通过`--parallel`参数开启并行，通过`--pool-size`指定线程个数。

我们在ls中sleep 3秒，比较一下使用并行和不使用并行的差异。

    def ls(path='.'):
        run('ls {}'.format(path))
        time.sleep(3)

下面是使用并行和不使用并行时的执行时间消耗，可以看到，使用并行能够显著地降低命令的执行时间。

    $ time fab --hosts=`cat hosts | xargs | tr ' ' ','` --user=rds-user --port=1046 --fabfile=fabfile.py ls:~/log
    real    0m7.050s
    user    0m0.372s
    sys     0m0.028s
    
    $ time fab --pool-size=3 --parallel --hosts=`cat hosts | xargs | tr ' ' ','` --user=rds-user --port=1046 --fabfile=fabfile.py ls:~/log
    real    0m3.779s
    user    0m0.380s
    sys     0m0.052s

# Fabric示例1


获取所有的task：

    fab --hosts=`cat hosts | xargs | tr ' ' ','` --user=rds-user --port=1046 --fabfile=upload_file.py --list

执行单个task：

    fab --hosts=`cat hosts | xargs | tr ' ' ','` --user=rds-user --port=1046 --fabfile=upload_file.py tar_task

一次执行所有操作：

    fab --hosts=`cat hosts | xargs | tr ' ' ','` --user=rds-user --port=1046 --fabfile=upload_file.py go

# Fabric示例2

部署flask应用：

    fab --hosts=`cat hosts | xargs | tr ' ' ','` --user=rds-user --port=1046 --fabfile=fabfile_app.py depoly
