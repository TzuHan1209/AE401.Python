import random
num=random.randint(1,10)
number = int(input('number'))
while num != number:
    if num > number:
        print('太小')
    else :
        print('太大')
    print('you are wrong')
    number = int(input('number'))
print('you are right')
print(num)
