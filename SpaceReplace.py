'''
author: Yaqi Zhang
Function: Replace the space between 'else' and 'if'
Email: admireseven@163.com
'''
import re
reg = r"\be.*?f\b"
#reg = r"\/\/.*"
def replace_space(text):
    '''
    替换注释
    :param text: 字符串
    :return: 替换注释（字符串）后的str
    '''
    comment = re.finditer(reg,text)
    for match in comment:
        #print(match.group())
        text = text.replace(match.group(),'elseif')
    return text

