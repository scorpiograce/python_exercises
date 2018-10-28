def test1(para1,para2,para3):
    print ('-------1-start------')
    print ("三个参数分别是：%s %s %s" %(para1,para2,para3))
    print ('-------1-end------')
def test2():
    print ("--------2-start-----")
    para1=input("请输入参数1：")
    para2=input("请输入参数2：")
    para3=input("请输入参数3：")
    test1(para1,para2,para3)
    print ("--------2-end-----")
test2()