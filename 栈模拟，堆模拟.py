#栈模拟，先进的后出
#利用list的有序和list中pop方法的特性(删除并返回最后一个),来实现栈模拟
'''
list=[]
list.append(1)
list.append(2)
list.append(3)
while len(list)!=0:
    str=list.pop()
    if str==3:
        list.append(4)
        list.append(5)
    print(str)

'''
#堆模拟  先进的先出

import collections
list=collections.deque()
list.append(1)
list.append(2)
list.append(3)

while len(list)!=0:
    str=list.popleft()
    if str==3:
        list.append(4)
        list.append(5)
    print(str)

