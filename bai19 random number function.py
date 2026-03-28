from random import randrange
a=randrange(1,7)
b=randrange(1,7)
c=randrange(1,7)
d=a+b+c
lua_chon=input('doan tai hay xiu:')
if lua_chon=='tai':
    if d > 10:
        print('ban da trung thuog')
    else:
        print('chuc ban may man lan sau')
elif lua_chon=='xiu':
    if d < 10:
        print('ban da trung thuong')
    else:
        print('chuc ban may man lan sau')
print(a,b,c)