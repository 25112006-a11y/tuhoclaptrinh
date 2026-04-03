so_phan_tu=int(input('nhap vao so phan tu: '))
phan_tu=[]
dem=0
so_phan_tu_be_hon_5=0
while dem<so_phan_tu:
    dem+=1
    a=int(input(f'nhap vao phan tu thu{dem}: '))
    phan_tu.append(a)
print('list ban vua nhap la: ',phan_tu)
'''for i in phan_tu:
    if i>5:
        so_phan_tu_be_hon_5+=1
        print(f'so be hon 5 o vi tri thu{so_phan_tu_be_hon_5}')
print(f'co {so_phan_tu_be_hon_5} phan tu be hon 5')'''
lst_index=[]
for j in range(len(phan_tu)):
    if phan_tu[j]>5:
        so_phan_tu_be_hon_5+=1
        lst_index.append(j)
print(f'co {so_phan_tu_be_hon_5} so nho hon 5')
print('cac vi tri index cua cac so nho hon 5 la',lst_index)
