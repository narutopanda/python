str=input('请输入字符串：')

def f(x):
    if x==-1:
        return ''
    else:
        return str[x]+f(x-1)
print(f(len(str)-1))
