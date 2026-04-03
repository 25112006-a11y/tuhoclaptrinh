
a = input('vui long nhap mat khau:')
x=bool
y=bool
while True:
    for i in a:
        if i.isdigit():
            x=True
            break
        else:
            x=False
    for i in a:
        if i.isalpha():
            y=True
            break
        else:
            y=False
    if len(a)<6 or x==False or y==False:
        a=input('nhap lai mat khau, it nhat 6 ki tu,1 chu,1 so:')
    else:
        print('mat khau hop le')


b=input('moi nhap mat khau dang nhap he thong: ')
dem=0
while b!=a:
    dem+=1
    a=input(f'nhap lai mat khau,nhap sai{dem}/5 lan')
    if dem==5:
        print('ban nhap sai qua 5 lan,khoa dang nhap')
        break
else:
    print('dang nhap thanh cong')
