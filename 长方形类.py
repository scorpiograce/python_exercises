#定义一个长方形类，定义两个属性长和宽，定义一个方法，返回面积

class rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def getarea(self):
        print("面积是：",self.length*self.width)
        return self.length*self.width

aRectangle=rectangle(5,3)
aRectangle.getarea()