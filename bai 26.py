a=input('nhap 1 chuoi')
n1=''
n2=''
for i in a:
    if i.isdigit():
        n1+=i
    if i.isalpha():
        n2+=i
print(n1)
print(n2)