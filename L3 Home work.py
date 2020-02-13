import random
a=random.randint(1,20)
c=0

while c<5:
    b=input("隨機取數1~20(猜五次):")
    c=c+1
    if 1<=int(b)<=20:
        if int(b)>a:
            print("太大了")
        elif int(b)<a:
            print("太小了")
        else:
            print("你答對了")
            print("玩了",c,"次")
            break
if c==5:
    print("game over")
    