num=int(input("班上人數:"))#輸入人數
slist=[]#設一個要儲存名字和分數的序列
for i in range(num):
    score=int(input("成績"))#輸入成績
    name=input("名字")#輸入名字
    slist.append(score)
    slist.append(name)
def ave (slist):#平均的函式
    t=0
    for j in range(0,num*2,2):
        t=t+(slist[j])
    return t#回傳
def maxx (slist):#最高分分數和最高分名字的函式
    maxxx=0
    for j in range(0,num*2,2):
        if slist[j]>=maxxx:
            maxxx=slist[j]
            maxxname=slist[j+1]
    print("最高分分數:",maxxx)#印出最高分分數
    print("最高分名字:",maxxname)#印出最高分名字
def minn (slist):#最低分分數和最低分名字的函式
    minnn=100
    for j in range(0,num*2,2):
        if slist[j]<=minnn:
            minnn=slist[j]
            minnname=slist[j+1]
    print("最低分分數:",minnn)#印出最低分分數
    print("最低分名字:",minnname)#印出最低分名字
tt=ave(slist)#創一個變數來接t
print("平均:",tt)#印出平均
maxx(slist)#召喚最高分分數和最高分名字的函式
minn(slist)#召喚最低分分數和最低分名字的函式
