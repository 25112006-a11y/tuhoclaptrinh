a=input('nhap 1 chuoi')
print(a[0],a[-1])
for i in range(len(a)):
    if i==0 or i==len(a)-1:
        print(a[i],end='')
