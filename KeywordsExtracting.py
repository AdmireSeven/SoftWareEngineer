'''
author: Yaqi Zhang
Function: Keywords Extracting
Email: admireseven@163.com
'''

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

def kw_num():
    Count = {}
    for word in kw_list:
        num = line.count(word)
        if num != 0:
            Count[word] = num

    items = list(Count.items())
    count_sum = 0
    for i in range(len(items)):
        kw, count = items[i]
        print(kw, 'num : ', count)
        count_sum += count
    print('total num :', count_sum)

def switch_num():
    switch_num = 0
    switch_flag = 0  # 标记此时正在记数一组内的case
    case_num = []
    if line.count('switch') == 0:
        print('No switch')
        return 0
    for kw in line:
        # print(kw)
        if kw == 'switch':
            switch_num += 1
            switch_flag = 1
            case_num.append(0)
        if switch_flag == 1 and kw == 'case':
            #print(switch_num)
            case_num[switch_num-1] += 1
    for i in range(len(case_num)):
        print('Case num for No.{} switch: {}'.format(i+1, case_num[i]))


def if_else_elseif_num():
    # 将else if处理为elseif
    text_elseif = replace_space(path)
    line_elseif = re.findall(reg, text_elseif)
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
            # for i in range(stack.size()):
            # print(stack.value(i))
            # print('peek:', stack.peek())
            # print("-------------endend-----------")
            while (stack.value(-1) != 'if'):
                # print('------pop elseif------')
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

#输入代码文件路径及完成等级(1,2,3,4)
print("Please input one path:(eg:)")
path = input()
print("Please input the level you want(1,2,3,4)")
level = int(input())

reg = r'\b[a-zA-Z]+\b' #正则表达式匹配英文单词
# 正则表达式匹配所有符合要求的值，返回一个列表
#path = 'D:/Dev-cpp/example.cpp'
text = replace_comment(path)
line = re.findall(reg, text)
if level == 1:
    kw_num()
elif level == 2:
    switch_num()
else:
    if_else_elseif_num()
