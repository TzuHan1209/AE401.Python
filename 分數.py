s= []
max=0
min=101
a=0
num = int(input('人數'))
for i in range(num):
    score=int(input('分數'))
    s.append(score)
    a=a+score
    if score>max:
        max=score
    if score<min:
        min=score
print('最高',max)
print('最低',min)
print('平均',a/num)
