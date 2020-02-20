pe=input("班級人數:")
li=[]
mi=0
bi=100
for i in range(int(pe)):
    s=input("分數0~100:")
    name=input("名字")
    s=int(s)
    li.append(s)
    if s>mi:
        mi=s
        name1=name
    if s<bi:
        bi=s
        name2=name
print("平均:",sum(li)/int(pe),)
print("最低分:",mi,name1)
print("最高分:",bi,name2)
