'''
author: Yaqi Zhang
Function: Replace the comments
Email: admireseven@163.com
'''
#此题需求：字符串与注释一并替换
import os
import re
reg = r"(\/\*([^\*^\/]*|[\*^\/*]*|[^\**\/]*)*\*\/|\/\/.*|'.*'|\"([^\"]*)\")"
#reg = r"\/\/.*"
def replace_comment(file_name):
    '''
    替换注释
    :param file_name: 文件路径
    :return: 替换注释（字符串）后的str
    '''
    ls = []
    # 将输入的路径文件夹内所有文件的内容读取到text中
    if file_name.endswith('.cpp') or file_name.endswith('.c'):
        #print(file_name)
        fr = open(file_name, 'r', encoding='UTF-8')
        for line in fr:
            #print(line)
            #if (line != None):
            #   print(line)
            #ls.extend(line)  # 将多个列表合成一个列表
            ls.append(line)
        fr.close()
    text = "".join(ls)

    comment = re.finditer(reg,text)
    for match in comment:
        #print(match.group())
        text = text.replace(match.group(),' ')
    #print(text)
    return text
