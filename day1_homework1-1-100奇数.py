# 输出1-100以内的奇数
"""
#方法1：
for i in range(1, 101):
  if(i%2!=0):
      print(i)
"""
"""
#方法2：
for i in range(1, 101):
  if(i%2==1):
      print(i)
"""

#方法3：速度慢
i=1
while i<=100:
    if(i%2!=0):
        print(i)
    i=i+1