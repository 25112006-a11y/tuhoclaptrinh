def nycu(doan):
    ten='trang hong mai '
    if doan in ten:
        print(' tra loi dung')
    else :
        print(' tra loi sai')
        doan_moi=input('nhap lai ten')
        nycu(doan_moi)
doan=input('doan ten nyc')
nycu(doan)

