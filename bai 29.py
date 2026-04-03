from math import sqrt
quest=['2+5+7=','sqrt(16)=','12%2=','5//2=']
for i in quest:
    ans=eval(i.strip('='))
    traloi=float(input(i))
    if traloi==ans:
        print('correct')
    else:
        print('incorrect,the answer is',ans)