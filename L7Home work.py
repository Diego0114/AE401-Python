import random as r

name=[]
verb=[]
noun=[]

while True:
    a1=input("輸入名字(結束的話打0):")
    if a1=="0":
        break
    name.append(a1)
    
while True:
    a2=input("輸入動詞(結束的話打0):")
    if a2=="0":
        break
    verb.append(a2)

while True:
    a3=input("輸入名詞(結束的話打0):")
    if a3=="0":
        break
    noun.append(a3)

n1=r.randint(0,len(name)-1)
n2=r.randint(0,len(verb)-1)
n3=r.randint(0,len(noun)-1)

print(name[n1]+verb[n2]+noun[n3])
