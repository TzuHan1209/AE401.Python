import random
a=int(input('最大'))
b=int(input('最小'))
c=int(input('幾次機會'))
num=random.randint(b,a)
number = int(input('number'))
if num != number :
    for i in range(1,c):
        while number > a or number < b :
            print('輸入錯誤')
            number = int(input('number'))
        if num > number:
            print('太小')
        else:
            print('太大')
        print('you are wrong')
        c=c-1
        print('你還有',c,'次')
        number = int(input('number'))
print('you are right')
print(num)

    
