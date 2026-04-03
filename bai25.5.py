def mat_khau():
    so_lan_sai=0
    while so_lan_sai<5:
        a=input('nhap mat khau')
        dem_chu=0
        dem_so=0
        b=len(a)
        for i in a:
            if i.isalpha() :
                dem_chu+=1
            if i.isdigit() :
                dem_so+=1
        if b>=6 and dem_chu>=1 and dem_so>=1 :
            print('mat khau hop le')
        else :
            so_lan_sai+=1
            print(' mat khau khong hop le, moi nhap lai')
    print('khoa dang nhap')
mat_khau()