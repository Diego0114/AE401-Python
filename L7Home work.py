name=[]
while True:
    a1=input("輸入名字(結束的話打0):")
    if a1=="0":
        break
    name.append(a1)
import random as r
n1=r.randint(0,len(name)-1)
verb=[]
while True:
    a2=input("輸入動詞(結束的話打0):")
    if a2=="0":
        break
    name.append(a2)
import random as rr
n2=rr.randint(0,len(verb)-1)
noun=[]
while True:
    a3=input("輸入名詞(結束的話打0):")
    if a3=="0":
        break
    name.append(a3)
import random as rrr
n3=rrr.randint(0,len(noun)-1)
print(name[n1]+verb[n2]+noun[n3])