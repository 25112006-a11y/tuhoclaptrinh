a=input('nhap vao mot chuoi')
print(a)
print(a[0],a[-1])
for i in range(len(a)):
    if i%2==0:
        print(a[i],end=' ')