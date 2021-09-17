'''
author: Yaqi Zhang
Function: Keywords Extracting
Email: admireseven@163.com
'''

import os
import re
from CommentReplace import replace_comment
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
print(line)

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
