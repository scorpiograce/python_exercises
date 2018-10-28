username="xly"
password="12345678"
"""
i=3
while(i>0):
    name = input("请输入用户名：")
    pw = input("请输入密码：")
    if((name==username)and(pw==password)):
        print("恭喜，登录成功")
    else:
        i-=1
        if(i==0):
            print("三次机会已用完，登录失败")
"""
"""
i=0
while(1):
    name = input("请输入用户名：")
    pw = input("请输入密码：")
    if((name==username)and(pw==password)):
        print("恭喜，登录成功")
        break
    else:
        i+=1
        if(i==3):
           print("三次机会已用完，登录失败")
           break
"""
i=1
while True:
    name = input("请输入用户名：")
    pw = input("请输入密码：")
    if((name==username)and(pw==password)):
        print("恭喜，登录成功")
        break
    elif(i>=3):
           print("三次机会已用完，登录失败")
           break
    else:
        print("用户名或密码输入错误，请重新输入。")
        i+=1
        #continue