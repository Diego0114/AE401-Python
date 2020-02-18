num=int(input("人數"))
scoree=[]
for i in range(num):
    score=input("分數")
    scoree.append(score)
print("平均分:",sum(scoree)/len(scoree))
print("最高分:",max(scoree))
print("最低分:",min(scoree))
print("全部分數由小到大排:",sorted(scoree))
