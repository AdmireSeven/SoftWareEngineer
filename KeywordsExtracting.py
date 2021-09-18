'''
author: Yaqi Zhang
Function: Keywords Extracting
Email: admireseven@163.com
'''
import cProfile
import os
import re
from CommentReplace import replace_comment
from SpaceReplace import replace_space

class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def value(self,num):
        return self.items[num]

kw_list = ['auto','break','case','char','const','continue','default','do',
          'double','else','enum','extern','float','for','goto','if',
          'int','long','register','return','short','signed','sizeof',
          'static','struct','switch','typedef','union','unsigned',
          'void','volatile','while']

#输入代码文件路径及完成等级(1,2,3,4)
#print("Please input one path:")
#path = input()
#print("Please input the level you want(1,2,3,4)")
#level = int(input())
path = 'D:/Dev-cpp'
reg = r'\b[a-zA-Z]+\b' #正则表达式匹配英文单词
file_list = os.listdir(path)


Count = {}
ls = []
text = replace_comment(path)
line = re.findall(reg,text) #正则表达式匹配所有符合要求的值，返回一个列表

for word in kw_list:
    num = line.count(word)
    if num != 0:
        Count[word] = num

items = list(Count.items())
count_sum = 0
for i in range(len(items)):
    kw , count = items[i]
    print(kw,'num : ',count)
    count_sum += count
print('total num :',count_sum)

switch_num = 0
switch_flag = 0 #标记此时正在记数一组内的case
case_num = 0
for kw in line:
    #print(kw)
    if kw == 'switch':
        switch_num += 1
        switch_flag = 1
    if switch_flag == 1 and kw == 'case':
        case_num += 1
    elif switch_flag == 1 and kw == 'default':
        print('Case num for No.{} switch: {}'.format(switch_num,case_num))
        switch_flag = 0
        case_num = 0


#将else if处理为elseif
text_elseif = replace_space(path)
line_elseif = re.findall(reg,text_elseif)
ifelse_num = 0
ifelifelse_num = 0
ifelifelse_flag = 0
stack = Stack()
for kw in line_elseif:
    if kw == 'if':
        stack.push('if')
    elif kw == 'elseif' and stack.value(-1) == 'if':
        stack.push('elseif')
    elif kw == 'else':
        #for i in range(stack.size()):
            #print(stack.value(i))
        #print('peek:', stack.peek())
        #print("-------------endend-----------")
        while (stack.value(-1) != 'if'):
            #print('------pop elseif------')
            ifelifelse_flag = 1
            stack.pop()
        stack.pop()
        if ifelifelse_flag:
            ifelifelse_num += 1
            ifelifelse_flag = 0
        else:
            ifelse_num += 1

print('if-else num: {}'.format(ifelse_num))
print('if-elif-else num: {}'.format(ifelifelse_num))



