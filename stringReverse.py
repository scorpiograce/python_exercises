aStr="12345"
print(aStr[0:5:1])
print(aStr[0::1])
print(aStr[:5:1])
print(aStr[0:4:1])
print(aStr[::1])
print(aStr[::2])
print(aStr[::-1]) #字符串取反
print(aStr[::-2])
print(aStr[::-3])
print(aStr[-1:-4:-1])
print(aStr[-1:-5:-2])

aList=["a","b","c"]
print(aList[::-1])

strA = "abcde"
order = []
for i in strA:
  order.append(i)
order.reverse()   #将列表反转
print(''.join(order))    #将list转换成字符串
