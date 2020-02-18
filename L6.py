scores=[["a","b","c","d","e"],[0,1,2,3,4]]
scores=["a",0,"b",1,"c",2,"d",3,"e",4]
name=[]
score=[]
for i in range(len(scores)):
    if i%2==0:
        name.append(scores[i])
    else:
        score.append(scores[i])
print(name)
print(score)
num=0
big=0
min=100
scores=[["a",0],["b",1],["c",2],["d",3],["e",4]]
for i in range(len(scores)):
    if scores[i][1]>big:
        big=scores[i][1]
        bigname=scores[i][0]
    if scores[i][1]<min:
        min=scores[i][1]
        minname=scores[i][0]
    num+=scores[i][1]
print("最高分:",big)
print("最高分名字:",bigname)
print("最低分:",min)
print("最低分名字:",minname)
print("平均",num/len(scores))
import turtle
alex=turtle.Turtle()
def draw_square(x):
    for i in range(4):
        alex.forward(x)
        alex.left(90)
draw_square(10)
draw_square(20)
draw_square(30)
draw_square(40)
def add3(x,y,z):
    sum=x+y+z
    return sum
add3(1,2,3)