'''
author: Yaqi Zhang
Function: Replace the space between 'else' and 'if'
Email: admireseven@163.com
'''
#此题需求：字符串与注释一并替换
import os
import re
reg = r"\be.*?f\b"
#reg = r"\/\/.*"
def replace_space(path):
    '''
    替换注释
    :param path: 文件路径
    :return: 替换注释（字符串）后的str
    '''
    ls = []
    file_list = os.listdir(path)
    # 将输入的路径文件夹内所有文件的内容读取到text中
    for count in range(len(file_list)):
        file_name = path + '/' + file_list[count]
        if file_name.endswith('.cpp'):
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
        text = text.replace(match.group(),'elseif')
    return text

