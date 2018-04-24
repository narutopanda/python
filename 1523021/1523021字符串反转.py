str = input('请输入若干字符：')
 
def f(x):
    if x == -1:
        return ''
    else:
        return str[x] + f(x-1)
 
print(f(len(str)-1))
