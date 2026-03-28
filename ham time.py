import time
ten=input('nhap ten: ')
tuoi=int(input('nhap tuoi: '))
hientai=time.localtime()
nam=hientai.tm_year
print(f'nam{ten}dat 100 tuoi la ',(100-tuoi)+nam)