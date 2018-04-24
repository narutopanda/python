Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
str=input('请输入字符串：')

def f(x):
    if x==-1:
        return ''
    else:
        return str[x]+f(x-1)
print(f(len(str)-1))
