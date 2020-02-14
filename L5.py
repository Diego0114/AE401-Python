a=["游泳","羽毛球","籃球","足球"]
a.insert(2,"7")
a.pop()
a.append("學校")
p=input("班級人數:")
l=[]
m=0
b=100
for i in range(int(p)):
    s=input("分數0~100:")
    s=int(s)
    l.append(s)
    if s>m:
        c=s
    if s<b:
        d=s
print("平均:",sum(l)/int(p),"最高分:",m,"最低分:",b)