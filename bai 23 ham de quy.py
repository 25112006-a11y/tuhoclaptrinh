def giaithua(n):
    if n==0:
        return 1
    else:
        return n*giaithua(n-1)
a=giaithua(9)
print(a)
'''8*7*6*5*4*3*2*1
8*giaithua(8-1)
8*7*giaithua(7-1)
...'''
def fibonacy(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonacy(n-1)+fibonacy(n-2)
b=fibonacy(6)
print(b)
