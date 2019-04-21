def yy():
    for i in range(0,5):
        yield i
        print('this time is ',i)
    print('game over')

if __name__ =='__main__':
    for i in yy():
        print(i)