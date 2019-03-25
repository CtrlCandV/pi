DS18B20 教程：https://www.52pojie.cn/thread-902898-1-1.html
JQC-3FF 教程：https://www.52pojie.cn/thread-903925-1-1.html

SG90为90g舵机，其他舵机通用，SG90-2同为控制舵机的程序，但是次程序是使舵机0-180度来回旋转。SG90是询问用户度数，随后转到对应d度数

凡是报错无法引入passwd错误的，请在程序同级目录下增加文件passwd.py
内部内容如下：
class passwd(object):
    def __init__(self):
        self.user="数据库用户名"
        self.password="数据库密码"
        self.host="数据库ip地址"
    def getUser(self):
        return self.user
    def getpasswd(self):
        return self.password
    def getHost(self):
        return self.host


如此，即可正常使用。