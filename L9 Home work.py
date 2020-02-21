word={}
while True:
    b=input("1:建立字彙表，2:列出所有單字，3:英翻中，4:中翻英，5:測驗學習解果，6:離開系統")
    if b=="1":
        eword=input("英文單字:")
        cword=input("中文單字:")
        word[eword]=cword
    elif b=="2":
        a=open("1.txt","w")
        for j,k in word.items():
            a.write(j+"\t"+k)
            print(j,k)
        a.close()
    elif b=="3":
        eword=input("英文單字:")
        for j,k in word.items():
            if eword==j:
                print(k)
    elif b=="4":
        cword=input("中文單字:")
        for j,k in word.items():
            if cword==k:
                print(j)
    elif b=="5":
        i=0
        a=0
        for j,k in word.items():
            print(j)
            cword=input("中文單字:")
            if cword==k:
                i+=1
                print("你答對了喔!")
            else:
                print("你答錯了喔")
            a+=1
        print(i,"/",a)
    elif b=="6":
        break 
