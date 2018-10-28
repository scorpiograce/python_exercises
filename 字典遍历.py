#字典遍历：for … in…
#只对键的遍历：
d={'name1':'pythontab','name2':'.','name3':'com'}
for key in d:
    print(key,'value:',d[key])

#对键和值都遍历：
for key,value in d.items():
    print(key,'value:',value)
