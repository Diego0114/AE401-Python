a=input("身高公尺")
b=input("體重公斤")
if float(b)/float(a)**2<18.5:
    print("過輕")
elif 18.5<=float(b)/float(a)**2<=24:
    print("正常")
else:
    print("過重")
