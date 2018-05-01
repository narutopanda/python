n=input('请输入A处圆盘个数：')
def hanoi(n,A,B,C):
    if n==1:
        print('move from',A,'to',C)
    else:
        hanoi(n-1,A,C,B)
        print('move from',A,'to',C)
        hanoi(n-1,B,A,C)
hanoi(int(n),'A','B','C')
