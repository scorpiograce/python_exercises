import sys
sys.path.append("..") #..是把当前路径的上一级路径添加进可查询的路径里，从user文件夹下开始查询
print(sys.path)
from config.config import data_file #config前不用加user了
print(data_file)

def get_all():
    print("所有用户数据")

def add(name,password):
    print("添加用户成功")

def check(name,password):
    print("用户存在")


