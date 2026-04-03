lst=[]
so_phan_tu=int(input('nhap so phan tu'))
dem=0
while dem<so_phan_tu:
    dem+=1
    a=int(input(f'nhap vao phan tu thu{dem}'))
    lst.append(a)

lst_2=[]
for i in lst:
    lst_2.append(i**2)
print(lst_2)

dem2=0
for i in lst_2:
    if i>50:
        dem2+=1
print(f'list moi co {dem2} so lon hon 50')