def roi(dt,cp):
    return (dt-cp)/cp
def quyetdinhdautu(roi):
    if roi>=0.75:
        return 'nen dau tu'
    else:
        return 'ko nen dau tu'
print('chuong trinh tinh roi')
cp=float(input('nhap vao chi phi'))
dt=float(input('nhap vao doanh thu'))
b=roi(dt,cp)
a=quyetdinhdautu(b)
print(a)
print(b)