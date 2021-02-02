math=int(input('score'))
eng=int(input('score'))
if math >= 90 and eng >= 90 :
    print('you get a prize' )
elif math < 60 and eng < 60 :
    print('要處罰')
elif math < 60 or eng < 60 :
    print('加油')
elif math >= 60 and eng >= 60 :
    print('???')
    
