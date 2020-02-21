a=open("1.txt","a")
a.write("")
if a=="":
    mi=0
    bi=100
while True:
    s=int(input("分數0~100(不想再輸入的話打-1，如果要清除全部的分數的話打-2):"))
    if s==-1:
        break
    if s==-2:
        a=open("1.txt","w")
    name=input("名字")
    a=open("1.txt","a")
    a.write(str(s))
    a.write(name)
    if s>mi:
        mi=s
        name1=name
    if s<bi:
        bi=s
        name2=name
print("平均:",)
print("最低分:",mi,name1)
print("最高分:",bi,name2)
a=open("1.txt","a")
a.write(s)
a=open("1.txt","r")
print(a.read())