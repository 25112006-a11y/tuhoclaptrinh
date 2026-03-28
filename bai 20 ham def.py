def dau_tu(doanhthu,chiphi):
     roi=(doanhthu-chiphi)/chiphi
    if roi>=0.75:
        print ('nen dau tu')
    else :
        print ('ko nen dau tu')
doanhthu=int(input('nhap doanh thu'))
chiphi=int(input('nhap chi phi'))
dau_tu(doanhthu,chiphi)
