import random
num=random.randint(1,10)
number = int(input('number'))
while num != number:
        print('you are wrong')
        number = int(input('number'))
print('you are right')
print(num)
